---
title: "D2ReverseDirection Property (ILocalCurvePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCurvePatternFeatureData"
member: "D2ReverseDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2ReverseDirection.html"
---

# D2ReverseDirection Property (ILocalCurvePatternFeatureData)

Gets or sets whether to reverse the [direction](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalCurvePatternFeatureData~D2Direction.html) of Direction 2 in this bidirectional curve-driven component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2ReverseDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCurvePatternFeatureData
Dim value As System.Boolean

instance.D2ReverseDirection = value

value = instance.D2ReverseDirection
```

### C#

```csharp
System.bool D2ReverseDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool D2ReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the direction of Direction 2, false to not

## VBA Syntax

See [LocalCurvePatternFeatureData::D2ReverseDirection](ms-its:sldworksapivb6.chm::/sldworks~LocalCurvePatternFeatureData~D2ReverseDirection.html).

## Remarks

[ILocalCurvePatternFeatureData::Dir2Specified](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalCurvePatternFeatureData~Dir2Specified.html) must be set to true for this property have an effect.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILocalCurvePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.html)
[ILocalCurvePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData_members.html)
[ILocalCurvePatternFeatureData::D2Direction Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2Direction.html)
[ILocalCurvePatternFeatureData::D2InstanceCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2InstanceCount.html)
[ILocalCurvePatternFeatureData::D2IsEqualSpaced Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2IsEqualSpaced.html)
[ILocalCurvePatternFeatureData::D2PatternSeedOnly Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2PatternSeedOnly.html)
[ILocalCurvePatternFeatureData::D2Spacing Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2Spacing.html)
[ILocalCurvePatternFeatureData::D1ReverseDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1ReverseDirection.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
