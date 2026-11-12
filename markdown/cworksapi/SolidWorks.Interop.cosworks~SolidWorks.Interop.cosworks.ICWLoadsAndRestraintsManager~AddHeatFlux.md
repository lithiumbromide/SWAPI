---
title: "AddHeatFlux Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddHeatFlux"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddHeatFlux.html"
---

# AddHeatFlux Method (ICWLoadsAndRestraintsManager)

Creates a heat flux load for thermal studies.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddHeatFlux( _
   ByVal DispArray As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWHeatFlux
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim DispArray As System.Object
Dim ErrorCode As System.Integer
Dim value As CWHeatFlux

value = instance.AddHeatFlux(DispArray, ErrorCode)
```

### C#

```csharp
CWHeatFlux AddHeatFlux(
   System.object DispArray,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWHeatFlux^ AddHeatFlux(
   System.Object^ DispArray,
   [Out] System.int ErrorCode
)
```

### Parameters

- `DispArray`: Array of entities (faces or shell edges) to which to apply heat flux
- `ErrorCode`: Error as defined in [swsHeatFluxError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsHeatFluxError_e.html)

### Return Value

[Heat flux](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWHeatFlux.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddHeatFlux](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddHeatFlux.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
