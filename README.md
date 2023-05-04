# Tested on : 
- Unix based operating System (Ubuntu server) --> use conda-unix.yml
- MacOS (arm64, Intel) --> use conda-macos.yml
- Windows (Intel) --> use conda-win.yml

# Pre-requisite : 
1. Installed latest Anaconda version (Download [here](https://anaconda.com/products/distribution))
2. Ensure that the port 11112 is opened (default DICOM port)

# Setup :
1. Copy ```router.conf.template``` to ```router.conf```
2. Setup your target endpoint in ```router.conf``` in ```url```. Default is dev environment : ```api-satusehat-dev.dto.kemkes.go.id```
3. Insert your SATUSEHAT Organization ID, Client Key, and Secret Key on ```router.conf```. <br> If you don't have access, please access [SATUSEHAT Developer Portal](https://satusehat.kemkes.go.id/sign-up)
4. Run conda env creation in terminal based on .yml environment file provided

| Server OS    | Script |
| ----------- | ----------- |
| Unix      | ```conda env create -n dicom-router -f conda_env/conda-unix.yml```       |
| Windows   | ```conda env create -n dicom-router -f conda_env/conda-win.yml```       |
| MacOS M1  | ```conda env create -n dicom-router -f conda_env/conda-macos-m1.yml```       |
| MacOS Intel  | ```conda env create -n dicom-router -f conda_env/conda-macos-x-64.yml```       |


# How to run :
1. Activate conda environment : ```conda activate dicom-router```
2. Move to directory containing main.py : ```cd dicom-router```
3. Run main microservices : ```python main.py -v```

# Testing :
### Prerequisite : 
1. Download dcmtk from official site ```https://dicom.offis.de/dcmtk.php.en```

### Sending File
- Recursive (multislice file) : ```storescu --call DCMROUTER localhost 11112-- scan-directories --recurse STUDY_MR```
- Single (singular file) : ```storescu --call DCMROUTER localhost 11112 file.dcm```

### Sending File with JPEG lossless
- Recursive (multislice file) : ```storescu --call DCMROUTER -xs localhost 11112-- scan-directories --recurse STUDY_MR```
- Single (singular file) : ```storescu --call DCMROUTER -xs localhost 11112 file.dcm```

### Sending File with JPEG 2000 lossless
- Recursive (multislice file) : ```storescu --call DCMROUTER -xv localhost 11112-- scan-directories --recurse STUDY_MR```
- Single (singular file) : ```storescu --call DCMROUTER -xv localhost 11112 file.dcm```


# Version Update:
Last update : 
- 19 January 2023 : Initial Commit with Python Virtual Environment
- 20 January 2023 : Commit with conda.yml environment 
