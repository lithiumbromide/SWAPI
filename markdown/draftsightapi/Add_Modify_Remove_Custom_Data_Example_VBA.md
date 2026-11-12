---
title: "Add, Modify, and Remove Custom Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Add_Modify_Remove_Custom_Data_Example_VBA.htm"
---

# Add, Modify, and Remove Custom Data Example (VBA)

This example shows how to add, modify, and remove custom data from a Circle.

```
'--------------------------------------------------------------
'Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
'    install_dir\bin\dsAutomation.dll.
' 4. Open the Immediate window.
' 5. Start DraftSight and open a document.
' 6. Run the macro.
'
'Postconditions:
' 1. Circle is constructed.
' 2. Custom data is added to, modified, and removed from
'    the Circle.
' 3. Examine the Immediate window to verify.
'----------------------------------------------------------------
```

```
Option Explicit
```

```
    Sub main()
```

```
        Dim dsApp As DraftSight.Application
```

```
        'Connect to DraftSight application
        Set dsApp = GetObject(, "DraftSight.Application")
        'Abort any command currently running in DraftSight
        'to avoid nested commands
	dsApp.AbortRunningCommand
```

```
        'Get active document
        Dim dsDoc As DraftSight.Document
        Set dsDoc = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MsgBox ("There are no open documents in DraftSight.")
            Return
        End If
```

```
        'Get model space
        Dim dsModel As DraftSight.Model
        Set dsModel = dsDoc.GetModel()
```

```
        'Get sketch manager
        Dim dsSketchMgr As DraftSight.SketchManager
        Set dsSketchMgr = dsModel.GetSketchManager()
```

```
        'Draw a Circle
        Dim centerX As Double
        centerX = 1
        Dim centerY As Double
        centerY = 1
        Dim centerZ As Double
        centerZ = 0
        Dim radius As Double
        radius = 5
        Dim dsCircle As DraftSight.Circle
        Set dsCircle = dsSketchMgr.InsertCircle(centerX, centerY, centerZ, radius)
```

```
        'Zoom to fit
        dsApp.Zoom dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing
```

```
        'Add custom data to the Circle
        Dim applicationName As String
        applicationName = "CircleApp"
        AddCustomDataToCircle dsCircle, applicationName
```

```
        Debug.Print ("Circle custom data...")
        Debug.Print ("")
```

```
        'Print custom data
        PrintCustomDataInfo dsCircle.GetCustomData(applicationName)
```

```
        'Change custom data
        Dim dsCustomData As DraftSight.CustomData
        Set dsCustomData = dsCircle.GetCustomData(applicationName)
        ChangeCustomData dsCustomData
```

```
        'Apply the changed custom data to the Circle
        dsCircle.SetCustomData applicationName, dsCustomData
```

```
        Debug.Print ("")
        Debug.Print ("Custom data changed...")
        Debug.Print ("")
```

```
        'Print custom data after changing it
        PrintCustomDataInfo dsCircle.GetCustomData(applicationName)
```

```
        'Remove all string values from custom data
        Set dsCustomData = dsCircle.GetCustomData(applicationName)
        DeleteStringDataFromCustomData dsCustomData, dsCustomDataType_e.dsCustomDataType_String
```

```
        'Apply the changed custom data to the Circle
        dsCircle.SetCustomData applicationName, dsCustomData
```

```
        Debug.Print ("")
        Debug.Print ("Removed all string values from custom data...")
        Debug.Print ("")
```

```
        'Print custom data after removing elements
        PrintCustomDataInfo dsCircle.GetCustomData(applicationName)
```

```
        'Delete custom data from the Circle
        dsCircle.DeleteCustomData applicationName
```

```
        Debug.Print ("")
        Debug.Print ("The custom data for the circle is removed...")
        Debug.Print ("")
```

```
        'Print custom data after removing it from the Circle
        PrintCustomDataInfo dsCircle.GetCustomData(applicationName)
```

```
    End Sub
```

```
    Sub AddCustomDataToCircle(ByVal dsCircle As DraftSight.Circle, ByVal applicationName As String)
        'Get custom data for the Circle
        Dim dsCustomData As DraftSight.CustomData
        Set dsCustomData = dsCircle.GetCustomData(applicationName)
```

```
        'Clear existing custom data
        dsCustomData.Empty
```

