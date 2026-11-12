---
title: "TemperatureValue Property (ICWTemperature)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTemperature"
member: "TemperatureValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature~TemperatureValue.html"
---

# TemperatureValue Property (ICWTemperature)

Gets or sets the temperature.

## Syntax

### Visual Basic (Declaration)

```vb
Property TemperatureValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTemperature
Dim value As System.Double

instance.TemperatureValue = value

value = instance.TemperatureValue
```

### C#

```csharp
System.double TemperatureValue {get; set;}
```

### C++/CLI

```cpp
property System.double TemperatureValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Temperature

## VBA Syntax

See [CWTemperature::TemperatureValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTemperature~TemperatureValue.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)

## See Also

[ICWTemperature Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature.html)
[ICWTemperature Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature_members.html)
[ICWTemperature::Unit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature~Unit.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
