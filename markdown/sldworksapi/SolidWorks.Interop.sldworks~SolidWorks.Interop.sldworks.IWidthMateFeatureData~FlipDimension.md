---
title: "FlipDimension Property (IWidthMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWidthMateFeatureData"
member: "FlipDimension"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~FlipDimension.html"
---

# FlipDimension Property (IWidthMateFeatureData)

Gets or sets whether to move entities to opposite sides of the dimension of this width mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlipDimension As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWidthMateFeatureData
Dim value As System.Boolean

instance.FlipDimension = value

value = instance.FlipDimension
```

### C#

```csharp
System.bool FlipDimension {get; set;}
```

### C++/CLI

```cpp
property System.bool FlipDimension {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flip the dimension, false to not (see **Remarks**)

## VBA Syntax

See [WidthMateFeatureData::FlipDimension](ms-its:sldworksapivb6.chm::/sldworks~WidthMateFeatureData~FlipDimension.html).

## Remarks

This property is valid only if [IWidthMateFeatureData::ConstraintType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~ConstraintType.html) is set to [swMateWidthOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateWidthOptions_e.html).swMateWidth_Dimension or swMateWidth_Percent.

## See Also

[IWidthMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData.html)
[IWidthMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
