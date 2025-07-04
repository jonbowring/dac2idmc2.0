from lxml import etree
import uuid
import logging

def generate_taskflow(taskflowID, taskflowName):


    # Initialise the log file
    logging.basicConfig(
        filename='logs/console.log',
        level=logging.DEBUG,
        format='%(asctime)s:%(levelname)s:%(message)s',
    )

    logging.info('Starting to generate the Taskflow XML files')


    #taskflowName = 'tf_Generated_Taskflow'
    #taskflowName


    #taskflowID = str(uuid.uuid4()).replace('-','')
    #taskflowID

    ######################################################################################
    # # Build XML
    ######################################################################################

    ######################################################################################
    # ## /aetgt:getResponse
    ######################################################################################


    logging.info('Building "/aetgt:getResponse" elements...')

    # Define the namespace map
    namespaces = {
        'aetgt': 'http://schemas.active-endpoints.com/appmodules/repository/2010/10/avrepository.xsd',
        'types1': 'http://schemas.active-endpoints.com/appmodules/repository/2010/10/avrepository.xsd'
    }

    # Create the "/aetgt:getResponse" element
    namespace_url = 'http://schemas.active-endpoints.com/appmodules/repository/2010/10/avrepository.xsd'
    namespace = "{%s}" % namespace_url
    root = etree.Element(namespace + "getResponse", nsmap=namespaces)

    # Create the "/aetgt:getResponse/types1:Item" element
    namespace_url = 'http://schemas.active-endpoints.com/appmodules/repository/2010/10/avrepository.xsd'
    namespace = "{%s}" % namespace_url
    getResponse_Item = etree.SubElement(root, namespace + "Item", nsmap={'types1': namespace_url})

    ######################################################################################
    # ## /aetgt:getResponse/types1:Item
    ######################################################################################


    logging.info('Building "/aetgt:getResponse/types1:Item" elements...')

    # Create the "/aetgt:getResponse/types1:Item/types1:EntryId" element
    namespace_url = 'http://schemas.active-endpoints.com/appmodules/repository/2010/10/avrepository.xsd'
    namespace = "{%s}" % namespace_url
    getResponse_Item_EntryId = etree.SubElement(getResponse_Item, namespace + "EntryId", nsmap={'types1': namespace_url})
    getResponse_Item_EntryId.text = "DEPOiVhC2g0aaaa-gt-58577-2025-02-07T05:28:41.474Z::tf.xml"

    # Create the "/aetgt:getResponse/types1:Item/types1:Name" element
    namespace_url = 'http://schemas.active-endpoints.com/appmodules/repository/2010/10/avrepository.xsd'
    namespace = "{%s}" % namespace_url
    getResponse_Item_Name = etree.SubElement(getResponse_Item, namespace + "Name", nsmap={'types1': namespace_url})
    getResponse_Item_Name.text = taskflowName

    # Create the "/aetgt:getResponse/types1:Item/types1:MimeType" element
    namespace_url = 'http://schemas.active-endpoints.com/appmodules/repository/2010/10/avrepository.xsd'
    namespace = "{%s}" % namespace_url
    getResponse_Item_MimeType = etree.SubElement(getResponse_Item, namespace + "MimeType", nsmap={'types1': namespace_url})
    getResponse_Item_MimeType.text = "application/xml+taskflow"

    # Create the "/aetgt:getResponse/types1:Item/types1:Description" element
    namespace_url = 'http://schemas.active-endpoints.com/appmodules/repository/2010/10/avrepository.xsd'
    namespace = "{%s}" % namespace_url
    getResponse_Item_Description = etree.SubElement(getResponse_Item, namespace + "Description", nsmap={'types1': namespace_url})

    # Create the "/aetgt:getResponse/types1:Item/types1:AppliesTo" element
    namespace_url = 'http://schemas.active-endpoints.com/appmodules/repository/2010/10/avrepository.xsd'
    namespace = "{%s}" % namespace_url
    getResponse_Item_AppliesTo = etree.SubElement(getResponse_Item, namespace + "AppliesTo", nsmap={'types1': namespace_url})

    # Create the "/aetgt:getResponse/types1:Item/types1:Tags" element
    namespace_url = 'http://schemas.active-endpoints.com/appmodules/repository/2010/10/avrepository.xsd'
    namespace = "{%s}" % namespace_url
    getResponse_Item_Tags = etree.SubElement(getResponse_Item, namespace + "Tags", nsmap={'types1': namespace_url})

    # Create the "/aetgt:getResponse/types1:Item/types1:VersionLabel" element
    namespace_url = 'http://schemas.active-endpoints.com/appmodules/repository/2010/10/avrepository.xsd'
    namespace = "{%s}" % namespace_url
    getResponse_Item_VersionLabel = etree.SubElement(getResponse_Item, namespace + "VersionLabel", nsmap={'types1': namespace_url})
    getResponse_Item_VersionLabel.text = "1.0"

    # Create the "/aetgt:getResponse/types1:Item/types1:State" element
    namespace_url = 'http://schemas.active-endpoints.com/appmodules/repository/2010/10/avrepository.xsd'
    namespace = "{%s}" % namespace_url
    getResponse_Item_State = etree.SubElement(getResponse_Item, namespace + "State", nsmap={'types1': namespace_url})
    getResponse_Item_State.text = "CURRENT"

    # Create the "/aetgt:getResponse/types1:Item/types1:ProcessGroup" element
    namespace_url = 'http://schemas.active-endpoints.com/appmodules/repository/2010/10/avrepository.xsd'
    namespace = "{%s}" % namespace_url
    getResponse_Item_ProcessGroup = etree.SubElement(getResponse_Item, namespace + "ProcessGroup", nsmap={'types1': namespace_url})

    # Create the "/aetgt:getResponse/types1:Item/types1:CreatedBy" element
    namespace_url = 'http://schemas.active-endpoints.com/appmodules/repository/2010/10/avrepository.xsd'
    namespace = "{%s}" % namespace_url
    getResponse_Item_CreatedBy = etree.SubElement(getResponse_Item, namespace + "CreatedBy", nsmap={'types1': namespace_url})
    getResponse_Item_CreatedBy.text = "jbowring_APJS_tspod_SO"

    # Create the "/aetgt:getResponse/types1:Item/types1:CreationDate" element
    namespace_url = 'http://schemas.active-endpoints.com/appmodules/repository/2010/10/avrepository.xsd'
    namespace = "{%s}" % namespace_url
    getResponse_Item_CreationDate = etree.SubElement(getResponse_Item, namespace + "CreationDate", nsmap={'types1': namespace_url})
    getResponse_Item_CreationDate.text = "2025-02-07T05:28:41Z"

    # Create the "/aetgt:getResponse/types1:Item/types1:ModifiedBy" element
    namespace_url = 'http://schemas.active-endpoints.com/appmodules/repository/2010/10/avrepository.xsd'
    namespace = "{%s}" % namespace_url
    getResponse_Item_ModifiedBy = etree.SubElement(getResponse_Item, namespace + "ModifiedBy", nsmap={'types1': namespace_url})

    # Create the "/aetgt:getResponse/types1:Item/types1:PublicationStatus" element
    namespace_url = 'http://schemas.active-endpoints.com/appmodules/repository/2010/10/avrepository.xsd'
    namespace = "{%s}" % namespace_url
    getResponse_Item_PublicationStatus = etree.SubElement(getResponse_Item, namespace + "PublicationStatus", nsmap={'types1': namespace_url})
    getResponse_Item_PublicationStatus.text = "unpublished"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry" element
    namespace_url = 'http://schemas.active-endpoints.com/appmodules/repository/2010/10/avrepository.xsd'
    namespace = "{%s}" % namespace_url
    getResponse_Item_Entry = etree.SubElement(getResponse_Item, namespace + "Entry", nsmap={'types1': namespace_url})


    ######################################################################################
    # ## /aetgt:getResponse/types1:Item/types1:Entry
    ######################################################################################


    logging.info('Building "/aetgt:getResponse/types1:Item/types1:Entry" elements...')

    # Define the namespace map
    namespaces = {
        "tfm": "http://schemas.active-endpoints.com/appmodules/screenflow/2021/04/taskflowModel.xsd",
        "list": "urn:activevos:spi:list:functions"
    }

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow" element
    getResponse_Item_Entry_taskflow = etree.SubElement(getResponse_Item_Entry, "taskflow", attrib={ 
        "xmlns": "http://schemas.active-endpoints.com/appmodules/screenflow/2010/10/avosScreenflow.xsd",
        "displayName": taskflowName,
        "overrideAPIName": "false"
        },
        nsmap=namespaces)

    ######################################################################################
    # ## /aetgt:getResponse/types1:Item/types1:Entry/taskflow
    ######################################################################################


    logging.info('Building "/aetgt:getResponse/types1:Item/types1:Entry/taskflow" elements...')

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/parameterSet" element
    getResponse_Item_Entry_taskflow_parameterSet = etree.SubElement(getResponse_Item_Entry_taskflow, "parameterSet", attrib={ 
        "xmlns": "http://schemas.active-endpoints.com/appmodules/screenflow/2021/04/taskflowModel.xsd"
        })

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/appliesTo" element
    getResponse_Item_Entry_taskflow_appliesTo = etree.SubElement(getResponse_Item_Entry_taskflow, "appliesTo")

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/description" element
    getResponse_Item_Entry_taskflow_description = etree.SubElement(getResponse_Item_Entry_taskflow, "description")

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/tags" element
    getResponse_Item_Entry_taskflow_tags = etree.SubElement(getResponse_Item_Entry_taskflow, "tags")

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/generator" element
    getResponse_Item_Entry_taskflow_generator = etree.SubElement(getResponse_Item_Entry_taskflow, "generator")
    getResponse_Item_Entry_taskflow_generator.text = "Informatica Process Designer 11"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/notes" element
    getResponse_Item_Entry_taskflow_notes = etree.SubElement(getResponse_Item_Entry_taskflow, "notes")

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/deployment" element
    getResponse_Item_Entry_taskflow_deployment = etree.SubElement(getResponse_Item_Entry_taskflow, "deployment", attrib={
        "skipIfRunning": "false", 
        "suspendOnFault": "false",
        "tracingLevel": "verbose"
    })

    ######################################################################################
    # ## /aetgt:getResponse/types1:Item/types1:Entry/taskflow/deployment
    ######################################################################################

    logging.info('Building "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/deployment" elements...')

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/deployment/rest" element
    getResponse_Item_Entry_taskflow_deployment_rest = etree.SubElement(getResponse_Item_Entry_taskflow_deployment, "rest")

    ######################################################################################
    # ## /aetgt:getResponse/types1:Item/types1:Entry/taskflow
    ######################################################################################


    logging.info('Building "/aetgt:getResponse/types1:Item/types1:Entry/taskflow" elements...')

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/extData" element
    getResponse_Item_Entry_taskflow_extData = etree.SubElement(getResponse_Item_Entry_taskflow, "extData")

    ######################################################################################
    # ## /aetgt:getResponse/types1:Item/types1:Entry/taskflow/extData
    ######################################################################################


    logging.info('Building "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/extData" elements...')

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/extData/nvpair" element
    getResponse_Item_Entry_taskflow_extData_nvpair1 = etree.SubElement(getResponse_Item_Entry_taskflow_extData, "nvpair", attrib={
        "name": "treatEmptyStringAsNotNull"
    })
    getResponse_Item_Entry_taskflow_extData_nvpair1.text = "false"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/extData/nvpair" element
    getResponse_Item_Entry_taskflow_extData_nvpair2 = etree.SubElement(getResponse_Item_Entry_taskflow_extData, "nvpair", attrib={
        "name": "treatEmptyObjectListAsArray"
    })
    getResponse_Item_Entry_taskflow_extData_nvpair2.text = "false"

    ######################################################################################
    # ## /aetgt:getResponse/types1:Item/types1:Entry/taskflow
    ######################################################################################


    logging.info('Building "/aetgt:getResponse/types1:Item/types1:Entry/taskflow" elements...')

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow" element
    getResponse_Item_Entry_taskflow_flow = etree.SubElement(getResponse_Item_Entry_taskflow, "flow", attrib={
        "id": "a"
    })

    ######################################################################################
    # ## /aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow
    ######################################################################################


    logging.info('Building "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow" elements...')

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/start" element
    getResponse_Item_Entry_taskflow_flow_start = etree.SubElement(getResponse_Item_Entry_taskflow_flow, "start", attrib={
        "id": "b"
    })

    ######################################################################################
    # ## /aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/start
    ######################################################################################


    logging.info('Building "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/start" elements...')

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/start/link" element
    getResponse_Item_Entry_taskflow_flow_end = etree.SubElement(getResponse_Item_Entry_taskflow_flow_start, "link", attrib={
        "id": "link1",
        "targetId": "c"
    })

    ######################################################################################
    # ## /aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow
    ######################################################################################


    logging.info('Building "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow" elements...')

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/end" element
    getResponse_Item_Entry_taskflow_flow_end = etree.SubElement(getResponse_Item_Entry_taskflow_flow, "end", attrib={
        "id": "c"
    })

    ######################################################################################
    # ## /aetgt:getResponse/types1:Item
    ######################################################################################


    logging.info('Building "/aetgt:getResponse/types1:Item" elements...')

    # Create the "/aetgt:getResponse/types1:Item/types1:GUID" element
    namespace_url = 'http://schemas.active-endpoints.com/appmodules/repository/2010/10/avrepository.xsd'
    namespace = "{%s}" % namespace_url
    getResponse_Item_GUID = etree.SubElement(getResponse_Item, namespace + "GUID", nsmap={'types1': namespace_url})
    getResponse_Item_GUID.text = taskflowID

    # Create the "/aetgt:getResponse/types1:Item/types1:DisplayName" element
    namespace_url = 'http://schemas.active-endpoints.com/appmodules/repository/2010/10/avrepository.xsd'
    namespace = "{%s}" % namespace_url
    getResponse_Item_DisplayName = etree.SubElement(getResponse_Item, namespace + "DisplayName", nsmap={'types1': namespace_url})
    getResponse_Item_DisplayName.text = taskflowName

    ######################################################################################
    # ## /aetgt:getResponse
    ######################################################################################


    logging.info('Building "/aetgt:getResponse" elements...')

    # Create the "/aetgt:getResponse/types1:CurrentServerDateTime" element
    namespace_url = 'http://schemas.active-endpoints.com/appmodules/repository/2010/10/avrepository.xsd'
    namespace = "{%s}" % namespace_url
    getResponse_CurrentServerDateTime = etree.SubElement(root, namespace + "CurrentServerDateTime", nsmap={'types1': namespace_url})
    getResponse_CurrentServerDateTime.text = "2025-02-07T05:29:29.149Z"



    ######################################################################################
    # ## Save the XML file
    ######################################################################################


    logging.info('Finished building the XML')

    logging.info(f'Saving the XML file "out/{ taskflowName }.TASKFLOW.xml"')

    # Create an ElementTree object from the root element
    tree = etree.ElementTree(root)

    # Write the XML to a file with pretty print
    with open(f"tmp/{ taskflowName }/Explore/Default/{ taskflowName }.TASKFLOW.xml", "wb") as f:
        tree.write(f, pretty_print=True, xml_declaration=False, encoding="UTF-8")

    logging.info('Save successful')


