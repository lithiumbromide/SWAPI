---
title: "SetSimulationOptionStringValue Method (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "SetSimulationOptionStringValue"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~SetSimulationOptionStringValue.html"
---

# SetSimulationOptionStringValue Method (ICWModelDoc)

Sets the string value for the specified user preference.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSimulationOptionStringValue( _
   ByVal NUserPreferenceValue As System.Integer, _
   ByVal StringVal As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWModelDoc
Dim NUserPreferenceValue As System.Integer
Dim StringVal As System.String
Dim value As System.Boolean

value = instance.SetSimulationOptionStringValue(NUserPreferenceValue, StringVal)
```

### C#

```csharp
System.bool SetSimulationOptionStringValue(
   System.int NUserPreferenceValue,
   System.string StringVal
)
```

### C++/CLI

```cpp
System.bool SetSimulationOptionStringValue(
   System.int NUserPreferenceValue,
   System.String^ StringVal
)
```

### Parameters

- `NUserPreferenceValue`: User preference as defined by [swsUserPreferenceStringValue_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUserPreferenceStringValue_e.html)
- `StringVal`: String value

### Return Value

True if option successfully set, false if not

## VBA Syntax

See [CWModelDoc::SetSimulationOptionStringValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~SetSimulationOptionStringValue.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)
[ICWModelDoc::GetSimulationOptionStringValue Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~GetSimulationOptionStringValue.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
