---
title: "SetSimulationOptionToggle Method (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "SetSimulationOptionToggle"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~SetSimulationOptionToggle.html"
---

# SetSimulationOptionToggle Method (ICWModelDoc)

Sets the boolean value for the specified user preference.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSimulationOptionToggle( _
   ByVal NUserPreferenceValue As System.Integer, _
   ByVal BValue As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWModelDoc
Dim NUserPreferenceValue As System.Integer
Dim BValue As System.Boolean
Dim value As System.Boolean

value = instance.SetSimulationOptionToggle(NUserPreferenceValue, BValue)
```

### C#

```csharp
System.bool SetSimulationOptionToggle(
   System.int NUserPreferenceValue,
   System.bool BValue
)
```

### C++/CLI

```cpp
System.bool SetSimulationOptionToggle(
   System.int NUserPreferenceValue,
   System.bool BValue
)
```

### Parameters

- `NUserPreferenceValue`: User preference as defined by [swsUserPreferenceToggle_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUserPreferenceToggle_e.html)
- `BValue`: Boolean value

### Return Value

True if option successfully set, false if not

## VBA Syntax

See [CWModelDoc::SetSimulationOptionToggle](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~SetSimulationOptionToggle.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)
[ICWModelDoc::GetSimulationOptionToggle Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~GetSimulationOptionToggle.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
