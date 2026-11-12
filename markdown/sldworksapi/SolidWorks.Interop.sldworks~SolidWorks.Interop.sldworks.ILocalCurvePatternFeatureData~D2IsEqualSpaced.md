---
title: "D2IsEqualSpaced Property (ILocalCurvePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCurvePatternFeatureData"
member: "D2IsEqualSpaced"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2IsEqualSpaced.html"
---

# D2IsEqualSpaced Property (ILocalCurvePatternFeatureData)

Gets or sets whether to use equal spacing between instances of the pattern in Direction 2 for this bidirectional curve-driven component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2IsEqualSpaced As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCurvePatternFeatureData
Dim value As System.Boolean

instance.D2IsEqualSpaced = value

value = instance.D2IsEqualSpaced
```

### C#

```csharp
System.bool D2IsEqualSpaced {get; set;}
```

### C++/CLI

```cpp
property System.bool D2IsEqualSpaced {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use equal spacing in Direction 2, false to use the value set by [ILocalCurvePatternFeatureData::D2Spacing](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalCurvePatternFeatureData~D2Spacing.html)

## VBA Syntax

See [LocalCurvePatternFeatureData::D2Spacing](ms-its:sldworksapivb6.chm::/sldworks~LocalCurvePatternFeatureData~D2Spacing.html).

## Remarks

[ILocalCurvePatternFeatureData::Dir2Specified](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalCurvePatternFeatureData~Dir2Specified.html) must be set to true for this property have an effect.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILocalCurvePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.html)
[ILocalCurvePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData_members.html)
[ILocalCurvePatternFeatureData::D2Direction Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2Direction.html)
[ILocalCurvePatternFeatureData::D2InstanceCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2InstanceCount.html)
[ILocalCurvePatternFeatureData::D2PatternSeedOnly Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2PatternSeedOnly.html)
[ILocalCurvePatternFeatureData::D2ReverseDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2ReverseDirection.html)
[ILocalCurvePatternFeatureData::D1IsEqualSpaced Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1IsEqualSpaced.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
