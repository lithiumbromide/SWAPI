---
title: "DAssemblyDocEvents_SensorAlertPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_SensorAlertPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_SensorAlertPreNotifyEventHandler.html"
---

# DAssemblyDocEvents_SensorAlertPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired before a sensor's value deviates from its limits in an assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_SensorAlertPreNotifyEventHandler( _
   ByVal SensorIn As System.Object, _
   ByVal SensorAlertType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_SensorAlertPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_SensorAlertPreNotifyEventHandler(
   System.object SensorIn,
   System.int SensorAlertType
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_SensorAlertPreNotifyEventHandler(
   System.Object^ SensorIn,
   System.int SensorAlertType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SensorIn`: [Sensor](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISensor.html)
- `SensorAlertType`: Type of sensor as defined in [swSensorAlertType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSensorAlertType_e.html)

## VBA Syntax

See [SensorAlertPreNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~SensorAlertPreNotify_EV.html).

## Availability

SOLIDWORKS 2009 SP2, Revision Number 17.2