```
        'Get the index
        Dim index As Long
        index = dsCustomData.GetDataCount()
```

```
        'Add a description of the Circle as a string value to the custom data
        Dim markerForString As Long
        markerForString = 1000
        dsCustomData.InsertStringData index, markerForString, "Circle entity"
```

```
        'Get the next index
        index = dsCustomData.GetDataCount()
```

```
        'Add custom data section to custom data
        Dim dsInnerCustomData As DraftSight.CustomData
        Set dsInnerCustomData = dsCustomData.InsertCustomData(index)
```

```
        'Get the next index
        index = dsInnerCustomData.GetDataCount()
```

```
        'Get the center point of the Circle
        'and add it as point data to the custom data
        Dim markerForPoint As Long
        markerForPoint = 1011
        Dim centerX As Double, centerY As Double, centerZ As Double
        dsCircle.GetCenter centerX, centerY, centerZ
        dsInnerCustomData.InsertPointData index, markerForPoint, centerX, centerY, centerZ
```

```
        'Get the next index
        index = dsInnerCustomData.GetDataCount()
```

```
        'Get the radius of the Circle
        'and add it as double data to the custom data
        Dim markerForDouble As Long
        markerForDouble = 1040
        Dim doubleValue As Double
        doubleValue = dsCircle.radius
        dsInnerCustomData.InsertDoubleData index, markerForDouble, doubleValue
```

```
        'Get the next index
        index = dsInnerCustomData.GetDataCount()
```

```
        'Add the layer name of Circle as layer name data
        'to custom data
        dsInnerCustomData.InsertLayerName index, dsCircle.Layer
```

```
        'Get the next index
        index = dsInnerCustomData.GetDataCount()
```

```
        'Add the name of the LineStyle of the Circle
        'as a string data to custom data
        dsInnerCustomData.InsertStringData index, markerForString, dsCircle.LineStyle
```

```
        'Get the next index
        index = dsInnerCustomData.GetDataCount()
```

```
        'Add Int16 data to custom data
        Dim markerForInt16 As Integer
        markerForInt16 = 1070
        Dim intValue As Long
        intValue = 5
        dsInnerCustomData.InsertInteger16Data index, markerForInt16, intValue
```

```
        'Get the next index
        index = dsInnerCustomData.GetDataCount()
```

```
        'Add Int32 data to custom data
        Dim markerForInt32 As Integer
        markerForInt32 = 1071
        Dim int32Value As Long
        int32Value = 7
        dsInnerCustomData.InsertInteger32Data index, markerForInt32, int32Value
```

```
        'Get the next index
        index = dsInnerCustomData.GetDataCount()
```

```
        'Add the handle of the Circle as handle data to custom data
        dsInnerCustomData.InsertHandle index, dsCircle.handle
```

```
        'Get the next index
        index = dsInnerCustomData.GetDataCount()
```

```
        'Add binary data to custom data
        Dim binaryDataArray(3) As Byte
        binaryDataArray(0) = 0
        binaryDataArray(1) = 1
        binaryDataArray(2) = 0
        binaryDataArray(3) = 1
        dsInnerCustomData.InsertByteData index, binaryDataArray
```

```
        'Set custom data
        dsCircle.SetCustomData applicationName, dsCustomData
    End Sub
```

```
    Sub DeleteStringDataFromCustomData(ByVal dsCustomData As DraftSight.CustomData, ByVal dataType As dsCustomDataType_e)
        'Get custom data count
        Dim count As Long
        count = dsCustomData.GetDataCount()
```

```
        Dim index As Long
        For index = count - 1 To 0 Step -1
            'Get custom data type
            Dim customDataType As dsCustomDataType_e
            dsCustomData.GetDataType index, customDataType
```

```
            If customDataType = dataType Then
                'Delete custom data element
                dsCustomData.Delete (index)
            End If
```

```
            If customDataType = dsCustomDataType_e.dsCustomDataType_CustomData Then
                'Get inner custom data
                Dim dsInnerCustomData As DraftSight.CustomData
                Set dsInnerCustomData = Nothing
                dsCustomData.GetCustomData index, dsInnerCustomData
```

```
                DeleteStringDataFromCustomData dsInnerCustomData, dataType
            End If
        Next
    End Sub
```

