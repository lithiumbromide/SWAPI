---
title: "GetSensorFeatureData Method (ISensor)"
project: "SOLIDWORKS API Help"
interface: "ISensor"
member: "GetSensorFeatureData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~GetSensorFeatureData.html"
---

# GetSensorFeatureData Method (ISensor)

Gets a sensor feature data.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSensorFeatureData() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISensor
Dim value As System.Object

value = instance.GetSensorFeatureData()
```

### C#

```csharp
System.object GetSensorFeatureData()
```

### C++/CLI

```cpp
System.Object^ GetSensorFeatureData();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Sensor feature data](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionSensorData.html) (see **Remarks**)

## VBA Syntax

See [Sensor::GetSensorFeatureData](ms-its:sldworksapivb6.chm::/sldworks~Sensor~GetSensorFeatureData.html).

## Examples

[Get and Set Sensor (C#)](Get_and_Set_Sensor_Example_CSharp.htm)
[Get and Set Sensor (VB.NET)](Get_and_Set_Sensor_Example_VBNET.htm)
[Get and Set Sensor (VBA)](Get_and_Set_Sensor_Example_VB.htm)

## Remarks

Currently only Measurement (dimension) sensors are supported.

## See Also

[ISensor Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor.html)
[ISensor Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor_members.html)

## Availability

SOLIDWORKS 2009 SP2, Revision Number 17.2
