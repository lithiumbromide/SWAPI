---
title: "D1Direction Property (ILocalCurvePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCurvePatternFeatureData"
member: "D1Direction"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1Direction.html"
---

# D1Direction Property (ILocalCurvePatternFeatureData)

Gets or sets Direction 1 using the selected curve, edge, sketch, or sketch entity for this curve-driven component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1Direction As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCurvePatternFeatureData
Dim value As System.Object

instance.D1Direction = value

value = instance.D1Direction
```

### C#

```csharp
System.object D1Direction {get; set;}
```

### C++/CLI

```cpp
property System.Object^ D1Direction {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html), [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html), [sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html), or sketch entity for Direction 1

## VBA Syntax

See [LocalCurvePatternFeatureData::D1Direction](ms-its:sldworksapivb6.chm::/sldworks~LocalCurvePatternFeatureData~D1Direction.html).

## Remarks

You must pre-select the direction entity using selection Mark = 1 before creating the feature definition. If you are using a 3D curve for Direction 1, then you must also pre-select the face normal entity using selection Mark = 64.

Use this property only when editing the pattern feature.

If you specify this property using a 3D curve, you should also specify [ILocalCurvePatternFeatureData::D1FaceNormal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1FaceNormal.html).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILocalCurvePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.html)
[ILocalCurvePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData_members.html)
[ILocalCurvePatternFeatureData::D1AlignmentMethod Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1AlignmentMethod.html)
[ILocalCurvePatternFeatureData::D1CurveMethod Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1CurveMethod.html)
[ILocalCurvePatternFeatureData::D1InstanceCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1InstanceCount.html)
[ILocalCurvePatternFeatureData::D1IsEqualSpaced Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1IsEqualSpaced.html)
[ILocalCurvePatternFeatureData::D1ReferencePoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1ReferencePoint.html)
[ILocalCurvePatternFeatureData::D1ReverseDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1ReverseDirection.html)
[ILocalCurvePatternFeatureData::D1Spacing Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1Spacing.html)
[ILocalCurvePatternFeatureData::D2Direction Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2Direction.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
