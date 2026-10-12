---
title: "Magnitude Property (ISimulationMotorFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationMotorFeatureData"
member: "Magnitude"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~Magnitude.html"
---

# Magnitude Property (ISimulationMotorFeatureData)

Get or set the magnitude for this motor feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Magnitude As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationMotorFeatureData
Dim value As System.Double

instance.Magnitude = value

value = instance.Magnitude
```

### C#

```csharp
System.double Magnitude {get; set;}
```

### C++/CLI

```cpp
property System.double Magnitude {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Magnitude

## VBA Syntax

See [SimulationMotorFeatureData::Magnitude](ms-its:sldworksapivb6.chm::/sldworks~SimulationMotorFeatureData~Magnitude.html).

## See Also

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.html)
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
