---
title: "Convert Curves into 3D Sketches Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Convert_Curves_into_3D_Sketches_Example_VB.htm"
---

# Convert Curves into 3D Sketches Example (VBA)

This example:

- Shows how to convert curves (edges) into 3D sketches.
- Uses IModelDoc2::SketchConvertIsoCurves to extract ISO-parametric (UV) curves from a face or surface. Specifically, this code shows how to extract the curves containing a vertex.

```
'---------------------------------
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
'-----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSelData As SldWorks.SelectData
    Dim swFace As SldWorks.Face2
    Dim swVertex As SldWorks.Vertex
    Dim swFaceEnt As SldWorks.Entity
    Dim swVertexEnt As SldWorks.Entity
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc

    Set swSelMgr = swModel.SelectionManager
    Set swSelData = swSelMgr.CreateSelectData
    Set swFace = swSelMgr.GetSelectedObject6(1, -1)
    Set swVertex = swSelMgr.GetSelectedObject6(2, -1)

    Set swFaceEnt = swFace
    Set swVertexEnt = swVertex
```

```
    swModel.ClearSelection2 True
```

```
    bRet = swFaceEnt.Select4(True, swSelData)
    bRet = swVertexEnt.Select4(True, swSelData)
```

```
    swModel.SketchConvertIsoCurves 100#, False, True, True
    swModel.SketchConvertIsoCurves 100#, True, True, True
```

```
End Sub
```
