---
title: "Convert Edges and Inner Loops of Face to Sketch Entities Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Convert_Edges_and_Inner_Loops_of_Face_to_Sketch_Entities_Example_VBNET.htm"
---

# Convert Edges and Inner Loops of Face to Sketch Entities Example (VB.NET)

## Convert Edges and Inner Loops of Face to Sketch Entities Example (VBA)

This example shows how to convert the edges and inner loops of a selected face to sketch entities on a sketch plane.

```
'------------------------------------------------------------------------
' Preconditions: Open public_documents\samples\tutorial\api\cover_plate.slprt.
'
' Postconditions:
' 1. Creates an offset plane named Plane1.
' 2. Opens a sketch on Plane1.
' 3. Selects a face on the part.
' 4. Converts the edges and inner loops of the selected face to sketch
'    entities and creates Sketch2.
' 5. Examine the graphics area and FeatureManager design tree.
'
' NOTE: Because this part is used elsewhere, do not save changes.
'------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swFeatureManager As FeatureManager
        Dim swRefPlane As RefPlane
        Dim swSketchManager As SketchManager
        Dim boolstatus As Boolean

        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension
        swFeatureManager = swModel.FeatureManager
        swSketchManager = swModel.SketchManager

        'Create offset plane
        boolstatus = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
        swRefPlane = swFeatureManager.InsertRefPlane(8, 0.05, 0, 0, 0, 0)
        swModel.ClearSelection2(True)

        'Open sketch on Plane1
        boolstatus = swModelDocExt.SelectByID2("Plane1", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swSketchManager.InsertSketch(True)

        'Select face whose edges and inner loops to convert
        boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.0456486773091456, 0.085157409722342, 0, False, 0, Nothing, 0)

        'Convert edges and inner loops of selected face to sketch entities
        boolstatus = swSketchManager.SketchUseEdge3(False, True)

        'Clear the selections and close the sketch
        swModel.ClearSelection2(True)
        swSketchManager.InsertSketch(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
