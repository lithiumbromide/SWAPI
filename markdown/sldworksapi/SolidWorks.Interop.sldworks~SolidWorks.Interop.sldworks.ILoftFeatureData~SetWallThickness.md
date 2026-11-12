---
title: "SetWallThickness Method (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "SetWallThickness"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~SetWallThickness.html"
---

# SetWallThickness Method (ILoftFeatureData)

Sets the wall thickness for this loft feature in the forward or reverse direction.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetWallThickness( _
   ByVal Forward As System.Boolean, _
   ByVal WallThickness As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData
Dim Forward As System.Boolean
Dim WallThickness As System.Double

instance.SetWallThickness(Forward, WallThickness)
```

### C#

```csharp
void SetWallThickness(
   System.bool Forward,
   System.double WallThickness
)
```

### C++/CLI

```cpp
void SetWallThickness(
   System.bool Forward,
   System.double WallThickness
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`: True for forward feature direction, false for reverse
- `WallThickness`: Wall thickness

## VBA Syntax

See [LoftFeatureData::SetWallThickness](ms-its:sldworksapivb6.chm::/sldworks~LoftFeatureData~SetWallThickness.html).

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)
[ILoftFeatureData::GetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetWallThickness.html)
[ILoftFeatureData::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IsThinFeature.html)
[ILoftFeatureData::ThinWallType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ThinWallType.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
