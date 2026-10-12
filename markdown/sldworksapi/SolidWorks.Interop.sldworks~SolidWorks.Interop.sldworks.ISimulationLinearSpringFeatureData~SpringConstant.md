---
title: "SpringConstant Property (ISimulationLinearSpringFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationLinearSpringFeatureData"
member: "SpringConstant"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationLinearSpringFeatureData~SpringConstant.html"
---

# SpringConstant Property (ISimulationLinearSpringFeatureData)

Obsolete. Superseded by [ISimulationSpringFeatureData::SpringConstant](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimulationSpringFeatureData~SpringConstant.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property SpringConstant As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationLinearSpringFeatureData
Dim value As System.Double

instance.SpringConstant = value

value = instance.SpringConstant
```

### C#

```csharp
System.double SpringConstant {get; set;}
```

### C++/CLI

```cpp
property System.double SpringConstant {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Strength

## VBA Syntax

See [SimulationLinearSpringFeatureData::SpringConstant](ms-its:sldworksapivb6.chm::/sldworks~SimulationLinearSpringFeatureData~SpringConstant.html).

## See Also

[ISimulationLinearSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationLinearSpringFeatureData.html)
[ISimulationLinearSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationLinearSpringFeatureData_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
