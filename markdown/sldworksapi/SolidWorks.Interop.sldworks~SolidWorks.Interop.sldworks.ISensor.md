---
title: "ISensor Interface"
project: "SOLIDWORKS API Help"
interface: "ISensor"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor.html"
---

# ISensor Interface

Allows access to a sensor, which can monitor selected properties of parts and assemblies and alert you when the sensor's values deviate from the specified limits.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISensor
```

### Visual Basic (Usage)

```vb
Dim instance As ISensor
```

### C#

```csharp
public interface ISensor
```

### C++/CLI

```cpp
public interface class ISensor
```

## VBA Syntax

See [Sensor.](ms-its:sldworksapivb6.chm::/sldworks~Sensor.html)

## Examples

[Get and Set Sensor (C#)](Get_and_Set_Sensor_Example_CSharp.htm)
[Get and Set Sensor (VB.NET)](Get_and_Set_Sensor_Example_VBNET.htm)
[Get and Set Sensor (VBA)](Get_and_Set_Sensor_Example_VB.htm)

## Accessors

[IFeature::GetSpecificFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetSpecificFeature2.html)

## Access Diagram

[Sensor](SWObjectModel.pdf#Sensor)

## See Also

[ISensor Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IDimensionSensorData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionSensorData.html)
[DPartDocEvents_SensorAlertPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_SensorAlertPreNotifyEventHandler.html)
[DAssemblyDocEvents_SensorAlertPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_SensorAlertPreNotifyEventHandler.html)
