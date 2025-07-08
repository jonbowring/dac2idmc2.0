from lxml import etree
import uuid
import shortuuid
import re
import logging

def add_task(parent, infa_id, step_id, step_name, next_id, create_link):
    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer" element
    getResponse_Item_Entry_taskflow_flow_eventContainer = etree.SubElement(parent, "eventContainer", attrib={
        "id": step_id
    })

    '''
    <service id="mcoczikl">
        <title>SDE_ORA_EmployeeDailySnapshotFact_2</title>
        <serviceName>ICSExecuteDataTask</serviceName>
        <serviceGUID/>
        <serviceInput>
            ...
        </serviceInput>
        <serviceOutput>
            ...
        </serviceOutput>
    </service>
    '''

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer, "service", attrib={
        #"id": str(uuid.uuid4()).replace('-','')
        "id": "svc" + shortuuid.uuid()[:8]
    })

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/title" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_title = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service, "title")
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_title.text = step_name

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceName" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceName = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service, "serviceName")
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceName.text = "ICSExecuteDataTask"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceGUID" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceGUID = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service, "serviceGUID")

    '''
    <serviceInput>
        <parameter name="Wait for Task to Complete" source="constant" updatable="true">true</parameter>
        <parameter name="Max Wait" source="constant" updatable="true">604800</parameter>
        <parameter name="Task Name" source="constant" updatable="true">SDE_ORA_EmployeeDailySnapshotFact_2</parameter>
        <parameter name="GUID" source="constant" updatable="true">a0Ks8uNXYKLg38LRNzw6gv</parameter>
        <parameter name="Task Type" source="constant" updatable="true">MCT</parameter>
        <parameter name="Has Inout Parameters" source="constant" updatable="true">false</parameter>
        <parameter name="taskField" source="nested">
            <operation source="field"
                        to="SDE-ORA-EmployeeDailySnapshotFact-2-a0Ks8uNXYKLg38LRNzw6gv">temp.SDE_ORA_EmployeeDailySnapshotFact_2</operation>
        </parameter>
    </serviceInput>
    '''

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service, "serviceInput")

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param1 = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput, "parameter", attrib={
        "name": "Wait for Task to Complete",
        "source": "constant",
        "updatable": "true"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param1.text = "true"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param2 = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput, "parameter", attrib={
        "name": "Max Wait",
        "source": "constant",
        "updatable": "true"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param2.text = "604800"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param3 = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput, "parameter", attrib={
        "name": "Task Name",
        "source": "constant",
        "updatable": "true"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param3.text = step_name

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param4 = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput, "parameter", attrib={
        "name": "GUID",
        "source": "constant",
        "updatable": "true"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param4.text = infa_id

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param5 = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput, "parameter", attrib={
        "name": "Task Type",
        "source": "constant",
        "updatable": "true"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param5.text = "MCT"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param6 = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput, "parameter", attrib={
        "name": "Has Inout Parameters",
        "source": "constant",
        "updatable": "true"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param6.text = "false"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param7 = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput, "parameter", attrib={
        "name": "taskField",
        "source": "nested"
    })

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param7_operation = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param7, "operation", attrib={
        "source": "field",
        "to": f"{ re.sub(r'[^A-Za-z0-9]', '-', step_name) }-{ infa_id }"
        #"to": f"{ re.sub(r'[^A-Za-z0-9]', '-', step_name) }"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param7_operation.text = f"temp.{ step_name }"

    '''
    <serviceOutput>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/Object_Name">Object Name</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/Run_Id">Run Id</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/Log_Id">Log Id</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/Task_Id">Task Id</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/Task_Status">Task Status</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/Success_Source_Rows">Success Source Rows</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/Failed_Source_Rows">Failed Source Rows</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/Success_Target_Rows">Success Target Rows</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/Failed_Target_Rows">Failed Target Rows</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/Start_Time">Start Time</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/End_Time">End Time</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/Error_Message">Error Message</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/TotalTransErrors">Total Transformation Errors</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/FirstErrorCode">First Error Code</operation>
    </serviceOutput>
    '''

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceOutput" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceOutput = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service, "serviceOutput")

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation1 = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceOutput, "operation", attrib={
        "source": "field",
        "to": f"temp.{ step_name }/output/Object_Name"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation1.text = "Object Name"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation2 = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceOutput, "operation", attrib={
        "source": "field",
        "to": f"temp.{ step_name }/output/Run_Id"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation2.text = "Run Id"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation3 = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceOutput, "operation", attrib={
        "source": "field",
        "to": f"temp.{ step_name }/output/Log_Id"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation3.text = "Log Id"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation4 = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceOutput, "operation", attrib={
        "source": "field",
        "to": f"temp.{ step_name }/output/Task_Id"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation4.text = "Task Id"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation5 = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceOutput, "operation", attrib={
        "source": "field",
        "to": f"temp.{ step_name }/output/Task_Status"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation5.text = "Task Status"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation6 = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceOutput, "operation", attrib={
        "source": "field",
        "to": f"temp.{ step_name }/output/Success_Source_Rows"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation6.text = "Success Source Rows"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation7 = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceOutput, "operation", attrib={
        "source": "field",
        "to": f"temp.{ step_name }/output/Failed_Source_Rows"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation7.text = "Failed Source Rows"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation8 = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceOutput, "operation", attrib={
        "source": "field",
        "to": f"temp.{ step_name }/output/Success_Target_Rows"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation8.text = "Success Target Rows"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation9 = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceOutput, "operation", attrib={
        "source": "field",
        "to": f"temp.{ step_name }/output/Failed_Target_Rows"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation9.text = "Failed Target Rows"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation10 = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceOutput, "operation", attrib={
        "source": "field",
        "to": f"temp.{ step_name }/output/Start_Time"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation10.text = "Start Time"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation11 = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceOutput, "operation", attrib={
        "source": "field",
        "to": f"temp.{ step_name }/output/End_Time"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation11.text = "End Time"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation12 = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceOutput, "operation", attrib={
        "source": "field",
        "to": f"temp.{ step_name }/output/Error_Message"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation12.text = "Error Message"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation13 = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceOutput, "operation", attrib={
        "source": "field",
        "to": f"temp.{ step_name }/output/TotalTransErrors"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation13.text = "Total Transformation Errors"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation14 = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceOutput, "operation", attrib={
        "source": "field",
        "to": f"temp.{ step_name }/output/FirstErrorCode"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation14.text = "First Error Code"

    '''
    <link id="mcoczikn" targetId="c"/>
    <events>
        <catch faultField="temp.SDE_ORA_EmployeeDailySnapshotFact_2/fault"
            id="mcoczil7"
            interrupting="true"
            name="error">
        <suspend/>
        </catch>
        <catch faultField="temp.SDE_ORA_EmployeeDailySnapshotFact_2/fault"
            id="mcoczil8"
            interrupting="true"
            name="warning"/>
    </events>
    '''

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/link" element
    if create_link:
        targetId = next_id
        getResponse_Item_Entry_taskflow_flow_eventContainer_link = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer, "link", attrib={
            #"id": str(uuid.uuid4()).replace('-',''),
            "id": "link" + shortuuid.uuid()[:8],
            "targetId": targetId if targetId is not None else 'end'
        })

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/events" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_events = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer, "events")

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/events/catch" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_events_catch1 = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_events, "catch", attrib={
        "faultField": f"temp.{ step_name }/fault",
        #"id": str(uuid.uuid4()).replace('-',''),
        "id": "catch" + shortuuid.uuid()[:8],
        "interrupting": "true",
        "name": "error"
    })

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/events/catch/suspend" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_events_catch1_suspend = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_events_catch1, "suspend")

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/events/catch" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_events_catch2 = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_events, "catch", attrib={
        "faultField": f"temp.{ step_name }/fault",
        #"id": str(uuid.uuid4()).replace('-',''),
        "id": "catch" + shortuuid.uuid()[:8],
        "interrupting": "true",
        "name": "warning"
    })




def add_cmd(parent, step_id, step_name, next_id, runtime_id, runtime_guid, runtime_name, create_link):
    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer" element
    getResponse_Item_Entry_taskflow_flow_eventContainer = etree.SubElement(parent, "eventContainer", attrib={
        "id": step_id
    })

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer, "service", attrib={
        #"id": str(uuid.uuid4()).replace('-','')
        "id": "svc" + shortuuid.uuid()[:8]
    })

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/title" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_title = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service, "title")
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_title.text = step_name

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceName" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceName = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service, "serviceName")
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceName.text = "ICSExecuteCommandTask"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceGUID" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceGUID = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service, "serviceGUID")

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service, "serviceInput")

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput, "parameter", attrib={
        "name": "Task Name",
        "source": "constant"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param.text = step_name
    
    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput, "parameter", attrib={
        "name": "Wait for Task to Complete",
        "source": "constant"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param.text = "true"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput, "parameter", attrib={
        "name": "Runtime Environment",
        "source": "constant"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param.text = f"{ runtime_id }:{ runtime_name }"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput, "parameter", attrib={
        "name": "Max Wait",
        "source": "constant"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param.text = "86400"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput, "parameter", attrib={
        "name": "Script Name",
        "source": "constant"
    })

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput, "parameter", attrib={
        "name": "Input Arguments",
        "source": "constant"
    })

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput, "parameter", attrib={
        "name": "Work Directory",
        "source": "constant"
    })

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput, "parameter", attrib={
        "name": "RuntimeEnvGUID",
        "source": "constant"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param.text = runtime_guid

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput, "parameter", attrib={
        "name": "FailTaskIfAnyScriptFails",
        "source": "constant"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param.text = "false"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput, "parameter", attrib={
        "name": "taskField",
        "source": "nested"
    })

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param_operation = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param, "operation", attrib={
        "source": "field",
        "to": "INFA-commandTask"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param_operation.text = f"temp.{ step_name }"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param_operation = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param, "operation", attrib={
        "source": "constant",
        "to": "INFA-commandTask/input[1]/script-1/name"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param_operation.text = "Script1"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param_operation = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param, "operation", attrib={
        "source": "constant",
        "to": "INFA-commandTask/input[1]/script-1/scriptName"
    })
    #TODO update script path to sqlplus script
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param_operation.text = "C:\Informatica\scripts\HelloWorld.bat"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param_operation = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param, "operation", attrib={
        "source": "constant",
        "to": "INFA-commandTask/input[1]/script-1/inputArguments"
    })
    #TODO update script args
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param_operation.text = '"Jon"'

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param_operation = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param, "operation", attrib={
        "source": "constant",
        "to": "INFA-commandTask/input[1]/script-1/workDir"
    })
    #TODO update script work dir
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_param_operation.text = 'C:\Informatica\scripts'

    '''
    <serviceOutput>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/Object_Name">Object Name</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/Run_Id">Run Id</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/Log_Id">Log Id</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/Task_Id">Task Id</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/Task_Status">Task Status</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/Success_Source_Rows">Success Source Rows</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/Failed_Source_Rows">Failed Source Rows</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/Success_Target_Rows">Success Target Rows</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/Failed_Target_Rows">Failed Target Rows</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/Start_Time">Start Time</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/End_Time">End Time</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/Error_Message">Error Message</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/TotalTransErrors">Total Transformation Errors</operation>
        <operation source="field"
                    to="temp.SDE_ORA_EmployeeDailySnapshotFact_2/output/FirstErrorCode">First Error Code</operation>
    </serviceOutput>
    '''

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceOutput" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceOutput = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service, "serviceOutput")

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceOutput, "operation", attrib={
        "source": "field",
        "to": f"temp.{ step_name }/output/Run_Id"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation.text = "Run Id"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceOutput, "operation", attrib={
        "source": "field",
        "to": f"temp.{ step_name }/output/Start_Time"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation.text = "Start Time"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceOutput, "operation", attrib={
        "source": "field",
        "to": f"temp.{ step_name }/output/End_Time"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation.text = "End Time"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceOutput, "operation", attrib={
        "source": "field",
        "to": f"temp.{ step_name }/output/Exit_Code"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation.text = "Exit Code"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceOutput, "operation", attrib={
        "source": "field",
        "to": f"temp.{ step_name }/output/Execution_Status"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation.text = "Execution Status"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/service/serviceInput/parameter/operation" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceOutput, "operation", attrib={
        "source": "field",
        "to": f"temp.{ step_name }/output/Std_Error"
    })
    getResponse_Item_Entry_taskflow_flow_eventContainer_service_serviceInput_operation.text = "Std Error"


    '''
    <link id="mcoczikn" targetId="c"/>
    <events>
        <catch faultField="temp.SDE_ORA_EmployeeDailySnapshotFact_2/fault"
            id="mcoczil7"
            interrupting="true"
            name="error">
        <suspend/>
        </catch>
        <catch faultField="temp.SDE_ORA_EmployeeDailySnapshotFact_2/fault"
            id="mcoczil8"
            interrupting="true"
            name="warning"/>
    </events>
    '''

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/link" element
    if create_link:
        targetId = next_id
        getResponse_Item_Entry_taskflow_flow_eventContainer_link = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer, "link", attrib={
            "id": "link" + shortuuid.uuid()[:8],
            "targetId": targetId if targetId is not None else 'end'
        })

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/events" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_events = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer, "events")

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/events/catch" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_events_catch1 = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_events, "catch", attrib={
        "faultField": f"temp.{ step_name }/fault",
        "id": "catch" + shortuuid.uuid()[:8],
        "interrupting": "true",
        "name": "error"
    })

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/eventContainer/events/catch/suspend" element
    getResponse_Item_Entry_taskflow_flow_eventContainer_events_catch1_suspend = etree.SubElement(getResponse_Item_Entry_taskflow_flow_eventContainer_events_catch1, "suspend")

def generate_taskflow(taskflowID, taskflowName, dfPlan):

    # Initialise the log file
    logging.basicConfig(
        filename='logs/console.log',
        level=logging.DEBUG,
        format='%(asctime)s:%(levelname)s:%(message)s',
    )

    logging.info('Starting to generate the Taskflow XML files')

    # Get the unique list of step orders
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

    # Create the "/aetgt:getResponse/types1:Item/types1:ModificationDate" element
    #namespace_url = 'http://schemas.active-endpoints.com/appmodules/repository/2010/10/avrepository.xsd'
    #namespace = "{%s}" % namespace_url
    #getResponse_Item_ModificationDate = etree.SubElement(getResponse_Item, namespace + "ModificationDate", nsmap={'types1': namespace_url})

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
        "name": taskflowName,
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
    for idx, row in dfPlan.iterrows():

        step_id = row['dac2idmc_step_id']
        step_name = row['step_name']
        step_type = row['plan_step_type']
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
        if step_type == 'REGULAR':
            getResponse_Item_Entry_taskflow_tempFields_options_option3.text = f"$po:{ re.sub(r'[^A-Za-z0-9]', '-', step_name) }-{ infa_id }"
        elif step_type == 'CREATE_QUERY_INDEXES':
            getResponse_Item_Entry_taskflow_tempFields_options_option3.text = "$po:INFA-commandTask"


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
    #getResponse_Item_Entry_taskflow_extData = etree.SubElement(getResponse_Item_Entry_taskflow, "extData")

    ######################################################################################
    # ## /aetgt:getResponse/types1:Item/types1:Entry/taskflow/extData
    ######################################################################################


    #logging.info('Building "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/extData" elements...')

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/extData/nvpair" element
    #getResponse_Item_Entry_taskflow_extData_nvpair1 = etree.SubElement(getResponse_Item_Entry_taskflow_extData, "nvpair", attrib={
    #    "name": "treatEmptyStringAsNotNull"
    #})
    #getResponse_Item_Entry_taskflow_extData_nvpair1.text = "false"

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/extData/nvpair" element
    #getResponse_Item_Entry_taskflow_extData_nvpair2 = etree.SubElement(getResponse_Item_Entry_taskflow_extData, "nvpair", attrib={
    #    "name": "treatEmptyObjectListAsArray"
    #})
    #getResponse_Item_Entry_taskflow_extData_nvpair2.text = "false"

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
    #TODO Add link handling when the first step is a parallel path
    first_seq = dfPlan.iloc[0]['plan_step_order']
    dfSteps = dfPlan[dfPlan['plan_step_order'] == first_seq]
    isParallel = True if len(dfSteps.index) > 1 else False
    targetId = dfPlan.iloc[0]['dac2idmc_group_id'] if isParallel else dfPlan.iloc[0]['dac2idmc_step_id']
    getResponse_Item_Entry_taskflow_flow_end = etree.SubElement(getResponse_Item_Entry_taskflow_flow_start, "link", attrib={
        "id": "link" + shortuuid.uuid()[:8],
        "targetId": targetId if targetId is not None else 'end'
    })

    ######################################################################################
    # ## /aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow
    ######################################################################################

    '''
    <flow id="a">
        <start id="b">
            <link id="mcoczikm" targetId="mcoczil9"/>
        </start>
        <eventContainer id="mcoczil9">
            <service id="mcoczikl">
                ...
            </service>
            <link id="mcoczikn" targetId="c"/>
            <events>
                <catch faultField="temp.SDE_ORA_EmployeeDailySnapshotFact_2/fault"
                    id="mcoczil7"
                    interrupting="true"
                    name="error">
                <suspend/>
                </catch>
                <catch faultField="temp.SDE_ORA_EmployeeDailySnapshotFact_2/fault"
                    id="mcoczil8"
                    interrupting="true"
                    name="warning"/>
            </events>
        </eventContainer>
        <end id="c"/>
    </flow>
    '''

    logging.info('Building "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow" elements...')

    # Loop through the steps and add them to the flow
    #TODO add handling for parallel paths
    for seq in order_list:
        dfSteps = dfPlan[dfPlan['plan_step_order'] == seq]
        isParallel = True if len(dfSteps.index) > 1 else False

        # Add a parallel paths step if more than one step in the same group
        if isParallel:
            groupId = dfSteps.iloc[0]['dac2idmc_group_id']
            next_id = dfSteps.iloc[-1]['dac2idmc_next_id']
            next_group = dfSteps.iloc[0]['dac2idmc_next_group']
            next_count = len(dfPlan[dfPlan['dac2idmc_group_id'] == next_group].index)
            link_id = next_group if next_count > 1 and next_group is not None else next_id if next_id is not None else 'end'
            
            # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/container" element
            getResponse_Item_Entry_taskflow_flow_container = etree.SubElement(getResponse_Item_Entry_taskflow_flow, "container", attrib={
                "id": groupId,
                "type": "parallel"
            })

            # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/container/title" element
            getResponse_Item_Entry_taskflow_flow_container_title = etree.SubElement(getResponse_Item_Entry_taskflow_flow_container, "title")
            getResponse_Item_Entry_taskflow_flow_container_title.text = f"Parallel Paths { groupId }"

            # Add the task containers
            for idx, row in dfSteps.iterrows():
                infa_id = row['infa_id']
                step_name = row['step_name']
                step_id = row['dac2idmc_step_id']
                step_type = row['plan_step_type']
                runtime_id = row['agent_id']
                runtime_guid = row['agent_guid']
                runtime_name = row['agent_name']

                # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/container/flow" element
                getResponse_Item_Entry_taskflow_flow_container_flow = etree.SubElement(getResponse_Item_Entry_taskflow_flow_container, "flow", attrib={
                    "id": "flow" + step_id
                })

                if step_type == 'REGULAR':
                # Add the task
                    add_task(getResponse_Item_Entry_taskflow_flow_container_flow, infa_id, step_id, step_name, groupId, False)
                elif step_type == 'CREATE_QUERY_INDEXES':
                    add_cmd(getResponse_Item_Entry_taskflow_flow_container_flow, step_id, step_name, next_id, runtime_id, runtime_guid, runtime_name, False)

                # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/container/flow/link" element
                getResponse_Item_Entry_taskflow_flow_container_flow_link = etree.SubElement(getResponse_Item_Entry_taskflow_flow_container_flow, "link", attrib={
                    "id": "link" + shortuuid.uuid()[:8],
                    "targetId": groupId,
                    "type": "containerLink"
                })

            # Add the container links
            for idx, row in dfSteps.iterrows():
                infa_id = row['infa_id']
                step_name = row['step_name']
                step_id = row['dac2idmc_step_id']
                next_id = row['dac2idmc_next_id']

                # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/container/link" element
                getResponse_Item_Entry_taskflow_flow_container_flow_link = etree.SubElement(getResponse_Item_Entry_taskflow_flow_container, "link", attrib={
                    "id": "link" + shortuuid.uuid()[:8],
                    "targetId": "flow" + step_id,
                    "type": "containerLink"
                })

            # Create the final connecting "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/container/link" element
            getResponse_Item_Entry_taskflow_flow_container_flow_link = etree.SubElement(getResponse_Item_Entry_taskflow_flow_container, "link", attrib={
                "id": "link" + shortuuid.uuid()[:8],
                "targetId": link_id
            })


        # Add the single tasks
        else:
            for idx, row in dfSteps.iterrows():
                infa_id = row['infa_id']
                step_name = row['step_name']
                step_id = row['dac2idmc_step_id']
                next_id = row['dac2idmc_next_id']
                next_group = row['dac2idmc_next_group']
                next_count = len(dfPlan[dfPlan['dac2idmc_group_id'] == next_group].index)
                link_id = next_group if next_count > 1 and next_group is not None else next_id if next_id is not None else 'end'
                step_type = row['plan_step_type']
                runtime_id = row['agent_id']
                runtime_guid = row['agent_guid']
                runtime_name = row['agent_name']
        
                if step_type == 'REGULAR':
                    add_task(getResponse_Item_Entry_taskflow_flow, infa_id, step_id, step_name, link_id, True)
                elif step_type == 'CREATE_QUERY_INDEXES':
                    add_cmd(getResponse_Item_Entry_taskflow_flow, step_id, step_name, next_id, runtime_id, runtime_guid, runtime_name, True)

    # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/flow/end" element
    getResponse_Item_Entry_taskflow_flow_end = etree.SubElement(getResponse_Item_Entry_taskflow_flow, "end", attrib={
        "id": "end"
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
    for idx, row in dfPlan.iterrows():

        step_name = row['step_name']
        step_type = row['plan_step_type']
        infa_id = row['infa_id']

        if step_type == 'REGULAR':
        
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
        
        elif step_type == 'CREATE_QUERY_INDEXES':
            
            # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/dependencies/processObject" element
            getResponse_Item_Entry_taskflow_dependencies_processObject = etree.SubElement(getResponse_Item_Entry_taskflow_dependencies, "processObject", attrib={
                "xmlns": "http://schemas.active-endpoints.com/appmodules/screenflow/2011/06/avosHostEnvironment.xsd",
                "displayName": "INFA-commandTask",
                "isByCopy": "true",
                "name": "INFA-commandTask"
            })

            # Create the "/aetgt:getResponse/types1:Item/types1:Entry/taskflow/dependencies/processObject/description" element
            getResponse_Item_Entry_taskflow_dependencies_processObject_description = etree.SubElement(getResponse_Item_Entry_taskflow_dependencies_processObject, "description")
            getResponse_Item_Entry_taskflow_dependencies_processObject_description.text = "This process object represents a taskflow specific command task output field details."

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


