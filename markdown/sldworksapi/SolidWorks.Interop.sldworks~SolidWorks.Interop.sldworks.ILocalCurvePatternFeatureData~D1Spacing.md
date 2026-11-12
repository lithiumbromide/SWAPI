---
title: "D1Spacing Property (ILocalCurvePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCurvePatternFeatureData"
member: "D1Spacing"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1Spacing.html"
---

# D1Spacing Property (ILocalCurvePatternFeatureData)

Gets or sets the distance between pattern instances in Direction 1 in this curve-driven component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1Spacing As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCurvePatternFeatureData
Dim value As System.Double

instance.D1Spacing = value

value = instance.D1Spacing
```

### C#

```csharp
System.double D1Spacing {get; set;}
```

### C++/CLI

```cpp
property System.double D1Spacing {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance between pattern instances in Direction 1 (see **Remarks**)

## VBA Syntax

See [LocalCurvePatternFeatureData::D1Spacing](ms-its:sldworksapivb6.chm::/sldworks~LocalCurvePatternFeatureData~D1Spacing.html).

## Examples

[Create Local Curve-driven Pattern (C#)](Create_Local_Curve-driven_Pattern_Example_CSharp.htm)
[Create Local Curve-driven Pattern (VB.NET)](Create_Local_Curve-driven_Pattern_Example_VBNET.htm)
[Create Local Curve-Driven Pattern (VBA)](Create_Local_Curve-driven_Pattern_Example_VB.htm)

## Remarks

To set the spacing between pattern instances, set [ILocalCurvePatternFeatureData::Dir1IsEqualSpaced](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalCurvePatternFeatureData~D1IsEqualSpaced.html) to false.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ILocalCurvePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.html)
[ILocalCurvePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData_members.html)
[ILocalCurvePatternFeatureData::D1AlignmentMethod Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1AlignmentMethod.html)
[ILocalCurvePatternFeatureData::D1CurveMethod Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1CurveMethod.html)
[ILocalCurvePatternFeatureData::D1Direction Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1Direction.html)
[ILocalCurvePatternFeatureData::D1InstanceCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1InstanceCount.html)
[ILocalCurvePatternFeatureData::D1ReferencePoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1ReferencePoint.html)
[ILocalCurvePatternFeatureData::D1ReverseDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1ReverseDirection.html)
[ILocalCurvePatternFeatureData::D2Spacing Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D2Spacing.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
