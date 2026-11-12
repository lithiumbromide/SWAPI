---
title: "UpdateSensor Method (ISensor)"
project: "SOLIDWORKS API Help"
interface: "ISensor"
member: "UpdateSensor"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~UpdateSensor.html"
---

# UpdateSensor Method (ISensor)

Updates the sensor.

## Syntax

### Visual Basic (Declaration)

```vb
Function UpdateSensor() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISensor
Dim value As System.Boolean

value = instance.UpdateSensor()
```

### C#

```csharp
System.bool UpdateSensor()
```

### C++/CLI

```cpp
System.bool UpdateSensor();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the sensor is updated, false if not

## VBA Syntax

See [Sensor::UpdateSensor](ms-its:sldworksapivb6.chm::/sldworks~Sensor~UpdateSensor.html).

## Examples

[Get and Set Sensor (C#)](Get_and_Set_Sensor_Example_CSharp.htm)
[Get and Set Sensor (VB.NET)](Get_and_Set_Sensor_Example_VBNET.htm)
[Get and Set Sensor (VBA)](Get_and_Set_Sensor_Example_VB.htm)

## See Also

[ISensor Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor.html)
[ISensor Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor_members.html)
[ISensor::SensorType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorType.html)

## Availability

SOLIDWORKS 2009 SP2, Revision Number 17.2