```
    Sub ChangeCustomData(ByVal dsCustomData As CustomData)
        'Get custom data count
        Dim count As Long
        count = dsCustomData.GetDataCount()
```

```
        Dim index As Long
        For index = 0 To count - 1
            'Get custom data type
            Dim dataType As dsCustomDataType_e
            dsCustomData.GetDataType index, dataType
```

```
            Select Case dataType
                Case dsCustomDataType_e.dsCustomDataType_BinaryData
                    If True Then
                        'Get binary data from custom data
                        Dim binaryDataArray As Variant
                        binaryDataArray = dsCustomData.GetByteData(index)
```

```
                        'Check if binary data is not empty
                        Dim i As Long
                        If Not IsEmpty(binaryDataArray) Then
                            For i = LBound(binaryDataArray) To UBound(binaryDataArray)
                                binaryDataArray(i) = binaryDataArray(i) + 1
                            Next i
```

```
                            'Set the updated binary data to custom data
                            dsCustomData.SetByteData index, binaryDataArray
                        End If
```

```
                    End If
                Case dsCustomDataType_e.dsCustomDataType_CustomData
                    If True Then
                        'Get the inner custom data
                        Dim dsInnerCustomData As DraftSight.CustomData
                        Set dsInnerCustomData = Nothing
                        dsCustomData.GetCustomData index, dsInnerCustomData
```

```
                        ChangeCustomData dsInnerCustomData
```

```
                    End If
                Case dsCustomDataType_e.dsCustomDataType_Double
                    If True Then
                        'Get double custom data
                        Dim doubleValue As Double
                        dsCustomData.GetDoubleData index, doubleValue
```

```
                        'Change double value
                        doubleValue = doubleValue + 1
```

```
                        'Set the updated double value to custom data
                        dsCustomData.SetDoubleData index, doubleValue
```

```
                    End If
                Case dsCustomDataType_e.dsCustomDataType_Integer16
                    If True Then
                        'Get Int16 custom data
                        Dim intValue As Long
                        dsCustomData.GetInteger16Data index, intValue
```

```
                        'Change Int16 value
                        intValue = intValue + 1
```

```
                        'Set the updated Int16 value to custom data
                        dsCustomData.SetInteger16Data index, intValue
```

```
                    End If
                Case dsCustomDataType_e.dsCustomDataType_Integer32
                    If True Then
                        'Get Int32 custom data
                        dsCustomData.GetInteger32Data index, intValue
```

```
                        'Change Int32 value
                        intValue = intValue + 1
```

```
                        'Set the updated Int32 value to custom data
                        dsCustomData.SetInteger32Data index, intValue
```

```
                    End If
                Case dsCustomDataType_e.dsCustomDataType_Point
                    If True Then
                        'Get point custom data
                        Dim x As Double, y As Double, z As Double
                        dsCustomData.GetPointData index, x, y, z
```

```
                        'Change point coordinates
                        x = x + 2
                        y = y + 2
                        z = z + 2
```

```
                        'Set the updated point coordinates to custom data
                        dsCustomData.SetPointData index, x, y, z
```

```
                    End If
                Case dsCustomDataType_e.dsCustomDataType_String
                    If True Then
                        'Get string custom data
                        Dim stringValue As String
                        stringValue = ""
                        dsCustomData.GetStringData index, stringValue
```

```
                        'Modify string value
                        stringValue = stringValue + "_Changed"
```

```
                        'Set the updated string value to custom data
                        dsCustomData.SetStringData index, stringValue
```

```
                    End If
                Case Else
            End Select
        Next
    End Sub
```

```
    Sub PrintCustomDataInfo(ByVal dsCustomData As CustomData)
        'Get custom data count
        Dim count As Long
        count = dsCustomData.GetDataCount()
        Debug.Print ("Custom data count:" & count)
```

```
        Dim index As Long
        For index = 0 To count - 1
            'Get custom data type
            Dim dataType As dsCustomDataType_e
            dsCustomData.GetDataType index, dataType
```

```
            'Get custom data marker
            Dim marker As Long
            dsCustomData.GetDataMarker index, marker
```

```
            Select Case dataType
                Case dsCustomDataType_e.dsCustomDataType_BinaryData
                    If True Then
                        'Get binary data from custom data
                        Dim binaryArray As Variant
                        binaryArray = dsCustomData.GetByteData(index)
```

