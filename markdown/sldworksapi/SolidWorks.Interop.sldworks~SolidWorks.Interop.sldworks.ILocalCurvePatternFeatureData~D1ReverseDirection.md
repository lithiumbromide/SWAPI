---
title: "D1ReverseDirection Property (ILocalCurvePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCurvePatternFeatureData"
member: "D1ReverseDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1ReverseDirection.html"
---

# D1ReverseDirection Property (ILocalCurvePatternFeatureData)

Gets or sets whether to reverse the [direction](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalCurvePatternFeatureData~D1Direction.html) of Direction 1 in this curve-driven component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1ReverseDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCurvePatternFeatureData
Dim value As System.Boolean

instance.D1ReverseDirection = value

value = instance.D1ReverseDirection
```

### C#

```csharp
System.bool D1ReverseDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool D1ReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the direction of Direction 1, false to not

## VBA Syntax

See [LocalCurvePatternFeatureData::D1ReverseDirection](ms-its:sldworksapivb6.chm::/sldworks~LocalCurvePatternFeatureData~D1ReverseDirection.html).

## Examples

[Create Local Curve-driven Pattern (C#)](Create_Local_Curve-driven_Pattern_Example_CSharp.htm)
[Create Local Curve-driven Pattern (VB.NET)](Create_Local_Curve-driven_Pattern_Example_VBNET.htm)
[Create Local Curve-Driven Pattern (VBA)](Create_Local_Curve-driven_Pattern_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILocalCurvePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.html)
[ILocalCurvePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData_members.html)
[ILocalCurvePatternFeatureData::D1AlignmentMethod Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1AlignmentMethod.html)
[ILocalCurvePatternFeatureData::D1CurveMethod Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1CurveMethod.html)
[ILocalCurvePatternFeatureData::D1InstanceCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1InstanceCount.html)
[ILocalCurvePatternFeatureData::D1IsEqualSpaced Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1IsEqualSpaced.html)
[ILocalCurvePatternFeatureData::D1ReferencePoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1ReferencePoint.html)
[ILocalCurvePatternFeatureData::D1Spacing Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1Spacing.html)
[ILocalCurvePatternFeatureData::D2ReverseDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2ReverseDirection.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
