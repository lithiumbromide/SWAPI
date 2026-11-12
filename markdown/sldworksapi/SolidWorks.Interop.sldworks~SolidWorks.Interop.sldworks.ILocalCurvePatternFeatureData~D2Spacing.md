---
title: "D2Spacing Property (ILocalCurvePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCurvePatternFeatureData"
member: "D2Spacing"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2Spacing.html"
---

# D2Spacing Property (ILocalCurvePatternFeatureData)

Gets or sets the distance between pattern instances in Direction 2 in this bidirectional curve-driven component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2Spacing As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCurvePatternFeatureData
Dim value As System.Double

instance.D2Spacing = value

value = instance.D2Spacing
```

### C#

```csharp
System.double D2Spacing {get; set;}
```

### C++/CLI

```cpp
property System.double D2Spacing {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance between pattern instances in Direction 2 (see **Remarks**)

## VBA Syntax

See [LocalCurvePatternFeatureData::D2Spacing](ms-its:sldworksapivb6.chm::/sldworks~LocalCurvePatternFeatureData~D2Spacing.html).

## Remarks

[ILocalCurvePatternFeatureData::Dir2Specified](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalCurvePatternFeatureData~Dir2Specified.html) must be set to true for this property have an effect. To set the spacing between pattern instances, set [ILocalCurvePatternFeatureData::D2IsEqualSpaced](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalCurvePatternFeatureData~D2IsEqualSpaced.html) to false.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILocalCurvePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.html)
[ILocalCurvePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData_members.html)
[ILocalCurvePatternFeatureData::D2Direction Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2Direction.html)
[ILocalCurvePatternFeatureData::D2InstanceCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2InstanceCount.html)
[ILocalCurvePatternFeatureData::D2PatternSeedOnly Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2PatternSeedOnly.html)
[ILocalCurvePatternFeatureData::D2ReverseDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2ReverseDirection.html)
[ILocalCurvePatternFeatureData::D1Spacing Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1Spacing.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
