---
title: "D1AlignmentMethod Property (ILocalCurvePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalCurvePatternFeatureData"
member: "D1AlignmentMethod"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1AlignmentMethod.html"
---

# D1AlignmentMethod Property (ILocalCurvePatternFeatureData)

Gets or sets how to align the instances in this curve-driven component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D1AlignmentMethod As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalCurvePatternFeatureData
Dim value As System.Integer

instance.D1AlignmentMethod = value

value = instance.D1AlignmentMethod
```

### C#

```csharp
System.int D1AlignmentMethod {get; set;}
```

### C++/CLI

```cpp
property System.int D1AlignmentMethod {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Alignment as defined in [swLocalCurvePatternAlignment_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLocalCurvePatternAlignment_e.html)

## VBA Syntax

See [LocalCurvePatternFeatureData::D1AlignmentMethod](ms-its:sldworksapivb6.chm::/sldworks~LocalCurvePatternFeatureData~D1AlignmentMethod.html).

## Examples

[Create Local Curve-driven Pattern (C#)](Create_Local_Curve-driven_Pattern_Example_CSharp.htm)
[Create Local Curve-driven Pattern (VB.NET)](Create_Local_Curve-driven_Pattern_Example_VBNET.htm)
[Create Local Curve-driven Pattern (VBA)](Create_Local_Curve-driven_Pattern_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

For more information, see the **Curve Driven Component Pattern** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ILocalCurvePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData.html)
[ILocalCurvePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData_members.html)
[ILocalCurvePatternFeatureData::D1CurveMethod Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1CurveMethod.html)
[ILocalCurvePatternFeatureData::D1Direction Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1Direction.html)
[ILocalCurvePatternFeatureData::D1InstanceCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1InstanceCount.html)
[ILocalCurvePatternFeatureData::D1IsEqualSpaced Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1IsEqualSpaced.html)
[ILocalCurvePatternFeatureData::D1ReferencePoint Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1ReferencePoint.html)
[ILocalCurvePatternFeatureData::D1ReverseDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1ReverseDirection.html)
[ILocalCurvePatternFeatureData::D1Spacing Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData~D1Spacing.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
