---
title: "MotorType Property (ISimulationMotorFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationMotorFeatureData"
member: "MotorType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~MotorType.html"
---

# MotorType Property (ISimulationMotorFeatureData)

Gets the type of motor for this motor feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property MotorType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationMotorFeatureData
Dim value As System.Integer

value = instance.MotorType
```

### C#

```csharp
System.int MotorType {get;}
```

### C++/CLI

```cpp
property System.int MotorType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of motor as defined in [swSimulationMotorType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSimulationMotorType_e.html)

## VBA Syntax

See [SimulationMotorFeatureData::MotorType](ms-its:sldworksapivb6.chm::/sldworks~SimulationMotorFeatureData~MotorType.html).

## Examples

[Create Linear Motor Feature (VBA)](Create_Linear_Motor_Feature_Example_VB.htm)

## See Also

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.html)
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
