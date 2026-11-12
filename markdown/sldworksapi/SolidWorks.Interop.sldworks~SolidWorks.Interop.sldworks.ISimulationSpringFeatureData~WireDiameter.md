---
title: "WireDiameter Property (ISimulationSpringFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationSpringFeatureData"
member: "WireDiameter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~WireDiameter.html"
---

# WireDiameter Property (ISimulationSpringFeatureData)

Gets or sets the diameter of the wire for this simulation spring feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property WireDiameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationSpringFeatureData
Dim value As System.Double

instance.WireDiameter = value

value = instance.WireDiameter
```

### C#

```csharp
System.double WireDiameter {get; set;}
```

### C++/CLI

```cpp
property System.double WireDiameter {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Wire diameter

## VBA Syntax

See [SimulationSpringFeatureData::WireDiameter](ms-its:sldworksapivb6.chm::/sldworks~SimulationSpringFeatureData~WireDiameter.html).

## Examples

[Add Spring to Motion Study (C#)](Add_Spring_to_Motion_Study_Example_CSharp.htm)
[Add Spring to Motion Study (VB.NET)](Add_Spring_to_Motion_Study_Example_VBNET.htm)
[Add Spring to Motion Study (VBA)](Add_Spring_to_Motion_Study_Example_VB.htm)

## See Also

[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.html)
[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.html)
[ISimulationSpringFeatureData::CoilDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~CoilDiameter.html)
[ISimulationSpringFeatureData::NumberOfCoils Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~NumberOfCoils.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
