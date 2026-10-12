---
title: "ThinFeature Property (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "ThinFeature"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~ThinFeature.html"
---

# ThinFeature Property (ISweepFeatureData)

Gets or sets whether to make this sweep feature a thin-walled feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThinFeature As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Boolean

instance.ThinFeature = value

value = instance.ThinFeature
```

### C#

```csharp
System.bool ThinFeature {get; set;}
```

### C++/CLI

```cpp
property System.bool ThinFeature {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to make a thin-walled sweep feature, false to not

## VBA Syntax

See [SweepFeatureData::ThinFeature](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~ThinFeature.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

To make a thin sweep, you must set this property before calling [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html). You cannot make a thin-walled sweep feature after the sweep has been created, and you cannot edit a sweep feature to make it thin walled.

This property is not valid for swept-surface features.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::ThinWallType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~ThinWallType.html)
[ISweepFeatureData::SetWallThickness Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetWallThickness.html)
[ISweepFeatureData::IsThinFeature Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~IsThinFeature.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
