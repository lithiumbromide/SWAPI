---
title: "DistanceFromEnd Property (IWidthMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWidthMateFeatureData"
member: "DistanceFromEnd"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~DistanceFromEnd.html"
---

# DistanceFromEnd Property (IWidthMateFeatureData)

Gets or sets the distance from the end of this width mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property DistanceFromEnd As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IWidthMateFeatureData
Dim value As System.Double

instance.DistanceFromEnd = value

value = instance.DistanceFromEnd
```

### C#

```csharp
System.double DistanceFromEnd {get; set;}
```

### C++/CLI

```cpp
property System.double DistanceFromEnd {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance from the end

## VBA Syntax

See [WidthMateFeatureData::DistanceFromEnd](ms-its:sldworksapivb6.chm::/sldworks~WidthMateFeatureData~DistanceFromEnd.html).

## Remarks

This property is valid only if [IWidthMateFeatureData::ConstraintType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~ConstraintType.html) is set to [swMateWidthOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateWidthOptions_e.html).swMateWidth_Dimension.

## See Also

[IWidthMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData.html)
[IWidthMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
