---
title: "TemperatureEndEdit Method (ICWTemperature)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTemperature"
member: "TemperatureEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature~TemperatureEndEdit.html"
---

# TemperatureEndEdit Method (ICWTemperature)

Ends editing the temperature.

## Syntax

### Visual Basic (Declaration)

```vb
Function TemperatureEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTemperature
Dim value As System.Integer

value = instance.TemperatureEndEdit()
```

### C#

```csharp
System.int TemperatureEndEdit()
```

### C++/CLI

```cpp
System.int TemperatureEndEdit();
```

### Return Value

Error as defined in [swsTemperatureEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTemperatureEndEditError_e.html)

## VBA Syntax

See [CWTemperature::TemperatureEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTemperature~TemperatureEndEdit.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)

## Remarks

You must call [ICWTemperature::TemperatureBeginEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWTemperature~TemperatureBeginEdit.html) to start editing the temperature. To end editing the temperature, you must call this method. Changes are not applied unless you call both methods.

## See Also

[ICWTemperature Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature.html)
[ICWTemperature Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTemperature_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
