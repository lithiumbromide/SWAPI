---
title: "BendAllowanceType Property (IBendsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBendsFeatureData"
member: "BendAllowanceType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~BendAllowanceType.html"
---

# BendAllowanceType Property (IBendsFeatureData)

Obsolete. Superseded by [IBendsFeatureData::GetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBendsFeatureData~GetCustomBendAllowance.html) and [IBendsFeatureData::SetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBendsFeatureData~SetCustomBendAllowance.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property BendAllowanceType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBendsFeatureData
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

### Property Value

Type of bend allowance as defined in [swBendAllowanceTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBendAllowanceTypes_e.html)

## VBA Syntax

See [BendsFeatureData::BendAllowanceType](ms-its:sldworksapivb6.chm::/sldworks~BendsFeatureData~BendAllowanceType.html).

## See Also

[IBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData.html)
[IBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData_members.html)
