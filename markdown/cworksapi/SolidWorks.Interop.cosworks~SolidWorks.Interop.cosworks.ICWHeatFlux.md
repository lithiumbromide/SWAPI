---
title: "ICWHeatFlux Interface"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWHeatFlux"
member: ""
kind: "interface"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux.html"
---

# ICWHeatFlux Interface

Allows access to the heat flux object used for steady state and transient thermal studies only.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICWHeatFlux
```

### Visual Basic (Usage)

```vb
Dim instance As ICWHeatFlux
```

### C#

```csharp
public interface ICWHeatFlux
```

### C++/CLI

```cpp
public interface class ICWHeatFlux
```

## VBA Syntax

See [CWHeatFlux](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWHeatFlux.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)

## Remarks

Heat flux can vary with time for transient studies. You can control the heat power by a thermostat.

## Accessors

[ICWLoadsAndRestraintsManager::AddHeatFlux](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWLoadsAndRestraintsManager~AddHeatFlux.html)

## See Also

[ICWHeatFlux Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWHeatFlux_members.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
