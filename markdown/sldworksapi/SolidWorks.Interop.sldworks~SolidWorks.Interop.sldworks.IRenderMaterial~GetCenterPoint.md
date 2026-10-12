---
title: "GetCenterPoint Method (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "GetCenterPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetCenterPoint.html"
---

# GetCenterPoint Method (IRenderMaterial)

Obsolete. Superseded by [IRenderMaterial::GetCenterPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~GetCenterPoint2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetCenterPoint( _
   ByRef CenterPt As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim CenterPt As System.Double

instance.GetCenterPoint(CenterPt)
```

### C#

```csharp
void GetCenterPoint(
   out System.double CenterPt
)
```

### C++/CLI

```cpp
void GetCenterPoint(
   [Out] System.double CenterPt
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CenterPt`: Array of doubles (x, y, z) representing the centerpoint of the mapping for texture-based appearances

### Return Value

Array of doubles (x, y, z) representing the centerpoint of the mapping for texture-based appearances

## VBA Syntax

See [RenderMaterial::GetCenterPoint](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~GetCenterPoint.html).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)
[IRenderMaterial::SetCenterPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetCenterPoint.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
