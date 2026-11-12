---
title: "BendAllowance Property (IBendsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBendsFeatureData"
member: "BendAllowance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~BendAllowance.html"
---

# BendAllowance Property (IBendsFeatureData)

Obsolete. Superseded by [IBendsFeatureData::GetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBendsFeatureData~GetCustomBendAllowance.html) and [IBendsFeatureData::SetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBendsFeatureData~SetCustomBendAllowance.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property BendAllowance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBendsFeatureData
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

### Property Value

## VBA Syntax

See [BendsFeatureData::BendAllowance](ms-its:sldworksapivb6.chm::/sldworks~BendsFeatureData~BendAllowance.html).

## See Also

[IBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData.html)
[IBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData_members.html)
