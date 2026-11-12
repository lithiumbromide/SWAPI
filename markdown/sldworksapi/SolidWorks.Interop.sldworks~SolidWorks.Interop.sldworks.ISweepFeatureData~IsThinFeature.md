---
title: "IsThinFeature Method (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "IsThinFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IsThinFeature.html"
---

# IsThinFeature Method (ISweepFeatureData)

Gets whether this is a thin-walled sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsThinFeature() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Boolean

value = instance.IsThinFeature()
```

### C#

```csharp
System.bool IsThinFeature()
```

### C++/CLI

```cpp
System.bool IsThinFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if a thin-walled sweep feature, false if not

## VBA Syntax

See [SweepFeatureData::IsThinFeature](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~IsThinFeature.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

Note that you can make a sweep feature thin-walled only by setting [ISweepFeatureData::ThinFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~ThinFeature.html) at the time of creation.

This method is not valid for swept-surface features.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::SetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetWallThickness.html)
[ISweepFeatureData::ThinWallType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~ThinWallType.html)
[ISweepFeatureData::GetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetWallThickness.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
