---
title: "Get Mesh Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swscanto3dapi/Get_Mesh_Data_Example_VB.htm"
---

# Get Mesh Data Example (VBA)

This example shows how to get the mesh feature data from a ***.3DS** file. You must have a SOLIDWORKS Premium license to run this example.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Click Tools > Add-ins > Scanto3D to activate the Scanto3D add-in.
 ' 2. Open a *.3DS file.
 ' 3. Open an Immediate window.
 '
 ' Postconditions: Inspect the Immediate window.
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim swModel As ModelDoc2
 Dim swModelDocExtension As ModelDocExtension
 Dim swScanto3D As Scanto3DLib.Scanto3D
 Dim boolStatus As Boolean
 Option Explicit
 Sub Main()
    Set swApp = Application.SldWorks

    Set swModel = swApp.ActiveDoc
     Set swModelDocExtension = swModel.Extension
     Set swScanto3D = swModelDocExtension.GetScanto3D()
    Dim MeshCount As Long
     Dim i As Long
     Dim PointsCount As Long
     Dim FacetsCount As Long
     Dim Points As Object
     Dim Facets As Object

    MeshCount = swScanto3D.GetMeshCount()
     Debug.Print "Number of mesh features: " & MeshCount

    For i = 0 To MeshCount
         boolStatus = swScanto3D.GetMeshDataCountAtIndex(i, PointsCount, FacetsCount)
         Debug.Print "Number of vertexes in mesh feature " & i & ": " & PointsCount
         Debug.Print "Number of facets in mesh feature " & i & ": " & FacetsCount
         boolStatus = swScanto3D.GetMeshDataAtIndex(i, Points, Facets)
     Next

End Sub
```
