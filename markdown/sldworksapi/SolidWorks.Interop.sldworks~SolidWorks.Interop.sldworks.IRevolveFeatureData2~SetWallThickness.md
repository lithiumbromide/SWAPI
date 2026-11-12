---
title: "SetWallThickness Method (IRevolveFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRevolveFeatureData2"
member: "SetWallThickness"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~SetWallThickness.html"
---

# SetWallThickness Method (IRevolveFeatureData2)

Sets the wall thickness of the thin revolution feature in forward/reverse direction.

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
Dim instance As IRevolveFeatureData2
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

See [RevolveFeatureData2::SetWallThickness](ms-its:sldworksapivb6.chm::/sldworks~RevolveFeatureData2~SetWallThickness.html).

## Remarks

This method only affects thin features.

## See Also

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.html)
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.html)
[IRevolveFeatureData2::GetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~GetWallThickness.html)
[IRevolveFeatureData2::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~IsThinFeature.html)
[IRevolveFeatureData2::ThinWallType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~ThinWallType.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
