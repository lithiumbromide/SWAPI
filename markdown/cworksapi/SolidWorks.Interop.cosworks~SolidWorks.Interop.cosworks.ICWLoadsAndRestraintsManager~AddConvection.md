---
title: "AddConvection Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "AddConvection"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~AddConvection.html"
---

# AddConvection Method (ICWLoadsAndRestraintsManager)

Creates a convection load for thermal studies.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddConvection( _
   ByVal DispArray As System.Object, _
   ByRef ErrorCode As System.Integer _
) As CWConvection
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim DispArray As System.Object
Dim ErrorCode As System.Integer
Dim value As CWConvection

value = instance.AddConvection(DispArray, ErrorCode)
```

### C#

```csharp
CWConvection AddConvection(
   System.object DispArray,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWConvection^ AddConvection(
   System.Object^ DispArray,
   [Out] System.int ErrorCode
)
```

### Parameters

- `DispArray`: Array of faces or shell edges to apply convection
- `ErrorCode`: Error as defined in [swsConvectionError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsConvectionError_e.html)

### Return Value

[Convection](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWConvection.html)

## VBA Syntax

See [CWLoadsAndRestraintsManager::AddConvection](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~AddConvection.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
