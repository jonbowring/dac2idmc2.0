import requests
import logging
import time
import shortuuid
from urllib.parse import quote

def upload_package(sessionID, taskflowName, config):

    # Initialise the log file
    logging.basicConfig(
    filename='logs/console.log',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s',
    )

    # Upload the zip file to idmc
    url = 'https://' + config['idmc']['pod'] + '.' + config['idmc']['host'] + '/saas/public/core/v3/import/package'
    headers = { 'INFA-SESSION-ID': sessionID }
    files = {'package': (f'{ taskflowName }.zip', open(f'out/{ taskflowName }.zip', 'rb'), 'application/zip')}
    r = requests.post(url=url, headers=headers, files=files)
    print(r.text)
    if r.status_code == 200:
        jobId = r.json()['jobId']
    else:
        logging.error('Upload of package failed. See below details:')
        logging.error('Method: ' + r.request.method)
        logging.error('Headers: ' + str(r.request.headers))
        logging.error('URL: ' + r.request.url)
        logging.error('Body: ' + str(r.request.body))
        logging.error('Hooks: ' + str(r.request.hooks))
        logging.error('Status: ' + str(r.status_code))
        logging.error('Response: ' + r.text)
        raise Exception('Upload of package failed. See log for more details.')
    
    # Start the import process
    url = 'https://' + config['idmc']['pod'] + '.' + config['idmc']['host'] + '/saas/public/core/v3/import/' + quote( jobId )
    headers = { 'Accept': 'application/json', 'Content-Type': 'application/json', 'INFA-SESSION-ID': sessionID }
    data = {
        'name' : taskflowName + '-' + shortuuid.uuid()[:8],
        'importSpecification' : {
            'defaultConflictResolution' : 'REUSE'
        }
    }
    r = requests.post(url=url, headers=headers, json=data)
    print(r.text)
    if r.status_code == 200:
        status = r.json()['status']['state']
    else:
        logging.error('Upload of package failed. See below details:')
        logging.error('Method: ' + r.request.method)
        logging.error('Headers: ' + str(r.request.headers))
        logging.error('URL: ' + r.request.url)
        logging.error('Body: ' + str(r.request.body))
        logging.error('Hooks: ' + str(r.request.hooks))
        logging.error('Status: ' + str(r.status_code))
        logging.error('Response: ' + r.text)
        raise Exception('Upload of package failed. See log for more details.')

    # Wait for the import job to finish
    maxWait = config['idmc']['maxWait']
    curWait = 0
    interval = 3
    while curWait < maxWait:
        url = 'https://' + config['idmc']['pod'] + '.' + config['idmc']['host'] + '/saas/public/core/v3/import/' + quote( jobId )
        headers = { 'Accept': 'application/json', 'INFA-SESSION-ID': sessionID }
        r = requests.get(url=url, headers=headers)
        print(r.text)
        if r.status_code == 200:
            status = r.json()['status']['state']
        else:
            logging.error('Upload of package failed. See below details:')
            logging.error('Method: ' + r.request.method)
            logging.error('Headers: ' + str(r.request.headers))
            logging.error('URL: ' + r.request.url)
            logging.error('Body: ' + str(r.request.body))
            logging.error('Hooks: ' + str(r.request.hooks))
            logging.error('Status: ' + str(r.status_code))
            logging.error('Response: ' + r.text)
            raise Exception('Upload of package failed. See log for more details.')

        if status == 'IN_PROGRESS':
            logging.info(f'Waiting for import of "{ taskflowName }.zip" to be processed.')
            curWait += interval
            time.sleep(interval)
        elif status == 'SUCCESSFUL':
            logging.info(f'Import of "{ taskflowName }.zip" completed successfully.')
            break
        else:
            break

    logging.info(f'Final status of "{ taskflowName }.zip" import was "{ status }".')
    return status