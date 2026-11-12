---
title: "Velocity Property (ISimulationMotorFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationMotorFeatureData"
member: "Velocity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~Velocity.html"
---

# Velocity Property (ISimulationMotorFeatureData)

Gets or sets the speed of the motor if no other force acts on it.

## Syntax

### Visual Basic (Declaration)

```vb
Property Velocity As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationMotorFeatureData
Dim value As System.Double

instance.Velocity = value

value = instance.Velocity
```

### C#

```csharp
System.double Velocity {get; set;}
```

### C++/CLI

```cpp
property System.double Velocity {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Speed of the motor

## VBA Syntax

See [SimulationMotorFeatureData::Velocity](ms-its:sldworksapivb6.chm::/sldworks~SimulationMotorFeatureData~Velocity.html).

## See Also

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.html)
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
