---
title: "HeatPowerBeginEdit Method (ICWHeatPower)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatPower"
member: "HeatPowerBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower~HeatPowerBeginEdit.html"
---

# HeatPowerBeginEdit Method (ICWHeatPower)

Starts editing heat power.

## Syntax

### Visual Basic (Declaration)

```vb
Sub HeatPowerBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatPower

instance.HeatPowerBeginEdit()
```

### C#

```csharp
void HeatPowerBeginEdit()
```

### C++/CLI

```cpp
void HeatPowerBeginEdit();
```

## VBA Syntax

See [CWHeatPower::HeatPowerBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatPower~HeatPowerBeginEdit.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)

## Remarks

To start editing heat power, you must call this method. You must call [ICWHeatPower::HeatPowerBeginEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWHeatPower~HeatPowerEndEdit.html) to end editing heat power. Changes are not applied unless you call both methods.

## See Also

[ICWHeatPower Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower.html)
[ICWHeatPower Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatPower_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
