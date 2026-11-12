---
title: "SensorAlertEnabled Property (ISensor)"
project: "SOLIDWORKS API Help"
interface: "ISensor"
member: "SensorAlertEnabled"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertEnabled.html"
---

# SensorAlertEnabled Property (ISensor)

Gets or sets whether an alert is triggered when the limits of the sensor deviate from its specified values.

## Syntax

### Visual Basic (Declaration)

```vb
Property SensorAlertEnabled As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISensor
Dim value As System.Boolean

instance.SensorAlertEnabled = value

value = instance.SensorAlertEnabled
```

### C#

```csharp
System.bool SensorAlertEnabled {get; set;}
```

### C++/CLI

```cpp
property System.bool SensorAlertEnabled {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True for an alert to be triggered when the limits of the sensor deviate from its specified values, false for it to not

## VBA Syntax

See [Sensor::SensorAlertEnabled](ms-its:sldworksapivb6.chm::/sldworks~Sensor~SensorAlertEnabled.html).

## Examples

[Get and Set Sensor (C#)](Get_and_Set_Sensor_Example_CSharp.htm)
[Get and Set Sensor (VB.NET)](Get_and_Set_Sensor_Example_VBNET.htm)
[Get and Set Sensor (VBA)](Get_and_Set_Sensor_Example_VB.htm)

## See Also

[ISensor Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor.html)
[ISensor Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor_members.html)
[ISensor::SensorAlertState Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertState.html)
[ISensor::SensorAlertType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertType.html)
[ISensor::SensorAlertValue1 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertValue1.html)
[ISensor::SensorAlertValue2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertValue2.html)
[DAssemblyDocEvents_SensorAlertPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_SensorAlertPreNotifyEventHandler.html)
[DPartDocEvents_SensorAlertPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_SensorAlertPreNotifyEventHandler.html)

## Availability

SOLIDWORKS 2009 SP2, Revision Number 17.2
