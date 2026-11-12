---
title: "D2Direction Property (ILocalCurvePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCurvePatternFeatureData"
member: "D2Direction"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2Direction.html"
---

# D2Direction Property (ILocalCurvePatternFeatureData)

Gets or sets Direction 2 using the selected curve, edge, sketch, or sketch entity for this bidirectional curve-driven component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2Direction As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCurvePatternFeatureData
Dim value As System.Object

instance.D2Direction = value

value = instance.D2Direction
```

### C#

```csharp
System.object D2Direction {get; set;}
```

### C++/CLI

```cpp
property System.Object^ D2Direction {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html), [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html), [sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html), or sketch entity for Direction 2

## VBA Syntax

See [LocalCurvePatternFeatureData::D2Direction](ms-its:sldworksapivb6.chm::/sldworks~LocalCurvePatternFeatureData~D2Direction.html).

## Remarks

You must pre-select the direction entity using selection Mark = 1 before creating the feature definition. Use this property only when editing the pattern feature.

[ILocalCurvePatternFeatureData::Dir2Specified](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalCurvePatternFeatureData~Dir2Specified.html) must be set to true for this property have an effect.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILocalCurvePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.html)
[ILocalCurvePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData_members.html)
[ILocalCurvePatternFeatureData::D2InstanceCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2InstanceCount.html)
[ILocalCurvePatternFeatureData::D2IsEqualSpaced Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2IsEqualSpaced.html)
[ILocalCurvePatternFeatureData::D2PatternSeedOnly Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2PatternSeedOnly.html)
[ILocalCurvePatternFeatureData::D2ReverseDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2ReverseDirection.html)
[ILocalCurvePatternFeatureData::D2Spacing Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2Spacing.html)
[ILocalCurvePatternFeatureData::D1Direction Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1Direction.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
