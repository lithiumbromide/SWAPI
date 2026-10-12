---
title: "NumberOfCoils Property (ISimulationSpringFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationSpringFeatureData"
member: "NumberOfCoils"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~NumberOfCoils.html"
---

# NumberOfCoils Property (ISimulationSpringFeatureData)

Gets or sets the number of coils in this simulation spring feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property NumberOfCoils As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationSpringFeatureData
Dim value As System.Integer

instance.NumberOfCoils = value

value = instance.NumberOfCoils
```

### C#

```csharp
System.int NumberOfCoils {get; set;}
```

### C++/CLI

```cpp
property System.int NumberOfCoils {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of coils

## VBA Syntax

See [SimulationSpringFeatureData::NumberOfCoils](ms-its:sldworksapivb6.chm::/sldworks~SimulationSpringFeatureData~NumberOfCoils.html).

## Examples

[Add Spring to Motion Study (C#)](Add_Spring_to_Motion_Study_Example_CSharp.htm)
[Add Spring to Motion Study (VB.NET)](Add_Spring_to_Motion_Study_Example_VBNET.htm)
[Add Spring to Motion Study (VBA)](Add_Spring_to_Motion_Study_Example_VB.htm)

## See Also

[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.html)
[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.html)
[ISimulationSpringFeatureData::CoilDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~CoilDiameter.html)
[ISimulationSpringFeatureData::WireDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~WireDiameter.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
