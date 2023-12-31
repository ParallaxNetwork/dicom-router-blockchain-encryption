import configparser
import logging
import os
import shutil
from pynetdicom import AE, evt, AllStoragePresentationContexts, debug_logger, StoragePresentationContexts, ALL_TRANSFER_SYNTAXES
from internal import dicom_handler, http_server
from utils.dicom2fhir import process_dicom_2_fhir
from time import sleep
from pydicom.uid import JPEGLosslessSV1, JPEG2000Lossless
from utils.dbquery import dbquery
from utils import config

# from pynetdicom.sop_class import Verification

from pynetdicom.sop_class import (
    Verification,
    PatientRootQueryRetrieveInformationModelFind,
    PatientRootQueryRetrieveInformationModelMove,
    PatientRootQueryRetrieveInformationModelGet,
    StudyRootQueryRetrieveInformationModelFind,
    StudyRootQueryRetrieveInformationModelMove,
    StudyRootQueryRetrieveInformationModelGet,
    ModalityWorklistInformationFind,
)


config.init()

global token
token = str()

debug_logger()
LOGGER = logging.getLogger('pynetdicom')

# Implement a handler for evt.EVT_C_STORE

# ====================================================
# Main
# ====================================================

LOGGER.info("[Init] - Starting services")

# Setup database
dbq = dbquery()

# Setup event handlers
LOGGER.info("[Init] - Set up store handler")
handlers = [
    (evt.EVT_C_STORE, dicom_handler.handle_store, [config.dcm_dir, LOGGER]),
    (evt.EVT_RELEASED, dicom_handler.handle_assoc_released, [config.dcm_dir, config.organization_id, config.mroc_client_url, LOGGER]),
    (evt.EVT_C_ECHO, dicom_handler.handle_echo, [LOGGER]),
    (evt.EVT_C_FIND, dicom_handler.handle_find,[LOGGER]),
]

# Initialise the Application Entity
ae = AE(ae_title=config.self_ae_title)

transfer_syntaxes = ALL_TRANSFER_SYNTAXES

for context in StoragePresentationContexts:
    ae.add_supported_context(context.abstract_syntax, transfer_syntaxes)

# Support verification SCP (echo)
ae.add_supported_context(Verification)

# Query/Retrieve SCP
ae.add_supported_context(PatientRootQueryRetrieveInformationModelFind)
ae.add_supported_context(PatientRootQueryRetrieveInformationModelMove)
ae.add_supported_context(PatientRootQueryRetrieveInformationModelGet)
ae.add_supported_context(StudyRootQueryRetrieveInformationModelFind)
ae.add_supported_context(StudyRootQueryRetrieveInformationModelMove)
ae.add_supported_context(StudyRootQueryRetrieveInformationModelGet)
ae.add_supported_context(ModalityWorklistInformationFind)

# Support presentation contexts for all storage SOP Classes
ae.supported_contexts = AllStoragePresentationContexts

# Set to require the *Called AE Title* must match the AE title
ae.require_called_aet = config.self_ae_title

# Purge and re-create the incoming folder
LOGGER.info("[Init] - Clearing incoming folder")
try:
    shutil.rmtree(os.getcwd()+config.dcm_dir)
except BaseException as err:
    LOGGER.error(err)
os.mkdir(os.getcwd()+config.dcm_dir)

# Start listening for incoming association requests

pid = os.fork()

if pid > 0:
    LOGGER.info("[Init] - Spawning DICOM interface on port " +
          str(config.dicom_port)+" with AE title: "+config.self_ae_title+".")
    ae.start_server(("0.0.0.0", config.dicom_port), evt_handlers=handlers)
else:
    LOGGER.info(f'[Init] - Starting HTTP service on port {config.http_port}...')
    http_server.start_server(config.http_port)
