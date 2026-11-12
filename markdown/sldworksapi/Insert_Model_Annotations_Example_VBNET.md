---
title: "Insert Model Annotations Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Model_Annotations_Example_VBNET.htm"
---

# Insert Model Annotations Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swModelDocExt As ModelDocExtension
    Dim swDrawing As DrawingDoc
    Dim swSelmgr As SelectionMgr
    Dim swView As View
    Dim annotations As Object
    Dim annot As Object
    Dim swAnnotation As Annotation
    Dim swSelData As SelectData
    Dim mark As Integer
    Dim retval As String
    Dim status As Boolean

    Sub main()

        retval = swApp.GetUserPreferenceStringValue(swUserPreferenceStringValue_e.swDefaultTemplateDrawing)
        swModel = swApp.NewDocument(retval, 0, 0, 0)
        swDrawing = swModel
        swModelDocExt = swModel.Extension
        swSelmgr = swModel.SelectionManager

        ' Create drawing from assembly
        swView = swDrawing.CreateDrawViewFromModelView3("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2024\samples\tutorial\api\wrench.sldasm", "*Front", 0.1314541543147, 0.1407887187817, 0)

        ' Select and activate the view
        status = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
        status = swDrawing.ActivateView("Drawing View1")

        swModel.ClearSelection2(True)

        ' Insert the annotations marked for the drawing
        annotations = swDrawing.InsertModelAnnotations4(swImportModelItemsSource_e.swImportModelItemsFromEntireModel, swInsertAnnotation_e.swInsertDimensionsMarkedForDrawing, True, False, False, False, False, False)

        ' Select and mark each annotation
        swSelData = swSelmgr.CreateSelectData
        mark = 0

        For Each annot In annotations
            swAnnotation = annot
            status = swAnnotation.Select3(True, swSelData)
            swSelData.Mark = mark
            mark = mark + 1
        Next

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
