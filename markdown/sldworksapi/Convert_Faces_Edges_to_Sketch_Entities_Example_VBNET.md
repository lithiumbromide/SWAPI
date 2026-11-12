---
title: "Convert Faces' Edges to Sketch Entities Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Convert_Faces_Edges_to_Sketch_Entities_Example_VBNET.htm"
---

# Convert Faces' Edges to Sketch Entities Example (VB.NET)

This example shows how to convert the edges of a face to sketch entities.

```
'-----------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\cosmosxpress\aw_hook.sldprt.
' 2. If prompted to convert to appearances, click OK.
'
' Postconditions:
' 1. Converts the edges of the selected faces to sketch entities
'    onto Plane1, and creates Sketch3.
' 2. Examine the FeatureManager design tree.
'
' NOTE: Because this part is used elsewhere, do not save changes.
'--------------------------------------------------------------
```

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchManager As SketchManager
        Dim boolstatus As Boolean

        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension
        swSketchManager = swModel.SketchManager

        ' Open sketch on Plane1
        boolstatus = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swSketchManager.InsertSketch(True)

        ' Select disjoint faces
        boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.1098855514325, -0.05688720168837, 0.03453543805836, False, 0, Nothing, 0)
        boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.1161834220602, 0.002276177312467, 0.03345674799152, True, 0, Nothing, 0)

        ' Convert edges of faces to sketch entities
        boolstatus = swSketchManager.SketchUseEdge2(False)

        ' Clear the selections and close the sketch
        swModel.ClearSelection2(True)
        swSketchManager.InsertSketch(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
