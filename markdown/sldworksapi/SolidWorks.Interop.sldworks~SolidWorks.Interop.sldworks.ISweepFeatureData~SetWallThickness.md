---
title: "SetWallThickness Method (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "SetWallThickness"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetWallThickness.html"
---

# SetWallThickness Method (ISweepFeatureData)

Sets the wall thickness, forward (Direction 1) or reverse (Direction 2), of this thin-walled sweep feature.

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
Dim instance As ISweepFeatureData
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

- `Forward`: True for Direction 1, false for Direction 2 (see **Remarks**)
- `WallThickness`: Wall thickness

## VBA Syntax

See [SweepFeatureData::SetWallThickness](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~SetWallThickness.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

This method:

- is valid only if [ISweepFeatureData::IsThinFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IsThinFeature.html) is true.
- sets the thickness in Direction 1 and Direction 2, depending on [ISweepFeaureData::ThinWallType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~ThinWallType.html).
- is not valid for swept-surface features.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IsThinFeature.html)
[ISweepFeatureData::GetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetWallThickness.html)
[ISweepFeatureData::ThinFeature Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~ThinFeature.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
