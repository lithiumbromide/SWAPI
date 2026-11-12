---
title: "Symmetric Property (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "Symmetric"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Symmetric.html"
---

# Symmetric Property (ICircularPatternFeatureData)

Gets or sets whether to create a symmetric or asymmetric circular pattern feature in Direction 2.

## Syntax

### Visual Basic (Declaration)

```vb
Property Symmetric As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
Dim value As System.Boolean

instance.Symmetric = value

value = instance.Symmetric
```

### C#

```csharp
System.bool Symmetric {get; set;}
```

### C++/CLI

```cpp
property System.bool Symmetric {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to create a symmetric circular pattern feature in Direction 2, false to create an asymmetrical circular pattern feature in Direction 2

## VBA Syntax

See [CircularPatternFeatureData::Symmetric](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~Symmetric.html).

## Examples

[Create Bidirectional Circular Pattern Feature (C#)](Create_Bidirectional_Circular_Pattern_Feature_Example_CSharp.htm)
[Create Bidirectional Circular Pattern Feature (VB.NET)](Create_Bidirectional_Circular_Pattern_Feature_Example_VBNET.htm)
[Create Bidirectional Circular Pattern Feature (VBA)](Create_Bidirectional_Circular_Pattern_Feature_Example_VB.htm)

## Remarks

This property is only available when [ICircularPatternFeatureData::Direction2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Direction2.html) is true.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)
[ICircularPatternFeatureData::EqualSpacing2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~EqualSpacing2.html)
[ICircularPatternFeatureData::Spacing2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Spacing2.html)
[ICircularPatternFeatureData::TotalInstances2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~TotalInstances2.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
