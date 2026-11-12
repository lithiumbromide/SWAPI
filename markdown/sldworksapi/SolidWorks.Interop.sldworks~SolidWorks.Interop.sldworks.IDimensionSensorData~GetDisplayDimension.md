---
title: "GetDisplayDimension Method (IDimensionSensorData)"
project: "SOLIDWORKS API Help"
interface: "IDimensionSensorData"
member: "GetDisplayDimension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionSensorData~GetDisplayDimension.html"
---

# GetDisplayDimension Method (IDimensionSensorData)

Gets the display dimension for this Measurement (dimension) sensor.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayDimension() As DisplayDimension
```

### Visual Basic (Usage)

```vb
Dim instance As IDimensionSensorData
Dim value As DisplayDimension

value = instance.GetDisplayDimension()
```

### C#

```csharp
DisplayDimension GetDisplayDimension()
```

### C++/CLI

```cpp
DisplayDimension^ GetDisplayDimension();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Display dimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html)

## VBA Syntax

See [DimensionSensorData::GetDisplayDimension](ms-its:sldworksapivb6.chm::/sldworks~DimensionSensorData~GetDisplayDimension.html).

## Examples

[Get and Set Sensor (C#)](Get_and_Set_Sensor_Example_CSharp.htm)
[Get and Set Sensor (VB.NET)](Get_and_Set_Sensor_Example_VBNET.htm)
[Get and Set Sensor (VBA)](Get_and_Set_Sensor_Example_VB.htm)

## See Also

[IDimensionSensorData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionSensorData.html)
[IDimensionSensorData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionSensorData_members.html)

## Availability

SOLIDWORKS 2009 SP2, Revision Number 17.2
