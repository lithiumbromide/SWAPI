---
title: "CoilDiameter Property (ISimulationSpringFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationSpringFeatureData"
member: "CoilDiameter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~CoilDiameter.html"
---

# CoilDiameter Property (ISimulationSpringFeatureData)

Gets or sets the diameter of the coil for this simulation spring feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property CoilDiameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationSpringFeatureData
Dim value As System.Double

instance.CoilDiameter = value

value = instance.CoilDiameter
```

### C#

```csharp
System.double CoilDiameter {get; set;}
```

### C++/CLI

```cpp
property System.double CoilDiameter {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Coil diameter

## VBA Syntax

See [SimulationSpringFeatureData::CoilDiameter](ms-its:sldworksapivb6.chm::/sldworks~SimulationSpringFeatureData~CoilDiameter.html).

## Examples

[Add Spring to Motion Study (C#)](Add_Spring_to_Motion_Study_Example_CSharp.htm)
[Add Spring to Motion Study (VB.NET)](Add_Spring_to_Motion_Study_Example_VBNET.htm)
[Add Spring to Motion Study (VBA)](Add_Spring_to_Motion_Study_Example_VB.htm)

## See Also

[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.html)
[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.html)
[ISimulationSpringFeatureData::NumberOfCoils Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~NumberOfCoils.html)
[ISimulationSpringFeatureData::WireDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~WireDiameter.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
