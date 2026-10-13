---
title: "SetCenterPoint Method (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "SetCenterPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetCenterPoint.html"
---

# SetCenterPoint Method (IRenderMaterial)

Obsolete. Superseded by [IRenderMaterial::SetCenterPoint2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial~SetCenterPoint2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCenterPoint( _
   ByRef CenterPt As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim CenterPt As System.Double

instance.SetCenterPoint(CenterPt)
```

### C#

```csharp
void SetCenterPoint(
   ref System.double CenterPt
)
```

### C++/CLI

```cpp
void SetCenterPoint(
   System.double% CenterPt
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CenterPt`: Array of doubles (x, y, z) representing the centerpoint of the mapping for texture-based appearances

## VBA Syntax

See [RenderMaterial::SetCenterPoint](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~SetCenterPoint.html).

## Remarks

This method is required to properly position a texture-based appearance (e.g., if you need a specific corner of a face to have the black square of a checkered-pattern appearance).

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)
[IRenderMaterial::GetCenterPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetCenterPoint.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
