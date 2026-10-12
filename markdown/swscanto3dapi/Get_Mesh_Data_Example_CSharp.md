---
title: "Get Mesh Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swscanto3dapi/Get_Mesh_Data_Example_CSharp.htm"
---

# Get Mesh Data Example (C#)

This example shows how to get the mesh feature data from a ***.3DS** file. You must have a SOLIDWORKS Premium license to run this example.

```vb
 //----------------------------------------------------------------------------
// Preconditions:
// 1. Click Tools > Add-ins > Scanto3D to activate the Scanto3D add-in.
// 2. Open a *.3DS file.
// 3. Open an Immediate window.
//
// Postconditions: Inspect the Immediate window.
// ---------------------------------------------------------------------------
```

```vb
using
```

Microsoft.VisualBasic;

```vb
using
```

System;

```vb
using
```

System.Collections;

```vb
using
```

System.Collections.Generic;

```vb
using
```

System.Data;

```vb
using
```

System.Diagnostics;

```vb
using
```

SolidWorks.Interop.sldworks;

```vb
using
```

SolidWorks.Interop.swconst;

```vb
using
```

SolidWorks.Interop.swscanto3d;

```vb
using
```

System.Runtime.InteropServices;

```vb
namespace
```

GetMeshData_CSharp.csproj

```vb
{
```

partial class SolidWorksMacro

```vb
{
```

ModelDoc2

swModel;

ModelDocExtension

swModelDocExtension;

Scanto3D

swScanto3D;

bool

boolStatus;

public void

Main()

```vb
    {
```

```vb
    swModel = (
```

ModelDoc2

)swApp.**ActiveDoc**;

```vb
    swModelDocExtension = swModel.Extension;
    swScanto3D = (
```

Scanto3D

)swModelDocExtension.**GetScanto3D**();

int

MeshCount = 0;

int

i = 0;

int

PointsCount = 0;

int

FacetsCount = 0;

object Points = null

;

object Facets = null

;

```vb
    MeshCount = swScanto3D.GetMeshCount();
```

Debug.Print("Number of mesh features: "

+ MeshCount);

for

(i = 0; i <= MeshCount; i++)

```vb
    {
```

```vb
    boolStatus = swScanto3D.GetMeshDataCountAtIndex(i,
```

out PointsCount, out

FacetsCount);

Debug.Print("Number of vertexes in mesh feature " + i + ": "

+ PointsCount);

Debug.Print("Number of facets in mesh feature " + i + ": "

+ FacetsCount);

```vb
    boolStatus = swScanto3D.GetMeshDataAtIndex(i,
```

out Points, out

Facets);

```vb
    }
}
```

public SldWorks

swApp;

```vb
}
}
```
