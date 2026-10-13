---
title: "SensorType Property (ISensor)"
project: "SOLIDWORKS API Help"
interface: "ISensor"
member: "SensorType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorType.html"
---

# SensorType Property (ISensor)

Gets the type of this sensor.

## Syntax

### Visual Basic (Declaration)

```vb
Property SensorType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISensor
Dim value As System.Integer

instance.SensorType = value

value = instance.SensorType
```

### C#

```csharp
System.int SensorType {get; set;}
```

### C++/CLI

```cpp
property System.int SensorType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of sensor as defined in [swSensorType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSensorType_e.html)

## VBA Syntax

See [Sensor::SensorType](ms-its:sldworksapivb6.chm::/sldworks~Sensor~SensorType.html).

## Examples

[Get and Set Sensor (C#)](Get_and_Set_Sensor_Example_CSharp.htm)
[Get and Set Sensor (VB.NET)](Get_and_Set_Sensor_Example_VBNET.htm)
[Get and Set Sensor (VBA)](Get_and_Set_Sensor_Example_VB.htm)

## Requirements

As of SOLIDWORKS 2009 SP02, only measurement (dimension) sensors of type swSensorType_e.swSensorDimension are supported.

## See Also

[ISensor Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor.html)
[ISensor Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor_members.html)

## Availability

SOLIDWORKS 2009 SP2, Revision Number 17.2
