---
title: "ThinWallType Property (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "ThinWallType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~ThinWallType.html"
---

# ThinWallType Property (ISweepFeatureData)

Gets or sets the type of this thin-walled sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThinWallType As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Short

instance.ThinWallType = value

value = instance.ThinWallType
```

### C#

```csharp
System.short ThinWallType {get; set;}
```

### C++/CLI

```cpp
property System.short ThinWallType {
   System.short get();
   void set (    System.short value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

- 0 = One Direction
- 1 = One Direction Reverse
- 2 = MidPlane
- 3 = Two Directions

## VBA Syntax

See [SweepFeatureData::ThinWallType](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~ThinWallType.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

This property is:

- only valid if [ISweepFeatureData::IsThinFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IsThinFeature.html) is true.
- not valid for swept-surface features.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::SetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetWallThickness.html)
[ISweepFeatureData::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IsThinFeature.html)
[ISweepFeatureData::GetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetWallThickness.html)
[ISweepFeatureData::ThinFeature Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~ThinFeature.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
