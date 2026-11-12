---
title: "HeatPowerEndEdit Method (ICWHeatPower)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatPower"
member: "HeatPowerEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~HeatPowerEndEdit.html"
---

# HeatPowerEndEdit Method (ICWHeatPower)

Ends editing heat power.

## Syntax

### Visual Basic (Declaration)

```vb
Function HeatPowerEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatPower
Dim value As System.Integer

value = instance.HeatPowerEndEdit()
```

### C#

```csharp
System.int HeatPowerEndEdit()
```

### C++/CLI

```cpp
System.int HeatPowerEndEdit();
```

### Return Value

Error as defined in [swsHeatPowerEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsHeatPowerEndEditError_e.html)

## VBA Syntax

See [CWHeatPower::HeatPowerEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatPower~HeatPowerEndEdit.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)

## Remarks

You must call [ICWHeatPower::HeatPowerBeginEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWHeatPower~HeatPowerBeginEdit.html) to start editing heat power. To ends editing heat power, you must call this method. Changes are not applied unless you call both methods.

## See Also

[ICWHeatPower Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower.html)
[ICWHeatPower Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
