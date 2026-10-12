---
title: "DPartDocEvents_SensorAlertPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_SensorAlertPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_SensorAlertPreNotifyEventHandler.html"
---

# DPartDocEvents_SensorAlertPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired before a sensor's value deviates from its limits in a part document.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_SensorAlertPreNotifyEventHandler( _
   ByVal SensorIn As System.Object, _
   ByVal SensorAlertType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_SensorAlertPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_SensorAlertPreNotifyEventHandler(
   System.object SensorIn,
   System.int SensorAlertType
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_SensorAlertPreNotifyEventHandler(
   System.Object^ SensorIn,
   System.int SensorAlertType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SensorIn`: [Sensor](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISensor.html)
- `SensorAlertType`: Type of sensor as defined in [swSensorAlertType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSensorAlertType_e.html)

## VBA Syntax

See [SensorAlertPreNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~SensorAlertPreNotify_EV.html).

## Examples

[Get and Set Sensor (C#)](Get_and_Set_Sensor_Example_CSharp.htm)
[Get and Set Sensor (VB.NET)](Get_and_Set_Sensor_Example_VBNET.htm)
[Get and Set Sensor (VBA)](Get_and_Set_Sensor_Example_VB.htm)

## Availability

SOLIDWORKS 2009 SP2, Revision Number 17.2
