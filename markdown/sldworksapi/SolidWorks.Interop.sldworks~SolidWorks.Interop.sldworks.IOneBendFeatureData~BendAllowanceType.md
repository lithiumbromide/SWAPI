---
title: "BendAllowanceType Property (IOneBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IOneBendFeatureData"
member: "BendAllowanceType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~BendAllowanceType.html"
---

# BendAllowanceType Property (IOneBendFeatureData)

Obsolete. Superseded by [IOneBendFeatureData::GetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IOneBendFeatureData~GetCustomBendAllowance.html) and [IOneBendFeatureData::SetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IOneBendFeatureData~SetCustomBendAllowance.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property BendAllowanceType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IOneBendFeatureData
Dim value As System.Integer

instance.BendAllowanceType = value

value = instance.BendAllowanceType
```

### C#

```csharp
System.int BendAllowanceType {get; set;}
```

### C++/CLI

```cpp
property System.int BendAllowanceType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [OneBendFeatureData::BendAllowanceType](ms-its:sldworksapivb6.chm::/sldworks~OneBendFeatureData~BendAllowanceType.html).

## See Also

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html)
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.html)
