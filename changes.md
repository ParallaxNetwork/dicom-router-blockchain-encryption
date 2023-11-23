[23-11-2023]:

- router.conf.template -- add mroc_client_url
- utils/config.py -- declare mroc_client_url
- main.py -- pass mroc_client_url to handle_assoc_released handler
- internal/dicom_handler.py -- handle_assoc_released func accepts new parameter mroc_client_url
- internal/mroc_client.py -- post_files_to_mroc_client func accepts new parameter mroc_client_url
