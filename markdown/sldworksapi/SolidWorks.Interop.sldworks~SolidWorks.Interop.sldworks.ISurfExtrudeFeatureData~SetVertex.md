---
title: "SetVertex Method (ISurfExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfExtrudeFeatureData"
member: "SetVertex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~SetVertex.html"
---

# SetVertex Method (ISurfExtrudeFeatureData)

Sets the end condition vertex in the forward or reverse direction for this extruded surface.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetVertex( _
   ByVal Forward As System.Boolean, _
   ByVal Vtx As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfExtrudeFeatureData
Dim Forward As System.Boolean
Dim Vtx As System.Object

instance.SetVertex(Forward, Vtx)
```

### C#

```csharp
void SetVertex(
   System.bool Forward,
   System.object Vtx
)
```

### C++/CLI

```cpp
void SetVertex(
   System.bool Forward,
   System.Object^ Vtx
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`: True sets the vertex in the forward direction, false sets it in the reverse direction
- `Vtx`: End condition [vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html)

## VBA Syntax

See [SurfExtrudeFeatureData::SetVertex](ms-its:sldworksapivb6.chm::/sldworks~SurfExtrudeFeatureData~SetVertex.html).

## See Also

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html)
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.html)
[ISurfExtrudeFeatureData::ISetVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~ISetVertex.html)
[ISurfExtrudeFeatureData::GetVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~GetVertex.html)
[ISurfExtrudeFeatureData::IGetVertex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~IGetVertex.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
