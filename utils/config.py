import configparser

def init():
  global config, url, organization_id, dicom_pathsuffix, fhir_pathsuffix, dicom_port, dcm_dir, http_port, self_ae_title, mroc_client_url
  global client_key, secret_key

  config = configparser.ConfigParser()
  config.read('router.conf')
  url = config.get('satusehat', 'url')
  organization_id = config.get('satusehat', 'organization_id')
  dicom_pathsuffix = config.get('satusehat', 'dicom_pathsuffix')
  fhir_pathsuffix = config.get('satusehat', 'fhir_pathsuffix')
  self_ae_title = config.get('satusehat', 'ae_title')
  dicom_port = int(config.get('satusehat', 'dicom_port'))
  dcm_dir = config.get('satusehat', 'dcm_dir')
  http_port = int(config.get('satusehat', 'http_port'))
  client_key = config.get('satusehat', 'client_key')
  secret_key = config.get('satusehat', 'secret_key')
  mroc_client_url = config.get('satusehat', 'mroc_client_url')


