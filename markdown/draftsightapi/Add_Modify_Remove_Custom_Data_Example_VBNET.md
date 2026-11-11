---
title: "Add, Modify, and Remove Custom Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Add_Modify_Remove_Custom_Data_Example_VBNET.htm"
---

# Add, Modify, and Remove Custom Data Example (VB.NET)

This example shows how to add, modify, and remove custom data from a Circle.

```
'--------------------------------------------------------------
'Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll
' 4. Open the Immediate window.
' 5. Start DraftSight and open a document.
' 6. Click Start Debugging.
'
'Postconditions:
' 1. Circle is constructed.
' 2. Custom data is added to, modified, and removed from
'    the Circle.
' 3. Examine the Immediate window to verify.
'----------------------------------------------------------------
```

```
Imports DraftSight.Interop.dsAutomation
```

```
Module Module1
```

```
    Sub Main()
```

```
        Dim dsApp As Application
```

```
        'Connect to DraftSight application
        dsApp = GetObject(, "DraftSight.Application")
        dsApp.AbortRunningCommand() ' abort any command currently running in DraftSight to avoid nested commands
```

```
        'Get active document
        Dim dsDoc As Document = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MsgBox("There are no open documents in DraftSight.")
            Return
        End If
```

```
        'Get model space
        Dim dsModel As Model = dsDoc.GetModel()
```

```
        'Get sketch manager
        Dim dsSketchMgr As SketchManager = dsModel.GetSketchManager()
```

```
        'Draw a Circle
        Dim centerX As Double = 1, centerY As Double = 1, centerZ As Double = 0
        Dim radius As Double = 5
        Dim dsCircle As Circle = dsSketchMgr.InsertCircle(centerX, centerY, centerZ, radius)
```

```
        'Zoom to fit
        dsApp.Zoom(dsZoomRange_e.dsZoomRange_Fit, Nothing, Nothing)
```

```
        'Add custom data to the Circle
        Dim applicationName As String = "CircleApp"
        AddCustomDataToCircle(dsCircle, applicationName)
```

```
        Debug.Print(Environment.NewLine + "Circle custom data..." + Environment.NewLine)
```

```
        'Print custom data
        PrintCustomDataInfo(dsCircle.GetCustomData(applicationName))
```

```
        'Change custom data
        Dim dsCustomData As CustomData = dsCircle.GetCustomData(applicationName)
        ChangeCustomData(dsCustomData)
```

```
        'Apply the changed custom data to the Circle
        dsCircle.SetCustomData(applicationName, dsCustomData)
```

```
        Debug.Print(Environment.NewLine + "Custom data changed..." + Environment.NewLine)
```

```
        'Print custom data after changing it
        PrintCustomDataInfo(dsCircle.GetCustomData(applicationName))
```

```
        'Remove all string values from custom data
        dsCustomData = dsCircle.GetCustomData(applicationName)
        DeleteStringDataFromCustomData(dsCustomData, dsCustomDataType_e.dsCustomDataType_String)
```

```
        'Apply the changed custom data to the Circle
        dsCircle.SetCustomData(applicationName, dsCustomData)
```

```
        Debug.Print(Environment.NewLine + "Removed all string values from custom data..." + Environment.NewLine)
```

```
        'Print custom data after removing elements
        PrintCustomDataInfo(dsCircle.GetCustomData(applicationName))
```

```
        'Delete custom data from the Circle
        dsCircle.DeleteCustomData(applicationName)
```

```
        Debug.Print(Environment.NewLine + "The custom data for the circle is removed..." + Environment.NewLine)
```

```
        'Print custom data after removing it from the Circle
        PrintCustomDataInfo(dsCircle.GetCustomData(applicationName))
```

```
    End Sub
```

```
    Sub AddCustomDataToCircle(ByVal dsCircle As Circle, ByVal applicationName As String)
        'Get custom data for the Circle
        Dim dsCustomData As CustomData = dsCircle.GetCustomData(applicationName)
```

```
        'Clear existing custom data
        dsCustomData.Empty()
```

```
        'Get the index
        Dim index As Integer = dsCustomData.GetDataCount()
```

