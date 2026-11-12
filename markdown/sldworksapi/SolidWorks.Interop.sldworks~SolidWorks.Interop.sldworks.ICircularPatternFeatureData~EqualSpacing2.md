---
title: "EqualSpacing2 Property (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "EqualSpacing2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~EqualSpacing2.html"
---

# EqualSpacing2 Property (ICircularPatternFeatureData)

Gets or sets whether the pattern instances in Direction 2 are equally spaced in this bidirectional circular pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property EqualSpacing2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
Dim value As System.Boolean

instance.EqualSpacing2 = value

value = instance.EqualSpacing2
```

### C#

```csharp
System.bool EqualSpacing2 {get; set;}
```

### C++/CLI

```cpp
property System.bool EqualSpacing2 {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use equal spacing in Direction 2, false to not

## VBA Syntax

See [CircularPatternFeatureData::EqualSpacing2](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~EqualSpacing2.html).

## Examples

[Create Bidirectional Circular Pattern Feature (C#)](Create_Bidirectional_Circular_Pattern_Feature_Example_CSharp.htm)
[Create Bidirectional Circular Pattern Feature (VB.NET)](Create_Bidirectional_Circular_Pattern_Feature_Example_VBNET.htm)
[Create Bidirectional Circular Pattern Feature (VBA)](Create_Bidirectional_Circular_Pattern_Feature_Example_VB.htm)

## Remarks

This property is only available when:

- [ICircularPatternFeatureData::Direction2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Direction2.html) is true and
- [ICircularPatternFeatureData::Symmetric](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Symmetric.html) is false.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)
[ICircularPatternFeatureData::Spacing2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Spacing2.html)
[ICircularPatternFeatureData::TotalInstances2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~TotalInstances2.html)
[ICircularPatternFeatureData::EqualSpacing Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~EqualSpacing.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
