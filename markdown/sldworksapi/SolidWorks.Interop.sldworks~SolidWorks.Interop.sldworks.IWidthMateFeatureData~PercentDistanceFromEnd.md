---
title: "PercentDistanceFromEnd Property (IWidthMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWidthMateFeatureData"
member: "PercentDistanceFromEnd"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~PercentDistanceFromEnd.html"
---

# PercentDistanceFromEnd Property (IWidthMateFeatureData)

Gets or sets the percentage of distance from the end of this width mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property PercentDistanceFromEnd As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IWidthMateFeatureData
Dim value As System.Double

instance.PercentDistanceFromEnd = value

value = instance.PercentDistanceFromEnd
```

### C#

```csharp
System.double PercentDistanceFromEnd {get; set;}
```

### C++/CLI

```cpp
property System.double PercentDistanceFromEnd {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Percentage of distance from the end

## VBA Syntax

See [WidthMateFeatureData::PercentDistanceFromEnd](ms-its:sldworksapivb6.chm::/sldworks~WidthMateFeatureData~PercentDistanceFromEnd.html).

## Remarks

This property is valid only if [IWidthMateFeatureData::ConstraintType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~ConstraintType.html) is set to [swMateWidthOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateWidthOptions_e.html).swMateWidth_Percent.

## See Also

[IWidthMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData.html)
[IWidthMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
