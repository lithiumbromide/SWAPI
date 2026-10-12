---
title: "DirectionReference Property (ISimulationMotorFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationMotorFeatureData"
member: "DirectionReference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~DirectionReference.html"
---

# DirectionReference Property (ISimulationMotorFeatureData)

Gets or sets the direction in which the motor moves.

## Syntax

### Visual Basic (Declaration)

```vb
Property DirectionReference As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationMotorFeatureData
Dim value As System.Object

instance.DirectionReference = value

value = instance.DirectionReference
```

### C#

```csharp
System.object DirectionReference {get; set;}
```

### C++/CLI

```cpp
property System.Object^ DirectionReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Circular edge; a planar, cylindrical, or conical face; an axis; or a plane indicating the direction to move the motor

## VBA Syntax

See [SimulationMotorFeatureData::DirectionReference](ms-its:sldworksapivb6.chm::/sldworks~SimulationMotorFeatureData~DirectionReference.html).

## Examples

[Create Linear Motor Feature (VBA)](Create_Linear_Motor_Feature_Example_VB.htm)

## See Also

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.html)
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.html)
[ISimulationMotorFeatureData::ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~ReverseDirection.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
