---
title: "AddRadiation Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddRadiation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddRadiation.html"
---

# AddRadiation Method (ICWLoadsAndRestraintsManager)

Creates a radiation load for thermal studies.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddRadiation( _
   ByVal NRadType As System.Integer, _
   ByVal DispArray As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWRadiation
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim NRadType As System.Integer
Dim DispArray As System.Object
Dim ErrorCode As System.Integer
Dim value As CWRadiation

value = instance.AddRadiation(NRadType, DispArray, ErrorCode)
```

### C#

```csharp
CWRadiation AddRadiation(
   System.int NRadType,
   System.object DispArray,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWRadiation^ AddRadiation(
   System.int NRadType,
   System.Object^ DispArray,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NRadType`: Type of radiation as defined in [swsRadiationType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRadiationType_e.html)
- `DispArray`: Array of faces or shell edges to which to apply radiation
- `ErrorCode`: Error as defined in [swsRadiationError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsRadiationError_e.html)

### Return Value

[Radiation](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWRadiation.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddRadiation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddRadiation.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)

## Remarks

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
