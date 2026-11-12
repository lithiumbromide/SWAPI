---
title: "TemperatureType Property (ICWTemperature)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTemperature"
member: "TemperatureType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature~TemperatureType.html"
---

# TemperatureType Property (ICWTemperature)

Gets or sets the temperature type for transient studies.

## Syntax

### Visual Basic (Declaration)

```vb
Property TemperatureType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTemperature
Dim value As System.Integer

instance.TemperatureType = value

value = instance.TemperatureType
```

### C#

```csharp
System.int TemperatureType {get; set;}
```

### C++/CLI

```cpp
property System.int TemperatureType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Temperature type as defined in [swsTemperatureType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTemperatureType_e.html)

## VBA Syntax

See [CWTemperature::TemperatureType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTemperature~TemperatureType.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)

## See Also

[ICWTemperature Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature.html)
[ICWTemperature Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