```
        'Add a description of the Circle as a string value to the custom data
        Dim markerForString As Integer = 1000
        dsCustomData.InsertStringData(index, markerForString, "Circle entity")
```

```
        'Get the next index
        index = dsCustomData.GetDataCount()
```

```
        'Add custom data section to custom data
        Dim dsInnerCustomData As CustomData = dsCustomData.InsertCustomData(index)
```

```
        'Get the next index
        index = dsInnerCustomData.GetDataCount()
```

```
        'Get the center point of the Circle
        'and add it as point data to the custom data
        Dim markerForPoint As Integer = 1011
        Dim centerX As Double, centerY As Double, centerZ As Double
        dsCircle.GetCenter(centerX, centerY, centerZ)
        dsInnerCustomData.InsertPointData(index, markerForPoint, centerX, centerY, centerZ)
```

```
        'Get the next index
        index = dsInnerCustomData.GetDataCount()
```

```
        'Get the radius of the Circle
        'and add it as double data to the custom data
        Dim markerForDouble As Integer = 1040
        Dim doubleValue As Double = dsCircle.Radius
        dsInnerCustomData.InsertDoubleData(index, markerForDouble, doubleValue)
```

```
        'Get the next index
        index = dsInnerCustomData.GetDataCount()
```

```
        'Add the layer name of Circle as layer name data
        'to custom data
        dsInnerCustomData.InsertLayerName(index, dsCircle.Layer)
```

```
        'Get the next index
        index = dsInnerCustomData.GetDataCount()
```

```
        'Add the name of the LineStyle of the Circle
        'as a string data to custom data
        dsInnerCustomData.InsertStringData(index, markerForString, dsCircle.LineStyle)
```

```
        'Get the next index
        index = dsInnerCustomData.GetDataCount()
```

```
        'Add Int16 data to custom data
        Dim markerForInt16 As Integer = 1070
        Dim intValue As Int16 = 5
        dsInnerCustomData.InsertInteger16Data(index, markerForInt16, intValue)
```

```
        'Get the next index
        index = dsInnerCustomData.GetDataCount()
```

```
        'Add Int32 data to custom data
        Dim markerForInt32 As Integer = 1071
        Dim int32Value As Int32 = 7
        dsInnerCustomData.InsertInteger32Data(index, markerForInt32, int32Value)
```

```
        'Get the next index
        index = dsInnerCustomData.GetDataCount()
```

```
        'Add the handle of the Circle as handle data to custom data
        dsInnerCustomData.InsertHandle(index, dsCircle.Handle)
```

```
        'Get the next index
        index = dsInnerCustomData.GetDataCount()
```

```
        'Add binary data to custom data
        Dim binaryDataArray As Byte() = New Byte() {0, 1, 0, 1}
        dsInnerCustomData.InsertByteData(index, binaryDataArray)
```

```
        'Set custom data
        dsCircle.SetCustomData(applicationName, dsCustomData)
    End Sub
```

```
    Sub DeleteStringDataFromCustomData(ByVal dsCustomData As CustomData, ByVal dataType As dsCustomDataType_e)
        'Get custom data count
        Dim count As Integer = dsCustomData.GetDataCount()
```

```
        For index As Integer = count - 1 To 0 Step -1
            'Get custom data type
            Dim customDataType As dsCustomDataType_e
            dsCustomData.GetDataType(index, customDataType)
```

```
            If customDataType = dataType Then
                'Delete custom data element
                dsCustomData.Delete(index)
            End If
```

```
            If customDataType = dsCustomDataType_e.dsCustomDataType_CustomData Then
                'Get inner custom data
                Dim dsInnerCustomData As CustomData = Nothing
                dsCustomData.GetCustomData(index, dsInnerCustomData)
```

```
                DeleteStringDataFromCustomData(dsInnerCustomData, dataType)
            End If
        Next
    End Sub
```

```
    Sub ChangeCustomData(ByVal dsCustomData As CustomData)
        'Get custom data count
        Dim count As Integer = dsCustomData.GetDataCount()
```

```
        For index As Integer = 0 To count - 1
            'Get custom data type
            Dim dataType As dsCustomDataType_e
            dsCustomData.GetDataType(index, dataType)
```