```
                        Dim binaryDataContent As String
                        binaryDataContent = ""
```

```
                        If IsEmpty(binaryArray) Then
                            binaryDataContent = "Empty"
                        Else
                            Dim j As Long
                            For j = LBound(binaryArray) To UBound(binaryArray)
                                binaryDataContent = binaryDataContent + CStr(binaryArray(j)) & ","
                            Next j
                        End If
```

```
                        'Print custom data index, data type, marker, and binary value
                        PrintCustomDataElement index, dataType, marker, binaryDataContent
```

```
                    End If
                Case dsCustomDataType_e.dsCustomDataType_CustomData
                    If True Then
                        'Get inner custom data
                        Dim dsGetCustomData As DraftSight.CustomData
                        Set dsGetCustomData = Nothing
                        dsCustomData.GetCustomData index, dsGetCustomData
```

```
                        PrintCustomDataInfo dsGetCustomData
```

```
                    End If
                Case dsCustomDataType_e.dsCustomDataType_Double
                    If True Then
                        'Get double value from custom data
                        Dim doubleValue As Double
                        dsCustomData.GetDoubleData index, doubleValue
```

```
                        'Print custom data index, data type, marker and double value
                        PrintCustomDataElement index, dataType, marker, doubleValue
```

```
                    End If
                Case dsCustomDataType_e.dsCustomDataType_Handle
                    If True Then
                        'Get handle value from custom data
                        Dim handle As String
                        handle = dsCustomData.GetHandleData(index)
```

```
                        'Print custom data index, data type, marker, and handle value
                        PrintCustomDataElement index, dataType, marker, handle
```

```
                    End If
                Case dsCustomDataType_e.dsCustomDataType_Integer16
                    If True Then
                        Dim int16Value As Long
                        dsCustomData.GetInteger16Data index, int16Value
```

```
                        'Print custom data index, data type, marker, and Int16 value
                        PrintCustomDataElement index, dataType, marker, int16Value
```

```
                    End If
                Case dsCustomDataType_e.dsCustomDataType_Integer32
                    If True Then
                        Dim int32Value As Long
                        dsCustomData.GetInteger32Data index, int32Value
```

```
                        'Print custom data index, data type, marker, and Int32 value
                        PrintCustomDataElement index, dataType, marker, int32Value
```

```
                    End If
                Case dsCustomDataType_e.dsCustomDataType_LayerName
                    If True Then
                        'Get layer name from custom data
                        Dim layerName As String
                        dsCustomData.GetLayerName index, layerName
```

```
                        'Print custom data index, data type, marker, and layer name value
                        PrintCustomDataElement index, dataType, marker, layerName
```

```
                    End If
                Case dsCustomDataType_e.dsCustomDataType_Point
                    If True Then
                        'Get point coordinates from custom data
                        Dim x As Double, y As Double, z As Double
                        dsCustomData.GetPointData index, x, y, z
```

```
                        'Print custom data index, data type, marker, and point values
                        Dim pointCoordinates As String
                        pointCoordinates = x & "," & y & "," & z
                        PrintCustomDataElement index, dataType, marker, pointCoordinates
```

```
                    End If
                Case dsCustomDataType_e.dsCustomDataType_String
                    If True Then
                        'Get string value from custom data
                        Dim stringValue As String
                        dsCustomData.GetStringData index, stringValue
```

```
                        'Print custom data index, data type, marker, and string value
                        PrintCustomDataElement index, dataType, marker, stringValue
```

```
                    End If
                Case dsCustomDataType_e.dsCustomDataType_Unknown
                    If True Then
                        'Print custom data index, data type, marker and value
                        PrintCustomDataElement index, dataType, marker, "Unknown value"
```

```
                    End If
                Case Else
            End Select
        Next
    End Sub
```

```
    Sub PrintCustomDataElement(ByVal index As Long, ByVal dataType As dsCustomDataType_e, ByVal marker As Integer, ByVal customDataValue As Variant)
        'Print custom data index, data type, marker, and value
        Dim message As String
        message = "Index: " & index
        message = message + " Data type: " & dataType
        message = message + " Marker: " & marker
        message = message + " Value: " & customDataValue
```

```
        Debug.Print (message)
    End Sub
```
