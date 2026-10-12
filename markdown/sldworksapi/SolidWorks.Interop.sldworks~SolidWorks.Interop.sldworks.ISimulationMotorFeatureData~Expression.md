---
title: "Expression Property (ISimulationMotorFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationMotorFeatureData"
member: "Expression"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~Expression.html"
---

# Expression Property (ISimulationMotorFeatureData)

Gets or sets the motor motion expression for this motor feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Expression As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationMotorFeatureData
Dim value As System.String

instance.Expression = value

value = instance.Expression
```

### C#

```csharp
System.string Expression {get; set;}
```

### C++/CLI

```cpp
property System.String^ Expression {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Motion motor expression in document units

## VBA Syntax

See [SimulationMotorFeatureData::Expression](ms-its:sldworksapivb6.chm::/sldworks~SimulationMotorFeatureData~Expression.html).

## See Also

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.html)
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.html)
[ISimulationMotorFeatureData::ConstantSpeedMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~ConstantSpeedMotor.html)
[ISimulationMotorFeatureData::DistanceMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~DistanceMotor.html)
[ISimulationMotorFeatureData::InterpolatedMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~InterpolatedMotor.html)
[ISimulationMotorFeatureData::OscillatingMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~OscillatingMotor.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
