from pathlib import Path
import shutil
import uuid
import json
import hashlib
import logging

def package_import(taskflowID, taskflowName, dfPlan):

    # Initialise the log file
    logging.basicConfig(
    filename='logs/console.log',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s',
    )

    # Filter the plan for just the MTT steps
    dfMtts = dfPlan[['plan_step_type','step_name','infa_id','infa_path']].copy()
    dfMtts = dfMtts[dfMtts['plan_step_type'] == 'REGULAR'].drop_duplicates()


    logging.info(f'Adding the file "tmp/{ taskflowName }/Explore/Default.Project.json"...')

    # Copy in the Default.Project.json template file
    srcPath = Path('templates/Default.Project.json')
    tgtPath = Path(f'tmp/{ taskflowName }/Explore/Default.Project.json')
    shutil.copy(srcPath, tgtPath)




    logging.info(f'Adding the file "tmp/{ taskflowName }/ContentsofExportPackage_{ taskflowName }.csv"...')

    # Generate the ContentsofExportPackage
    content = f'''objectPath,objectName,objectType,id
/Explore,Default,Project,92TQndHw9hvjJrQafpLX2R
/Explore/Default,{ taskflowName },TASKFLOW,{ taskflowID }'''

    with open(f'tmp/{ taskflowName }/ContentsofExportPackage_{ taskflowName }.csv', 'w', encoding='utf-8') as file:
        file.write(content)




    logging.info(f'Adding the file "tmp/{ taskflowName }/exportMetadata.v2.json"...')

    # Generate the exportMetadata.v2.json file
    with open('templates/exportMetadata.v2.json', 'r', encoding='utf-8') as file:
        exportMetadata = json.load(file)

    exportMetadata['name'] = taskflowName
    exportedObjects = []

    # Include the MTT dependencies
    for idx, row in dfMtts.iterrows():
        obj = {
            "objectGuid": row['infa_id'],
            "objectName": row['step_name'],
            "objectType": "MTT",
            "path": "/Explore/" + "/".join(row['infa_path'].split("/")[:-1]),
            "metadata": {
                "modelVersion": {
                    "major": 0,
                    "minor": 0
                    },
                "repoInfo": {
                    "repoHandle": "010SU10Z00000000001I"
                    },
                "objectRefs": [],
                "contextAttributes": None,
                "additionalInfo": {
                    "description": "",
                    "contentType": "JSON",
                    "documentState": "VALID"
                    }
                }
            }
        exportedObjects.append(obj)

    # Update the taskflow names and ID
    for obj in exportMetadata['exportedObjects']:
        if obj['objectType'] == 'TASKFLOW':
            obj['objectGuid'] = taskflowID
            obj['objectName'] = taskflowName
            obj['metadata']['objectRefs'] = dfMtts['infa_id'].to_list() if len(dfMtts.index) > 0 else []

        exportedObjects.append(obj)



    exportMetadata['exportedObjects'] = exportedObjects

    # Save the file
    with open(f'tmp/{ taskflowName }/exportMetadata.v2.json', 'w', encoding='utf-8') as file:
        json.dump(exportMetadata, file, ensure_ascii=False, indent=4)




    logging.info(f'Adding the file "tmp/{ taskflowName }/exportPackage.chksum"...')

    # Generate the checksums
    with open(f'tmp/{ taskflowName }/Explore/Default.Project.json', 'rb') as infile:
        infileBytes = infile.read()
    defaultProjectJsonHash = hashlib.sha256(infileBytes).hexdigest().upper()

    with open(f'tmp/{ taskflowName }/exportMetadata.v2.json', 'rb') as infile:
        infileBytes = infile.read()
    exportMetadataHash = hashlib.sha256(infileBytes).hexdigest().upper()

    with open(f'tmp/{ taskflowName }/Explore/Default/{ taskflowName }.TASKFLOW.xml', 'rb') as infile:
        infileBytes = infile.read()
    taskflowHash = hashlib.sha256(infileBytes).hexdigest().upper()

    content = f'''#
#Fri Jul 04 02:03:23 UTC 2025
Explore/Default/{ taskflowName }.TASKFLOW.xml={ taskflowHash }
Explore/Default.Project.json={ defaultProjectJsonHash }
exportMetadata.v2.json={ exportMetadataHash }
'''

    # Save the checksums file
    with open(f'tmp/{ taskflowName }/exportPackage.chksum', 'w', encoding='utf-8') as file:
        file.write(content)




    logging.info(f'Compressing import package "out/{ taskflowName }"...')

    # Create the import zip file
    shutil.make_archive(f'out/{ taskflowName }', 'zip', Path(f'tmp/{ taskflowName }'))


