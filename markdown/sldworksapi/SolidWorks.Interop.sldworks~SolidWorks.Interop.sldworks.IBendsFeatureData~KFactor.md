---
title: "KFactor Property (IBendsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBendsFeatureData"
member: "KFactor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~KFactor.html"
---

# KFactor Property (IBendsFeatureData)

Obsolete. Superseded by [IBendsFeatureData::GetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBendsFeatureData~GetCustomBendAllowance.html) and [IBendsFeatureData::SetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBendsFeatureData~SetCustomBendAllowance.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property KFactor As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBendsFeatureData
Dim value As System.Double

instance.KFactor = value

value = instance.KFactor
```

### C#

```csharp
System.double KFactor {get; set;}
```

### C++/CLI

```cpp
property System.double KFactor {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [BendsFeatureData::KFactor](ms-its:sldworksapivb6.chm::/sldworks~BendsFeatureData~KFactor.html).

## See Also

[IBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData.html)
[IBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData_members.html)
