---
title: "SensorAlertType Property (ISensor)"
project: "SOLIDWORKS API Help"
interface: "ISensor"
member: "SensorAlertType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertType.html"
---

# SensorAlertType Property (ISensor)

Gets or sets the type of alert for this sensor.

## Syntax

### Visual Basic (Declaration)

```vb
Property SensorAlertType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISensor
Dim value As System.Integer

instance.SensorAlertType = value

value = instance.SensorAlertType
```

### C#

```csharp
System.int SensorAlertType {get; set;}
```

### C++/CLI

```cpp
property System.int SensorAlertType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of sensor as defined by [swSensorAlertType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSensorAlertType_e.html)

## VBA Syntax

See [Sensor::SensorAlertType](ms-its:sldworksapivb6.chm::/sldworks~Sensor~SensorAlertType.html).

## Examples

[Get and Set Sensor (C#)](Get_and_Set_Sensor_Example_CSharp.htm)
[Get and Set Sensor (VB.NET)](Get_and_Set_Sensor_Example_VBNET.htm)
[Get and Set Sensor (VBA)](Get_and_Set_Sensor_Example_VB.htm)

## See Also

[ISensor Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor.html)
[ISensor Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor_members.html)
[ISensor::SensorAlertEnabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertEnabled.html)
[ISensor::SensorAlertState Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertState.html)
[ISensor::SensorAlertValue1 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertValue1.html)
[ISensor::SensorAlertValue2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertValue2.html)

## Availability

SOLIDWORKS 2009 SP2, Revision Number 17.2
