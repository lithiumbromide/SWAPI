---
title: "Get and Set Sensor Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Sensor_Example_VBNET.htm"
---

# Get and Set Sensor Example (VB.NET)

This example shows how to get a Measurement (dimension) sensor, resets its value to set off an alert, and fire notification before resetting the value.

```vb
'-------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part document that has a dimension
 '    of 2.5 inches and a corresponding Measurement
 '    (dimension) sensor that has an alert set to
 '    go off if the value of the dimension is
 '    reset to > 3 inches.
 ' 2. Select the Measurement (dimension) sensor
 '    of 2.5 inches in the Sensors folder in the
 '    FeatureManager design tree.
 ' 3. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Enables the Measurement (dimension) sensor alert, if it
 '    wasn't previously enabled.
 ' 2. Sets the value of the dimension to 3.5 inches.
 ' 3. Triggers the Measurement (dimension) sensor alert; click
 '    OK to close it.
 ' 4. Fires an event when updating the dimension; click
 '    OK to close it.
 ' 5. Examine the FeatureManager design tree, Immediate window,
 '    and the graphics area.
 '--------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
Imports System.Collections

Partial Class SolidWorksMacro

    Public WithEvents swPart As PartDoc

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swSelMgr As SelectionMgr
        Dim swFeat As Feature
        Dim swSensor As Sensor
        Dim swDimSensor As DimensionSensorData
        Dim swDisplayDim As DisplayDimension
        Dim swDim As Dimension
        Dim alertValue1 As Double
        Dim alertvalue2 As Double
        Dim sensorValue As Double
        Dim retVal As Integer
        Dim bool As Boolean
        Dim openPart As Hashtable

        swModel = swApp.ActiveDoc
        swSelMgr = swModel.SelectionManager

        ' Set up event handler
        swPart = swModel
        openPart = New Hashtable
        AttachEventHandlers()

        ' Get the selected Measurement (dimension) sensor
        ' in Sensors folder in FeatureManager design tree
        swFeat = swSelMgr.GetSelectedObject6(1, -1)
        swSensor = swFeat.GetSpecificFeature2
        ' Get name of sensor
        Debug.Print("Sensor name = " & swFeat.Name)

        ' Make sure selected sensor is a Measurement
        ' (dimension) sensor (as of SOLIDWORKS 2009 SP2, only Measurement
        ' (dimension) sensors are supported); if it's not, then exit
        ' the macro
        If swSensor Is Nothing Then
            Debug.Print("Selected sensor is not a Measurement (dimension) sensor. Exiting macro.")
            Exit Sub
        End If

        ' Get type of sensor
        Select Case swSensor.SensorType
            Case swSensorType_e.swSensorSimulation
                Debug.Print("Sensor type = Simulation")
            Case swSensorType_e.swSensorMassProperty
                Debug.Print("Sensor type = Mass Property")
            Case swSensorType_e.swSensorDimension
                Debug.Print("Sensor type = Measurement (dimension)")
            Case swSensorType_e.swSensorInterfaceDetection
                Debug.Print("Sensor type = Interference Detection")
        End Select

' Get whether the sensor is in an alerted state
Debug.Print ("Is an alert currently triggered for this sensor? " & swSensor.SensorAlertState)

' Enable sensor's alert
Debug.Print ("Is an alert enabled for this sensor? " & swSensor.SensorAlertEnabled)

        ' Get sensor's alert state
        If swSensor.SensorAlertState Then
            Select Case swSensor.SensorAlertType
                Case swSensorAlertType_e.swSensorAlert_GreaterThan
                    Debug.Print("Sensor alert type = Greater than")
                Case swSensorAlertType_e.swSensorAlert_LessThan
                    Debug.Print("Sensor alert type = Less than")
                Case swSensorAlertType_e.swSensorAlert_Exactly
                    Debug.Print("Sensor alert type = Exactly")
                Case swSensorAlertType_e.swSensorAlert_NotGreaterThan
                    Debug.Print("Sensor alert type = Not greater than")
                Case swSensorAlertType_e.swSensorAlert_NotLessThan
                    Debug.Print("Sensor alert type = Not less than")
                Case swSensorAlertType_e.swSensorAlert_NotExactly
                    Debug.Print("Sensor alert type = Not exactly")
                Case swSensorAlertType_e.swSensorAlert_Between
                    Debug.Print("Sensor alert type = Between")
                Case swSensorAlertType_e.swSensorAlert_NotBetween
                    Debug.Print("Sensor alert type = Not between")
                Case swSensorAlertType_e.swSensorAlert_True
                    Debug.Print("Sensor alert type = True")
                Case swSensorAlertType_e.swSensorAlert_False
                    Debug.Print("Sensor alert type = False")
            End Select

            ' Get sensor's alert values
            alertValue1 = swSensor.SensorAlertValue1
            ' ISensor::SensorAlertValue2 only valid when sensor
            ' alert type is swSensorAlertType_e.swSensorAlert_Between
            alertvalue2 = swSensor.SensorAlertValue2
            Debug.Print("  Alert value 1 = " & alertValue1)
            Debug.Print("  Alert value 2 = " & alertvalue2)
        End If

        ' Set sensor to a different sensor type
        swSensor.SensorType = swSensorType_e.swSensorSimulation
        Select Case swSensor.SensorType
            Case swSensorType_e.swSensorSimulation
                Debug.Print("Set sensor type to = Simulation")
            Case swSensorType_e.swSensorMassProperty
                Debug.Print("Set sensor type to = Mass Property")
            Case swSensorType_e.swSensorDimension
                Debug.Print("Set sensor type to = Measurement (dimension)")
            Case swSensorType_e.swSensorInterfaceDetection
                Debug.Print("Set sensor type to = Interference Detection")
        End Select

        ' Update and evaluate sensor
        bool = swSensor.UpdateSensor()

        ' Print updated sensor type
        Select Case swSensor.SensorType
            Case swSensorType_e.swSensorSimulation
                Debug.Print("Sensor updated to type = Simulation")
            Case swSensorType_e.swSensorMassProperty
                Debug.Print("Sensor updated to type = Mass Property")
            Case swSensorType_e.swSensorDimension
                Debug.Print("Sensor updated to type = Measurement (dimension)")
            Case swSensorType_e.swSensorInterfaceDetection
                Debug.Print("Sensor updated to type = Interference Detection")
        End Select

        ' Set sensor type back to original type
        swSensor.SensorType = swSensorType_e.swSensorDimension

        ' Update and evaluate sensor again
        bool = swSensor.UpdateSensor()
        ' Print updated sensor type
        Select Case swSensor.SensorType
            Case swSensorType_e.swSensorSimulation
                Debug.Print("Sensor updated back to type = Simulation")
            Case swSensorType_e.swSensorMassProperty
                Debug.Print("Sensor updated back to type = Mass Property")
            Case swSensorType_e.swSensorDimension
                Debug.Print("Sensor updated back to type = Measurement (dimension)")
            Case swSensorType_e.swSensorInterfaceDetection
                Debug.Print("Sensor updated back to type = Interference Detection")
        End Select

        ' Because sensor is a Measurement (dimension) sensor,
        ' get the sensor's feature data, object, configuration name, and value
        If TypeOf swSensor Is DimensionSensorData Then
            swDimSensor = swSensor.GetSensorFeatureData
            ' Get Measurement (dimension) sensor value
            sensorValue = swDimSensor.SensorValue
            'Convert meters to inches
            Debug.Print("Sensor value: " + Str(sensorValue * 39.37) + " inches")
            ' Get the actual dimension and update
            ' to a value that sets off the alert
            swDisplayDim = swDimSensor.GetDisplayDimension()
            swDim = swDisplayDim.GetDimension2(1)
            retVal = swDim.SetValue3(3.5, swSetValueInConfiguration_e.swSetValue_UseCurrentSetting, "Configuration")
            bool = swSensor.UpdateSensor()
            swModel.ForceRebuild3(True)
            ' Get Measurement (dimension) sensor value again
            sensorValue = swDimSensor.SensorValue
            Debug.Print("New sensor value: " + Str(sensorValue * 39.37) + " inches")
        End If
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

    Sub AttachEventHandlers()
        AttachSWEvents()
    End Sub

    Sub AttachSWEvents()
        AddHandler swPart.SensorAlertPreNotify, AddressOf Me.swPart_SensorAlertPreNotify
    End Sub

    Function swPart_SensorAlertPreNotify(ByVal SensorIn As Object, ByVal SensorAlertType As Integer) As Integer
        MsgBox("The value of the sensor deviates from its limits.")
    End Function

End Class
```
