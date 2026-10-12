---
title: "DampingConstant Property (ISimulationDamperFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationDamperFeatureData"
member: "DampingConstant"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData~DampingConstant.html"
---

# DampingConstant Property (ISimulationDamperFeatureData)

Gets or sets the damping constant value for this damper feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property DampingConstant As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationDamperFeatureData
Dim value As System.Double

instance.DampingConstant = value

value = instance.DampingConstant
```

### C#

```csharp
System.double DampingConstant {get; set;}
```

### C++/CLI

```cpp
property System.double DampingConstant {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Damping constant value

## VBA Syntax

See [SimulationDamperFeatureData::DampingConstant](ms-its:sldworksapivb6.chm::/sldworks~SimulationDamperFeatureData~DampingConstant.html).

## See Also

[ISimulationDamperFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData.html)
[ISimulationDamperFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
