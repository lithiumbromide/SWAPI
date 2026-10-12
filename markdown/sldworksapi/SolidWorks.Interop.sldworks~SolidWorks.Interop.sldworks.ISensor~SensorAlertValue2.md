---
title: "SensorAlertValue2 Property (ISensor)"
project: "SOLIDWORKS API Help"
interface: "ISensor"
member: "SensorAlertValue2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertValue2.html"
---

# SensorAlertValue2 Property (ISensor)

Gets or sets alert value for this sensor; only in effect when [sensor alert type](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISensor~SensorAlertType.html) set to swSensorAlert_Between.

## Syntax

### Visual Basic (Declaration)

```vb
Property SensorAlertValue2 As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISensor
Dim value As System.Double

instance.SensorAlertValue2 = value

value = instance.SensorAlertValue2
```

### C#

```csharp
System.double SensorAlertValue2 {get; set;}
```

### C++/CLI

```cpp
property System.double SensorAlertValue2 {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Alert value

## VBA Syntax

See [Sensor::SensorAlertValue2](ms-its:sldworksapivb6.chm::/sldworks~Sensor~SensorAlertValue2.html).

## Examples

[Get and Set Sensor (C#)](Get_and_Set_Sensor_Example_CSharp.htm)
[Get and Set Sensor (VB.NET)](Get_and_Set_Sensor_Example_VBNET.htm)
[Get and Set Sensor (VBA)](Get_and_Set_Sensor_Example_VB.htm)

## See Also

[ISensor Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor.html)
[ISensor Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor_members.html)
[ISensor::SensorAlertValue1 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertValue1.html)
[ISensor::SensorAlertState Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertState.html)
[ISensor::SensorAlertEnabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertEnabled.html)

## Availability

SOLIDWORKS 2009 SP2, Revision Number 17.2
