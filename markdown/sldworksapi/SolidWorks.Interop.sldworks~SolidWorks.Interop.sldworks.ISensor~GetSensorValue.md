---
title: "GetSensorValue Method (ISensor)"
project: "SOLIDWORKS API Help"
interface: "ISensor"
member: "GetSensorValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~GetSensorValue.html"
---

# GetSensorValue Method (ISensor)

Gets the value and units of this sensor.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSensorValue( _
   ByRef Value As System.Double, _
   ByRef Units As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISensor
Dim Value As System.Double
Dim Units As System.String
Dim value As System.Boolean

value = instance.GetSensorValue(Value, Units)
```

### C#

```csharp
System.bool GetSensorValue(
   out System.double Value,
   out System.string Units
)
```

### C++/CLI

```cpp
System.bool GetSensorValue(
   [Out] System.double Value,
   [Out] System.String^ Units
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Value`: Value of the sensor
- `Units`: Units of the sensor

### Return Value

True if successful, false if not

## VBA Syntax

See [Sensor::GetSensorValue](ms-its:sldworksapivb6.chm::/sldworks~Sensor~GetSensorValue.html).

## See Also

[ISensor Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor.html)
[ISensor Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
