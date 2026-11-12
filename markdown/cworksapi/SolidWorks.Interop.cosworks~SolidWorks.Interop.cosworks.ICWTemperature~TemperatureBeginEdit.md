---
title: "TemperatureBeginEdit Method (ICWTemperature)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTemperature"
member: "TemperatureBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature~TemperatureBeginEdit.html"
---

# TemperatureBeginEdit Method (ICWTemperature)

Starts editing the temperature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub TemperatureBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTemperature

instance.TemperatureBeginEdit()
```

### C#

```csharp
void TemperatureBeginEdit()
```

### C++/CLI

```cpp
void TemperatureBeginEdit();
```

## VBA Syntax

See [CWTemperature::TemperatureBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTemperature~TemperatureBeginEdit.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)

## Remarks

To start editing the temperature, you must call this method. You must call [ICWTemperature::TemperatureEndEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWTemperature~TemperatureEndEdit.html) to end editing the temperature. Changes are not applied unless you call both methods.

## See Also

[ICWTemperature Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature.html)
[ICWTemperature Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
