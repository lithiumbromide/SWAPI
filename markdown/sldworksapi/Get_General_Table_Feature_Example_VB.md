---
title: "Get General Table Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_General_Table_Feature_Example_VB.htm"
---

# Get General Table Feature Example (VBA)

This example shows how to get a general table feature and some of its table annotation data.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified drawing document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified drawing document.
' 2. Inserts a table annotation.
' 3. Gets the general table feature.
' 4. Prints the name of the general table feature and
'    some of its annotation table data the Immediate window.
' 5. Examine the Immediate window.
'
' NOTE: Because the drawing document is used elsewhere, do not
' save changes.
'-----------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDrawing As SldWorks.DrawingDoc
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
Dim swTableAnnotation As SldWorks.TableAnnotation
Dim swGeneralTableFeature As SldWorks.GeneralTableFeature
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeature As SldWorks.Feature
Dim nbrTableAnnotations As Long
Dim tableAnnotations As Variant
Dim i As Long
Dim anchorAttached As Boolean
Dim anchorType As Long
Dim nbrColumns As Long
Dim nbrRows As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open drawing document
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\assem20.slddrw"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    'Insert table annotation
    Set swDrawing = swModel
    Set swTableAnnotation = swDrawing.InsertTableAnnotation2(False, 2.75123456559767E-02, 0.132124518483965, 1, "", 2, 2)
    If Not swTableAnnotation Is Nothing Then
       swTableAnnotation.BorderLineWeight = 0
       swTableAnnotation.GridLineWeight = 0
    End If
```

```
    'Select and get general table feature
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("General Table1", "GENERALTABLEFEAT", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swGeneralTableFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swFeature = swGeneralTableFeature.GetFeature
    Debug.Print "General table feature name: " & swFeature.Name
```

```
    'Get general table feature's annotation data
    nbrTableAnnotations = swGeneralTableFeature.GetTableAnnotationCount
    Debug.Print "Number of annotations = " & nbrTableAnnotations
    tableAnnotations = swGeneralTableFeature.GetTableAnnotations
    For i = 0 To (nbrTableAnnotations - 1)
        Set swTableAnnotation = tableAnnotations(i)
        anchorAttached = swTableAnnotation.Anchored
        Debug.Print "Table anchored        = " & anchorAttached
        anchorType = swTableAnnotation.anchorType
        Debug.Print "Anchor type           = " & anchorType
        nbrColumns = swTableAnnotation.ColumnCount
        Debug.Print "Number of columns     = " & nbrColumns
        nbrRows = swTableAnnotation.RowCount
        Debug.Print "Number of rows        = " & nbrRows
    Next i
```

```
End Sub
```
