---
title: "Get Mesh Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swscanto3dapi/Get_Mesh_Data_Example_VBNET.htm"
---

# Get Mesh Data Example (VB.NET)

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
```

```vb
Imports
```

SolidWorks.Interop.sldworks

```vb
Imports
```

SolidWorks.Interop.swconst

```vb
Imports
```

SolidWorks.Interop.swscanto3d

```vb
Imports
```

System.Runtime.InteropServices

```vb
Imports
```

System

```vb
Imports
```

System.Diagnostics

```vb
Partial
```

Class

SolidWorksMacro

Dim swModel As

ModelDoc2

Dim swModelDocExtension As

ModelDocExtension

Dim swScanto3D As

Scanto3D

Dim boolStatus As Boolean

Sub

Main()

```vb
swModel = swApp.ActiveDoc
swModelDocExtension = swModel.Extension
swScanto3D = swModelDocExtension.GetScanto3D()
```

Dim MeshCount As Integer

Dim i As Integer

Dim PointsCount As Integer

Dim FacetsCount As Integer

Dim Points As Object = Nothing

Dim Facets As Object = Nothing

```vb
MeshCount = swScanto3D.GetMeshCount()
Debug.Print(
```

"Number of mesh features: "

& MeshCount)

For i = 0 To

MeshCount

```vb
boolStatus = swScanto3D.GetMeshDataCountAtIndex(i, PointsCount, FacetsCount)
Debug.Print(
```

"Number of vertexes in mesh feature " & i & ": "

& PointsCount)

```vb
Debug.Print(
```

"Number of facets in mesh feature " & i & ": "

& FacetsCount)

```vb
boolStatus = swScanto3D.GetMeshDataAtIndex(i, Points, Facets)
```

Next

End

Sub

Public swApp As

SldWorks

```vb
End
```

Class
