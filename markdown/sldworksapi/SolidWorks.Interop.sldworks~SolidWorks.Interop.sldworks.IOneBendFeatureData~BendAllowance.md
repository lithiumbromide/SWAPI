---
title: "BendAllowance Property (IOneBendFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IOneBendFeatureData"
member: "BendAllowance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~BendAllowance.html"
---

# BendAllowance Property (IOneBendFeatureData)

Obsolete. Superseded by [IOneBendFeatureData::GetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IOneBendFeatureData~GetCustomBendAllowance.html) and [IOneBendFeatureData::SetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IOneBendFeatureData~SetCustomBendAllowance.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property BendAllowance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IOneBendFeatureData
Dim value As System.Double

instance.BendAllowance = value

value = instance.BendAllowance
```

### C#

```csharp
System.double BendAllowance {get; set;}
```

### C++/CLI

```cpp
property System.double BendAllowance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [OneBendFeatureData::BendAllowance](ms-its:sldworksapivb6.chm::/sldworks~OneBendFeatureData~BendAllowance.html).

## See Also

[IOneBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData.html)
[IOneBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.html)
