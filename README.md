# Tested on : 
- Unix based operating System (Ubuntu server)
- MacOS (arm64, Intel)

# Pre-requisite : 
1. Installed latest Anaconda version (Download [here](https://anaconda.com/products/distribution))
2. Ensure that the port 11112 is opened (default DICOM port)

# Setup :
1. Setup your target endpoint in ```router.conf``` in ```url```. Default is dev environment : ```api-satusehat-dev.dto.kemkes.go.id```
2. Insert your SATUSEHAT Organization ID, Client Key, and Secret Key on ```router.conf```. <br> If you don't have access, please access [SATUSEHAT Developer Portal](https://satusehat.kemkes.go.id/sign-up)
3. Run in terminal ```conda env create -n dicom-router -f conda.yml```

# How to run :
1. Activate conda environment : ```conda activate dicom-router```
2. Move to directory containing main.py : ```cd dicom-router```
3. Run main microservices : ```python main.py -v```

# Testing :
### Prerequisite : 
1. Download dcmtk from official site ```https://dicom.offis.de/dcmtk.php.en```

### Sending File
- Recursive (multislice file) : ```dcmsend 127.0.0.1 11112 --call DCMROUTER --scan-directories --recurse STUDY_MR```
- Single (singular file) : ```dcmsend 127.0.0.1 11112 --call DCMROUTER 03DBDF35.dcm```

# Version Update:
Last update : 
- 19 January 2023 : Initial Commit with Python Virtual Environment
- 20 January 2023 : Commit with conda.yml environment 
