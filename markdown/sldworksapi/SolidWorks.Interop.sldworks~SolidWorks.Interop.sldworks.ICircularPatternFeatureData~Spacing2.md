---
title: "Spacing2 Property (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "Spacing2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Spacing2.html"
---

# Spacing2 Property (ICircularPatternFeatureData)

Gets or sets the spacing between pattern instances in Direction 2 of this bidirectional circular pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Spacing2 As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
Dim value As System.Double

instance.Spacing2 = value

value = instance.Spacing2
```

### C#

```csharp
System.double Spacing2 {get; set;}
```

### C++/CLI

```cpp
property System.double Spacing2 {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance in radians between pattern instances in Direction 2

## VBA Syntax

See [CircularPatternFeatureData::Spacing2](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~Spacing2.html).

## Examples

[Create Bidirectional Circular Pattern Feature (C#)](Create_Bidirectional_Circular_Pattern_Feature_Example_CSharp.htm)
[Create Bidirectional Circular Pattern Feature (VB.NET)](Create_Bidirectional_Circular_Pattern_Feature_Example_VBNET.htm)
[Create Bidirectional Circular Pattern Feature (VBA)](Create_Bidirectional_Circular_Pattern_Feature_Example_VB.htm)

## Remarks

This property is only available when:

- [ICircularPatternFeatureData::Direction2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Direction2.html) is true, and
- [ICircularPatternFeatureData::Symmetric](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Symmetric.html) is false.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)
[ICircularPatternFeatureData::EqualSpacing2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~EqualSpacing2.html)
[ICircularPatternFeatureData::TotalInstances2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~TotalInstances2.html)
[ICircularPatternFeatureData::Spacing Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Spacing.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
