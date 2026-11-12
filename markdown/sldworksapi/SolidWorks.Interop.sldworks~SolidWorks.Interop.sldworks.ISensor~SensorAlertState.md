---
title: "SensorAlertState Property (ISensor)"
project: "SOLIDWORKS API Help"
interface: "ISensor"
member: "SensorAlertState"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertState.html"
---

# SensorAlertState Property (ISensor)

Gets whether an alert is currently triggered for this sensor.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SensorAlertState As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISensor
Dim value As System.Boolean

value = instance.SensorAlertState
```

### C#

```csharp
System.bool SensorAlertState {get;}
```

### C++/CLI

```cpp
property System.bool SensorAlertState {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if an alert is currently triggered for this sensor, false if not

## VBA Syntax

See [Sensor::SensorAlertState](ms-its:sldworksapivb6.chm::/sldworks~Sensor~SensorAlertState.html).

## Examples

[Get and Set Sensor (C#)](Get_and_Set_Sensor_Example_CSharp.htm)
[Get and Set Sensor (VB.NET)](Get_and_Set_Sensor_Example_VBNET.htm)
[Get and Set Sensor (VBA)](Get_and_Set_Sensor_Example_VB.htm)

## See Also

[ISensor Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor.html)
[ISensor Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor_members.html)
[ISensor::SensorAlertType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertType.html)
[ISensor::SensorAlertValue1 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertValue1.html)
[ISensor::SensorAlertValue2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertValue2.html)
[ISensor::SensorAlertEnabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertEnabled.html)

## Availability

SOLIDWORKS 2009 SP2, Revision Number 17.2
