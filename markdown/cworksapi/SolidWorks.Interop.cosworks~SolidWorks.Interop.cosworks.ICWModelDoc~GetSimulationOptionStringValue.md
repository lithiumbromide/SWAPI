---
title: "GetSimulationOptionStringValue Method (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "GetSimulationOptionStringValue"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~GetSimulationOptionStringValue.html"
---

# GetSimulationOptionStringValue Method (ICWModelDoc)

Gets the string value for the specified user preference.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSimulationOptionStringValue( _
   ByVal NUserPreferenceValue As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWModelDoc
Dim NUserPreferenceValue As System.Integer
Dim value As System.String

value = instance.GetSimulationOptionStringValue(NUserPreferenceValue)
```

### C#

```csharp
System.string GetSimulationOptionStringValue(
   System.int NUserPreferenceValue
)
```

### C++/CLI

```cpp
System.String^ GetSimulationOptionStringValue(
   System.int NUserPreferenceValue
)
```

### Parameters

- `NUserPreferenceValue`: User preference as defined by [swsUserPreferenceStringValue_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUserPreferenceStringValue_e.html)

### Return Value

String value

## VBA Syntax

See [CWModelDoc::GetSimulationOptionStringValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~GetSimulationOptionStringValue.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)
[ICWModelDoc::SetSimulationOptionStringValue Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~SetSimulationOptionStringValue.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
