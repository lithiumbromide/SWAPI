---
title: "SensorValue Property (IDimensionSensorData)"
project: "SOLIDWORKS API Help"
interface: "IDimensionSensorData"
member: "SensorValue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionSensorData~SensorValue.html"
---

# SensorValue Property (IDimensionSensorData)

Gets the value of the display dimension for this Measurement (dimension) sensor.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SensorValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDimensionSensorData
Dim value As System.Double

value = instance.SensorValue
```

### C#

```csharp
System.double SensorValue {get;}
```

### C++/CLI

```cpp
property System.double SensorValue {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value of the display dimension for this Measurement (dimension) sensor

## VBA Syntax

See [DimensionSensorData::SensorValue](ms-its:sldworksapivb6.chm::/sldworks~DimensionSensorData~SensorValue.html).

## Examples

[Get and Set Sensor (C#)](Get_and_Set_Sensor_Example_CSharp.htm)
[Get and Set Sensor (VB.NET)](Get_and_Set_Sensor_Example_VBNET.htm)
[Get and Set Sensor (VBA)](Get_and_Set_Sensor_Example_VB.htm)

## See Also

[IDimensionSensorData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionSensorData.html)
[IDimensionSensorData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionSensorData_members.html)

## Availability

SOLIDWORKS 2009 SP2, Revision Number 17.2