```
            Select Case dataType
                Case dsCustomDataType_e.dsCustomDataType_BinaryData
                    If True Then
                        'Get binary data from custom data
                        Dim binaryDataArray As Byte() = DirectCast(dsCustomData.GetByteData(index), Byte())
```

```
                        'Check if binary data is not empty
                        If binaryDataArray IsNot Nothing Then
                            For i As Integer = 0 To binaryDataArray.Length - 1
                                binaryDataArray(i) += 1
                            Next
```

```
                            'Set the updated binary data to custom data
                            dsCustomData.SetByteData(index, binaryDataArray)
                        End If
```

```
                        Exit Select
                    End If
                Case dsCustomDataType_e.dsCustomDataType_CustomData
                    If True Then
                        'Get the inner custom data
                        Dim dsInnerCustomData As CustomData = Nothing
                        dsCustomData.GetCustomData(index, dsInnerCustomData)
```

```
                        ChangeCustomData(dsInnerCustomData)
```

```
                        Exit Select
                    End If
                Case dsCustomDataType_e.dsCustomDataType_Double
                    If True Then
                        'Get double custom data
                        Dim doubleValue As Double
                        dsCustomData.GetDoubleData(index, doubleValue)
```

```
                        'Change double value
                        doubleValue += 1
```

```
                        'Set the updated double value to custom data
                        dsCustomData.SetDoubleData(index, doubleValue)
```

```
                        Exit Select
                    End If
                Case dsCustomDataType_e.dsCustomDataType_Integer16
                    If True Then
                        'Get Int16 custom data
                        Dim intValue As Integer
                        dsCustomData.GetInteger16Data(index, intValue)
```

```
                        'Change Int16 value
                        intValue += 1
```

```
                        'Set the updated Int16 value to custom data
                        dsCustomData.SetInteger16Data(index, intValue)
```

```
                        Exit Select
                    End If
                Case dsCustomDataType_e.dsCustomDataType_Integer32
                    If True Then
                        'Get Int32 custom data
                        Dim intValue As Int32
                        dsCustomData.GetInteger32Data(index, intValue)
```

```
                        'Change Int32 value
                        intValue += 1
```

```
                        'Set the updated Int32 value to custom data
                        dsCustomData.SetInteger32Data(index, intValue)
```

```
                        Exit Select
                    End If
                Case dsCustomDataType_e.dsCustomDataType_Point
                    If True Then
                        'Get point custom data
                        Dim x As Double, y As Double, z As Double
                        dsCustomData.GetPointData(index, x, y, z)
```

```
                        'Change point coordinates
                        x += 2
                        y += 2
                        z += 2
```

```
                        'Set the updated point coordinates to custom data
                        dsCustomData.SetPointData(index, x, y, z)
```

```
                        Exit Select
                    End If
                Case dsCustomDataType_e.dsCustomDataType_String
                    If True Then
                        'Get string custom data
                        Dim stringValue As String = ""
                        dsCustomData.GetStringData(index, stringValue)
```

```
                        'Modify string value
                        stringValue += "_Changed"
```

```
                        'Set the updated string value to custom data
                        dsCustomData.SetStringData(index, stringValue)
```

```
                        Exit Select
                    End If
                Case Else
                    Exit Select
            End Select
        Next
    End Sub
```

```
    Sub PrintCustomDataInfo(ByVal dsCustomData As CustomData)
        'Get custom data count
        Dim count As Integer = dsCustomData.GetDataCount()
        Debug.Print("Custom data count:" + count.ToString())
```

```
        For index As Integer = 0 To count - 1
            'Get custom data type
            Dim dataType As dsCustomDataType_e
            dsCustomData.GetDataType(index, dataType)
```

```
            'Get custom data marker
            Dim marker As Integer
            dsCustomData.GetDataMarker(index, marker)
```

```
            Select Case dataType
                Case dsCustomDataType_e.dsCustomDataType_BinaryData
                    If True Then
                        'Get binary data from custom data
                        Dim binaryDataArray As Byte() = DirectCast(dsCustomData.GetByteData(index), Byte())
                        Dim binaryDataContent As String = String.Empty
```

```
                        If binaryDataArray Is Nothing Then
                            binaryDataContent = "Empty"
                        Else
                            For Each binaryData As Byte In binaryDataArray
                                binaryDataContent += binaryData.ToString() + ","
                            Next
                        End If
```

