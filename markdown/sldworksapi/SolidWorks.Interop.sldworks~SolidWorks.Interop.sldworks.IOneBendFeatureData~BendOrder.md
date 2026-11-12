---
title: "BendOrder Property (IOneBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IOneBendFeatureData"
member: "BendOrder"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~BendOrder.html"
---

# BendOrder Property (IOneBendFeatureData)

Gets or sets the bend order of this bend.

## Syntax

### Visual Basic (Declaration)

```vb
Property BendOrder As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IOneBendFeatureData
Dim value As System.Integer

instance.BendOrder = value

value = instance.BendOrder
```

### C#

```csharp
System.int BendOrder {get; set;}
```

### C++/CLI

```cpp
property System.int BendOrder {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Bend order

## VBA Syntax

See [OneBendFeatureData::BendOrder](ms-its:sldworksapivb6.chm::/sldworks~OneBendFeatureData~BendOrder.html).

## See Also

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html)
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.html)
[IOneBendFeatureData::GetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~GetCustomBendAllowance.html)
[IOneBendFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~SetCustomBendAllowance.html)
[IOneBendFeatureData::BendAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~BendAngle.html)
[IOneBendFeatureData::BendDown Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~BendDown.html)
[IOneBendFeatureData::BendRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~BendRadius.html)
[IOneBendFeatureData::UseDefaultBendAllowance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~UseDefaultBendAllowance.html)
[IOneBendFeatureData::UseDefaultBendRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~UseDefaultBendRadius.html)

## Availability

SOLIDWORKS 2001 SP1, Revision Number 9.1
