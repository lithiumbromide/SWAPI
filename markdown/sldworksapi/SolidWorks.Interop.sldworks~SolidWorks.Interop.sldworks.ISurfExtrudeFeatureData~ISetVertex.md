---
title: "ISetVertex Method (ISurfExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfExtrudeFeatureData"
member: "ISetVertex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~ISetVertex.html"
---

# ISetVertex Method (ISurfExtrudeFeatureData)

Sets the end condition vertex in the forward or reverse direction for this extruded surface.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetVertex( _
   ByVal Forward As System.Boolean, _
   ByVal Vtx As Vertex _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfExtrudeFeatureData
Dim Forward As System.Boolean
Dim Vtx As Vertex

instance.ISetVertex(Forward, Vtx)
```

### C#

```csharp
void ISetVertex(
   System.bool Forward,
   Vertex Vtx
)
```

### C++/CLI

```cpp
void ISetVertex(
   System.bool Forward,
   Vertex^ Vtx
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`: True sets the vertex in the forward direction, false sets it in the reverse direction
- `Vtx`: End condition [vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html)

## VBA Syntax

See [SurfExtrudeFeatureData::ISetVertex](ms-its:sldworksapivb6.chm::/sldworks~SurfExtrudeFeatureData~ISetVertex.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html)
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.html)
[ISurfExtrudeFeatureData::SetVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetVertex.html)
[ISurfExtrudeFeatureData::GetVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetVertex.html)
[ISurfExtrudeFeatureData::IGetVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~IGetVertex.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
