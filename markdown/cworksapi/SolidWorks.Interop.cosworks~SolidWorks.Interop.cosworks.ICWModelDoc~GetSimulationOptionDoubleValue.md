---
title: "GetSimulationOptionDoubleValue Method (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "GetSimulationOptionDoubleValue"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~GetSimulationOptionDoubleValue.html"
---

# GetSimulationOptionDoubleValue Method (ICWModelDoc)

Gets the double value for the specified user preference.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSimulationOptionDoubleValue( _
   ByVal NUserPreferenceValue As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWModelDoc
Dim NUserPreferenceValue As System.Integer
Dim value As System.Double

value = instance.GetSimulationOptionDoubleValue(NUserPreferenceValue)
```

### C#

```csharp
System.double GetSimulationOptionDoubleValue(
   System.int NUserPreferenceValue
)
```

### C++/CLI

```cpp
System.double GetSimulationOptionDoubleValue(
   System.int NUserPreferenceValue
)
```

### Parameters

- `NUserPreferenceValue`: User preference as defined by [swsUserPreferenceDoubleValue_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUserPreferenceDoubleValue_e.html)

### Return Value

Double value

## VBA Syntax

See [CWModelDoc::GetSimulationOptionDoubleValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~GetSimulationOptionDoubleValue.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)
[ICWModelDoc::SetSimulationOptionDoubleValue Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~SetSimulationOptionDoubleValue.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
