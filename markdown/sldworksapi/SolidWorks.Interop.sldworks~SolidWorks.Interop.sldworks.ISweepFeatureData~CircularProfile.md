---
title: "CircularProfile Property (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "CircularProfile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~CircularProfile.html"
---

# CircularProfile Property (ISweepFeatureData)

Gets or sets whether to use a circular profile for this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property CircularProfile As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Boolean

instance.CircularProfile = value

value = instance.CircularProfile
```

### C#

```csharp
System.bool CircularProfile {get; set;}
```

### C++/CLI

```cpp
property System.bool CircularProfile {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use a circular profile, false to use a [sketch profile or tool body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Profile.html)

## VBA Syntax

See [SweepFeatureData::CircularProfile](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~CircularProfile.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

If this property is set to false, call [ISweepFeatureData::GetCutSweepOption](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetCutSweepOption.html) to determine the type of profile.

To get or set the diameter of a circular profile, use [ISweepFeatureData::CircularProfileDiameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~CircularProfileDiameter.html).

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::GetProfileType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetProfileType.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
