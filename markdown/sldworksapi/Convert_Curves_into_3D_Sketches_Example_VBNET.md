---
title: "Convert Curves into 3D Sketches Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Convert_Curves_into_3D_Sketches_Example_VBNET.htm"
---

# Convert Curves into 3D Sketches Example (VB.NET)

This example:

- Shows how to convert curves (edges) into 3D sketches.
- Uses IModelDoc2::SketchConvertIsoCurves to extract ISO-parametric (UV) curves from a face or surface. Specifically, this code shows how to extract the curves containing a vertex.

```
'----------------------------------------------------
' Preconditions:
' 1. Open a part or fully resolved assembly.
' 2. Select a face.
' 3. Press the Ctrl key and select a vertex.
'
' Postconditions:
' 1. Generates two 3D sketches:
'    * First 3D sketch is edge of face in V direction
'      from the selected vertex.
'    * Second 3D sketch is edge of face in U direction
'      from the selected vertex.
' 2. Examine the graphics area and FeatureManager design
'    tree.
'---------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swModel As ModelDoc2
        Dim swSelMgr As SelectionMgr
        Dim swSelData As SelectData
        Dim swFace As Face2
        Dim swVertex As Vertex
        Dim swFaceEnt As Entity
        Dim swVertexEnt As Entity
        Dim bRet As Boolean

        swModel = swApp.ActiveDoc

        swSelMgr = swModel.SelectionManager
        swSelData = swSelMgr.CreateSelectData
        swFace = swSelMgr.GetSelectedObject6(1, -1)
        swVertex = swSelMgr.GetSelectedObject6(2, -1)

        swFaceEnt = swFace
        swVertexEnt = swVertex

        swModel.ClearSelection2(True)

        bRet = swFaceEnt.Select4(True, swSelData)
        bRet = swVertexEnt.Select4(True, swSelData)

        swModel.SketchConvertIsoCurves(100.0#, False, True, True)
        swModel.SketchConvertIsoCurves(100.0#, True, True, True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
