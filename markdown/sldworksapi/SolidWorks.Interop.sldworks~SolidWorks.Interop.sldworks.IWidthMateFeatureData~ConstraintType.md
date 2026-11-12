---
title: "ConstraintType Property (IWidthMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWidthMateFeatureData"
member: "ConstraintType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~ConstraintType.html"
---

# ConstraintType Property (IWidthMateFeatureData)

Gets or sets the type of constraint for this width mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property ConstraintType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IWidthMateFeatureData
Dim value As System.Integer

instance.ConstraintType = value

value = instance.ConstraintType
```

### C#

```csharp
System.int ConstraintType {get; set;}
```

### C++/CLI

```cpp
property System.int ConstraintType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Constraint type as defined in [swMateWidthOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateWidthOptions_e.html)

## VBA Syntax

See [WidthMateFeatureData::ConstraintType](ms-its:sldworksapivb6.chm::/sldworks~WidthMateFeatureData~ConstraintType.html).

## See Also

[IWidthMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData.html)
[IWidthMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData_members.html)
[IWidthMateFeatureData::DistanceFromEnd Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~DistanceFromEnd.html)
[IWidthMateFeatureData::FlipDimension Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~FlipDimension.html)
[IWidthMateFeatureData::PercentDistanceFromEnd Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~PercentDistanceFromEnd.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
