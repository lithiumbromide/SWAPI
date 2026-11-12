---
title: "BendDown Property (IOneBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IOneBendFeatureData"
member: "BendDown"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~BendDown.html"
---

# BendDown Property (IOneBendFeatureData)

Gets or sets the bend-down state of this bend.

## Syntax

### Visual Basic (Declaration)

```vb
Property BendDown As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IOneBendFeatureData
Dim value As System.Boolean

instance.BendDown = value

value = instance.BendDown
```

### C#

```csharp
System.bool BendDown {get; set;}
```

### C++/CLI

```cpp
property System.bool BendDown {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to set bend down, false to not

## VBA Syntax

See [OneBendFeatureData::BendDown](ms-its:sldworksapivb6.chm::/sldworks~OneBendFeatureData~BendDown.html).

## See Also

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html)
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.html)
[IOneBendFeatureData::BendAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~BendAngle.html)
[IOneBendFeatureData::BendOrder Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~BendOrder.html)
[IOneBendFeatureData::BendRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~BendRadius.html)
[IOneBendFeatureData::GetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~GetCustomBendAllowance.html)
[IOneBendFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~SetCustomBendAllowance.html)
[IOneBendFeatureData::UseDefaultBendAllowance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~UseDefaultBendAllowance.html)
[IOneBendFeatureData::UseDefaultBendRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~UseDefaultBendRadius.html)
[IOneBendFeatureData::BendDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~BendDirection.html)

## Availability

SOLIDWORKS 2001 SP1, Revision Number 9.1
