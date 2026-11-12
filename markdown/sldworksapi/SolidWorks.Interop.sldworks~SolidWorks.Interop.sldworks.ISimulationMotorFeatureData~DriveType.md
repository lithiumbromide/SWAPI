---
title: "DriveType Property (ISimulationMotorFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISimulationMotorFeatureData"
member: "DriveType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~DriveType.html"
---

# DriveType Property (ISimulationMotorFeatureData)

Sets the drive type of this motor feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property DriveType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimulationMotorFeatureData
Dim value As System.Integer

instance.DriveType = value

value = instance.DriveType
```

### C#

```csharp
System.int DriveType {get; set;}
```

### C++/CLI

```cpp
property System.int DriveType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Drive type as defined in [swSimulationMotorDriveType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSimulationMotorDriveType_e.html)

## VBA Syntax

See [SimulationMotorFeatureData::DriveType](ms-its:sldworksapivb6.chm::/sldworks~SimulationMotorFeatureData~DriveType.html).

## See Also

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.html)
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
