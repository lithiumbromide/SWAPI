---
title: "Insert Model Annotations Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Model_Annotations_Example_VB.htm"
---

# Insert Model Annotations Example (VBA)

This example shows how to automatically insert a model's dimensions marked for drawings into a drawing.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Assembly document to open exists.
' 2. Run the macro.
'
' Postconditions:
' 1. A new drawing document is opened.
' 2. A drawing view of the assembly document is created.
' 3. The dimensions in the assembly document that are marked for drawings,
'    including any duplicate dimensions, appear in the drawing view.
' 4. The dimensions in the drawing, which are annotations,
'    are selected and marked.
'---------------------------------------------------------------------------
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swDrawing As SldWorks.DrawingDoc
Dim swSelmgr As SldWorks.SelectionMgr
Dim swView As SldWorks.View
Dim annotations As Variant
Dim annot As Variant
Dim swAnnotation As SldWorks.Annotation
Dim swSelData As SldWorks.SelectData
Dim mark As Long
Dim retval As String
Dim status As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    retval = swApp.GetUserPreferenceStringValue(swDefaultTemplateDrawing)
    Set swModel = swApp.NewDocument(retval, 0, 0, 0)
    Set swDrawing = swModel
    Set swModelDocExt = swModel.Extension
    Set swSelmgr = swModel.SelectionManager
```

```
    ' Create drawing from assembly
    Set swView = swDrawing.CreateDrawViewFromModelView3("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2024\samples\tutorial\api\wrench.sldasm", "*Front", 0.1314541543147, 0.1407887187817, 0)
```

```
    ' Select and activate the view
    status = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
    status = swDrawing.ActivateView("Drawing View1")
```

```
    swModel.ClearSelection2 True
```

```
    ' Insert the annotations marked for the drawing
    annotations = swDrawing.InsertModelAnnotations4(0, swInsertDimensionsMarkedForDrawing, True, False, False, False, False, False)
```

```
    ' Select and mark each annotation
    Set swSelData = swSelmgr.CreateSelectData
    mark = 0
```

```
    For Each annot In annotations
        Set swAnnotation = annot
        status = swAnnotation.Select3(True, swSelData)
        swSelData.mark = mark
        mark = mark + 1
    Next
```

```
End Sub
```
