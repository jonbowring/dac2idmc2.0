from lxml import etree
import uuid
import re
import logging

def generate_taskflow(taskflowID, taskflowName, dfPlan):


    # Initialise the log file
    logging.basicConfig(
        filename='logs/console.log',
        level=logging.DEBUG,
        format='%(asctime)s:%(levelname)s:%(message)s',
    )

    logging.info('Starting to generate the Taskflow XML files')

    # Get the unique list of step orders
    dfPlan = dfPlan.sort_values('plan_step_order')
    order_list = dfPlan['plan_step_order'].unique()
    dfMtts = dfPlan[['plan_step_type','step_name','infa_id','infa_path']].copy()
    dfMtts = dfMtts[dfMtts['plan_step_type'] == 'REGULAR'].drop_duplicates()

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

    '''
    <aetgt:getResponse xmlns:aetgt="http://schemas.active-endpoints.com/appmodules/repository/2010/10/avrepository.xsd"
                   xmlns:types1="http://schemas.active-endpoints.com/appmodules/repository/2010/10/avrepository.xsd">
        <types1:Item>
        </types1:Item>
        <types1:CurrentServerDateTime>2025-07-04T05:15:19.236Z</types1:CurrentServerDateTime>
    </aetgt:getResponse>
    '''

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

    '''
    <types1:Item>
        <types1:EntryId>pJ7XhFtybduaa-gt-185706-2025-07-04T02:45:06.256Z::tf.xml</types1:EntryId>
        <types1:Name>tf_Base_Taskflow</types1:Name>
        <types1:MimeType>application/xml+taskflow</types1:MimeType>
        <types1:Description/>
        <types1:AppliesTo/>
        <types1:Tags/>
        <types1:VersionLabel>1.0</types1:VersionLabel>
        <types1:State>CURRENT</types1:State>
        <types1:ProcessGroup/>
        <types1:CreatedBy>jbowring_APJS_tspod_SO</types1:CreatedBy>
        <types1:CreationDate>2025-07-04T02:45:06Z</types1:CreationDate>
        <types1:ModifiedBy>jbowring_APJS_tspod_SO</types1:ModifiedBy>
        <types1:ModificationDate>2025-07-04T05:14:59Z</types1:ModificationDate>
        <types1:PublicationStatus>unpublished</types1:PublicationStatus>
        <types1:Entry>
        </types1:Entry>
        <types1:GUID>0MMbu6TFO6Wfp2SONVzaQi</types1:GUID>
        <types1:DisplayName>tf_Base_Taskflow</types1:DisplayName>
    </types1:Item>
    '''

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

    '''
    <types1:Entry>
        <taskflow xmlns="http://schemas.active-endpoints.com/appmodules/screenflow/2010/10/avosScreenflow.xsd"
            xmlns:tfm="http://schemas.active-endpoints.com/appmodules/screenflow/2021/04/taskflowModel.xsd"
            xmlns:list="urn:activevos:spi:list:functions"
            displayName="tf_Base_Taskflow"
            name="tf_Base_Taskflow"
            overrideAPIName="false">
        </taskflow>
    </types1:Entry>
    '''


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

    '''
    <taskflow xmlns="http://schemas.active-endpoints.com/appmodules/screenflow/2010/10/avosScreenflow.xsd"
            xmlns:tfm="http://schemas.active-endpoints.com/appmodules/screenflow/2021/04/taskflowModel.xsd"
            xmlns:list="urn:activevos:spi:list:functions"
            displayName="tf_Base_Taskflow"
            name="tf_Base_Taskflow"
            overrideAPIName="false">
        <parameterSet xmlns="http://schemas.active-endpoints.com/appmodules/screenflow/2021/04/taskflowModel.xsd"/>
        <appliesTo/>
        <description/>
        <tags/>
        <generator>Informatica Process Designer 11</generator>
        <tempFields>
                </tempFields>
        <notes/>
        <deployment skipIfRunning="false"
                    suspendOnFault="false"
                    tracingLevel="verbose">
            <rest/>
        </deployment>
        <extData>
            <nvpair name="treatEmptyStringAsNotNull">false</nvpair>
            <nvpair name="treatEmptyObjectListAsArray">false</nvpair>
        </extData>
        <flow id="a">
                </flow>
        <dependencies>
                </dependencies>
    </taskflow>
    '''


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

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/tempFields" element
    getResponse_Item_Entry_taskflow_tempFields = etree.SubElement(getResponse_Item_Entry_taskflow, "tempFields")

    ######################################################################################
    # ## /aetgt:getResponse/types1:Item/types1:Entry/taskflow/tempFields
    ######################################################################################

    '''
    <tempFields>
        <field description=""
                name="SDE_ORA_EmployeeDailySnapshotFact_2"
                type="reference">
            <options>
                <option name="failOnNotRun">false</option>
                <option name="failOnFault">false</option>
                <option name="referenceTo">$po:SDE-ORA-EmployeeDailySnapshotFact-2-a0Ks8uNXYKLg38LRNzw6gv</option>
            </options>
        </field>
    </tempFields>
    '''

    #TODO add loop to add field for each unique MTT
    for idx, row in dfMtts.iterrows():

        step_name = row['step_name']
        infa_id = row['infa_id']
        
        # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/tempFields/field" element
        getResponse_Item_Entry_taskflow_tempFields_field = etree.SubElement(getResponse_Item_Entry_taskflow_tempFields, "field", attrib={
            "description": "",
            "name": step_name, 
            "type": "reference"
        })

        # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/tempFields/options" element
        getResponse_Item_Entry_taskflow_tempFields_options = etree.SubElement(getResponse_Item_Entry_taskflow_tempFields_field, "options")

        # Create the "/aetgt:getResponse/types1:Item/types1:Entry/tempFields/options/option" element
        getResponse_Item_Entry_taskflow_tempFields_options_option1 = etree.SubElement(getResponse_Item_Entry_taskflow_tempFields_options, "option", attrib={
            "name": "failOnNotRun"
        })
        getResponse_Item_Entry_taskflow_tempFields_options_option1.text = "false"

        # Create the "/aetgt:getResponse/types1:Item/types1:Entry/tempFields/options/option" element
        getResponse_Item_Entry_taskflow_tempFields_options_option2 = etree.SubElement(getResponse_Item_Entry_taskflow_tempFields_options, "option", attrib={
            "name": "failOnFault"
        })
        getResponse_Item_Entry_taskflow_tempFields_options_option2.text = "false"

        # Create the "/aetgt:getResponse/types1:Item/types1:Entry/tempFields/options/option" element
        getResponse_Item_Entry_taskflow_tempFields_options_option3 = etree.SubElement(getResponse_Item_Entry_taskflow_tempFields_options, "option", attrib={
            "name": "referenceTo"
        })
        #TODO update reference name and ID
        getResponse_Item_Entry_taskflow_tempFields_options_option3.text = f"$po:{ re.sub(r'[^A-Za-z0-9]', '-', step_name) }-{ infa_id }"


    ######################################################################################
    # ## /aetgt:getResponse/types1:Item/types1:Entry/taskflow
    ######################################################################################

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

    '''
    <flow id="a">
        <start id="b">
            <link id="mcoczikm"
                targetId="mcoczil9"/>
        </start>
        <eventContainer id="mcoczil9">
        <service id="mcoczikl">
        </service>
        <link id="mcoczikn"
                targetId="c"/>
        <events>
        </events>
        </eventContainer>
        <end id="c"/>
    </flow>
    '''


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
    # ## /aetgt:getResponse/types1:Item/types1:Entry/taskflow
    ######################################################################################


    logging.info('Building "/aetgt:getResponse/types1:Item/types1:Entry/taskflow" elements...')

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/dependencies" element
    getResponse_Item_Entry_taskflow_dependencies = etree.SubElement(getResponse_Item_Entry_taskflow, "dependencies")

    ######################################################################################
    # ## /aetgt:getResponse/types1:Item/types1:Entry/taskflow/dependencies
    ######################################################################################

    '''
    <dependencies>
        <processObject xmlns="http://schemas.active-endpoints.com/appmodules/screenflow/2011/06/avosHostEnvironment.xsd"
                        displayName="SDE-ORA-EmployeeDailySnapshotFact-2-a0Ks8uNXYKLg38LRNzw6gv"
                        isByCopy="true"
                        name="SDE-ORA-EmployeeDailySnapshotFact-2-a0Ks8uNXYKLg38LRNzw6gv">
            <description/>
            <tags/>
            <detail>
                <field label="TaskProperties Parameters"
                    name="taskProperties"
                    nullable="true"
                    required="false"
                    type="reference"/>
                <field label="Output Parameters"
                    name="output"
                    nullable="true"
                    required="false"
                    type="reference"/>
                <field label="Fault"
                    name="fault"
                    nullable="true"
                    required="false"
                    type="reference"/>
                <field label="Max Wait (Seconds)"
                    name="Max_Wait"
                    nullable="true"
                    required="false"
                    type="int"/>
            </detail>
        </processObject>
    </dependencies>
    '''


    logging.info('Building "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/dependencies" elements...')

    # Add dependencies for each session
    for idx, row in dfMtts.iterrows():

        step_name = row['step_name']
        infa_id = row['infa_id']
        
        # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/dependencies/processObject" element
        getResponse_Item_Entry_taskflow_dependencies_processObject = etree.SubElement(getResponse_Item_Entry_taskflow_dependencies, "processObject", attrib={
            "xmlns": "http://schemas.active-endpoints.com/appmodules/screenflow/2011/06/avosHostEnvironment.xsd",
            "displayName": f"{ re.sub(r'[^A-Za-z0-9]', '-', step_name) }-{ infa_id }",
            "isByCopy": "true",
            "name": f"{ re.sub(r'[^A-Za-z0-9]', '-', step_name) }-{ infa_id }"
        })

        # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/dependencies/processObject/description" element
        getResponse_Item_Entry_taskflow_dependencies_processObject_description = etree.SubElement(getResponse_Item_Entry_taskflow_dependencies_processObject, "description")

        # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/dependencies/processObject/tags" element
        getResponse_Item_Entry_taskflow_dependencies_processObject_tags = etree.SubElement(getResponse_Item_Entry_taskflow_dependencies_processObject, "tags")

        # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/dependencies/processObject/detail" element
        getResponse_Item_Entry_taskflow_dependencies_processObject_detail = etree.SubElement(getResponse_Item_Entry_taskflow_dependencies_processObject, "detail")

        # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/dependencies/processObject/detail/field" element
        getResponse_Item_Entry_taskflow_dependencies_processObject_detail_field1 = etree.SubElement(getResponse_Item_Entry_taskflow_dependencies_processObject_detail, "field", attrib={
            "label": "TaskProperties Parameters",
            "name": "taskProperties",
            "nullable": "true",
            "required": "false",
            "type": "reference"
        })

        # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/dependencies/processObject/detail/field" element
        getResponse_Item_Entry_taskflow_dependencies_processObject_detail_field2 = etree.SubElement(getResponse_Item_Entry_taskflow_dependencies_processObject_detail, "field", attrib={
            "label": "Output Parameters",
            "name": "output",
            "nullable": "true",
            "required": "false",
            "type": "reference"
        })

        # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/dependencies/processObject/detail/field" element
        getResponse_Item_Entry_taskflow_dependencies_processObject_detail_field3 = etree.SubElement(getResponse_Item_Entry_taskflow_dependencies_processObject_detail, "field", attrib={
            "label": "Fault",
            "name": "fault",
            "nullable": "true",
            "required": "false",
            "type": "reference"
        })

        # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/dependencies/processObject/detail/field" element
        getResponse_Item_Entry_taskflow_dependencies_processObject_detail_field4 = etree.SubElement(getResponse_Item_Entry_taskflow_dependencies_processObject_detail, "field", attrib={
            "label": "Max Wait (Seconds)",
            "name": "Max_Wait",
            "nullable": "true",
            "required": "false",
            "type": "int"
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