```
                        'Print custom data index, data type, marker, and binary value
                        PrintCustomDataElement(index, dataType, marker, binaryDataContent)
```

```
                        Exit Select
                    End If
                Case dsCustomDataType_e.dsCustomDataType_CustomData
                    If True Then
                        'Get inner custom data
                        Dim dsGetCustomData As CustomData = Nothing
                        dsCustomData.GetCustomData(index, dsGetCustomData)
```

```
                        PrintCustomDataInfo(dsGetCustomData)
```

```
                        Exit Select
                    End If
                Case dsCustomDataType_e.dsCustomDataType_Double
                    If True Then
                        'Get double value from custom data
                        Dim doubleValue As Double
                        dsCustomData.GetDoubleData(index, doubleValue)
```

```
                        'Print custom data index, data type, marker and double value
                        PrintCustomDataElement(index, dataType, marker, doubleValue)
```

```
                        Exit Select
                    End If
                Case dsCustomDataType_e.dsCustomDataType_Handle
                    If True Then
                        'Get handle value from custom data
                        Dim handle As String = dsCustomData.GetHandleData(index)
```

```
                        'Print custom data index, data type, marker, and handle value
                        PrintCustomDataElement(index, dataType, marker, handle)
```

```
                        Exit Select
                    End If
                Case dsCustomDataType_e.dsCustomDataType_Integer16
                    If True Then
                        Dim intValue As Integer
                        dsCustomData.GetInteger16Data(index, intValue)
```

```
                        'Print custom data index, data type, marker, and Int16 value
                        PrintCustomDataElement(index, dataType, marker, intValue)
```

```
                        Exit Select
                    End If
                Case dsCustomDataType_e.dsCustomDataType_Integer32
                    If True Then
                        Dim intValue As Int32
                        dsCustomData.GetInteger32Data(index, intValue)
```

```
                        'Print custom data index, data type, marker, and Int32 value
                        PrintCustomDataElement(index, dataType, marker, intValue)
```

```
                        Exit Select
                    End If
                Case dsCustomDataType_e.dsCustomDataType_LayerName
                    If True Then
                        'Get layer name from custom data
                        Dim layerName As String = ""
                        dsCustomData.GetLayerName(index, layerName)
```

```
                        'Print custom data index, data type, marker, and layer name value
                        PrintCustomDataElement(index, dataType, marker, layerName)
```

```
                        Exit Select
                    End If
                Case dsCustomDataType_e.dsCustomDataType_Point
                    If True Then
                        'Get point coordinates from custom data
                        Dim x As Double, y As Double, z As Double
                        dsCustomData.GetPointData(index, x, y, z)
```

```
                        'Print custom data index, data type, marker, and point values
                        Dim pointCoordinates As String = x.ToString + "," + y.ToString + "," + z.ToString
                        PrintCustomDataElement(index, dataType, marker, pointCoordinates)
```

```
                        Exit Select
                    End If
                Case dsCustomDataType_e.dsCustomDataType_String
                    If True Then
                        'Get string value from custom data
                        Dim stringValue As String = ""
                        dsCustomData.GetStringData(index, stringValue)
```

```
                        'Print custom data index, data type, marker, and string value
                        PrintCustomDataElement(index, dataType, marker, stringValue)
```

```
                        Exit Select
                    End If
                Case dsCustomDataType_e.dsCustomDataType_Unknown
                    If True Then
                        'Print custom data index, data type, marker and value
                        PrintCustomDataElement(index, dataType, marker, "Unknown value")
```

```
                        Exit Select
                    End If
                Case Else
                    Exit Select
            End Select
        Next
    End Sub
```

```
    Sub PrintCustomDataElement(ByVal index As Integer, ByVal dataType As dsCustomDataType_e, ByVal marker As Integer, ByVal customDataValue As Object)
        'Print custom data index, data type, marker and value
        Dim message As String = "Index: " + index.ToString()
        message += " Data type: " + dataType.ToString()
        message += " Marker: " + marker.ToString()
        message += " Value: " + customDataValue.ToString()
```

```
        Debug.Print(message)
    End Sub
End Module
```
