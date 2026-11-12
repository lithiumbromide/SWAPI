---
title: "GetSimulationOptionToggle Method (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "GetSimulationOptionToggle"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~GetSimulationOptionToggle.html"
---

# GetSimulationOptionToggle Method (ICWModelDoc)

Gets the boolean value for the specified user preference.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSimulationOptionToggle( _
   ByVal NUserPreferenceValue As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWModelDoc
Dim NUserPreferenceValue As System.Integer
Dim value As System.Boolean

value = instance.GetSimulationOptionToggle(NUserPreferenceValue)
```

### C#

```csharp
System.bool GetSimulationOptionToggle(
   System.int NUserPreferenceValue
)
```

### C++/CLI

```cpp
System.bool GetSimulationOptionToggle(
   System.int NUserPreferenceValue
)
```

### Parameters

- `NUserPreferenceValue`: User preference as defined by [swsUserPreferenceToggle_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUserPreferenceToggle_e.html)

### Return Value

Boolean value

## VBA Syntax

See [CWModelDoc::GetSimulationOptionToggle](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~GetSimulationOptionToggle.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)
[ICWModelDoc::SetSimulationOptionToggle Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~SetSimulationOptionToggle.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
