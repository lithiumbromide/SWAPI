---
title: "MotionType Property (ISimulationMotorFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationMotorFeatureData"
member: "MotionType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~MotionType.html"
---

# MotionType Property (ISimulationMotorFeatureData)

Gets or sets the type of motion of this motor feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property MotionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationMotorFeatureData
Dim value As System.Integer

instance.MotionType = value

value = instance.MotionType
```

### C#

```csharp
System.int MotionType {get; set;}
```

### C++/CLI

```cpp
property System.int MotionType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of motion as defined in [swSimulationMotorMotionType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSimulationMotorMotionType_e.html)

## VBA Syntax

See [SimulationMotorFeatureData::MotionType](ms-its:sldworksapivb6.chm::/sldworks~SimulationMotorFeatureData~MotionType.html).

## See Also

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.html)
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
