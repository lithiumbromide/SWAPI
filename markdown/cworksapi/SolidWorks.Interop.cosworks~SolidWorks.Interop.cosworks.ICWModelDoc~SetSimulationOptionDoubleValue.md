---
title: "SetSimulationOptionDoubleValue Method (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "SetSimulationOptionDoubleValue"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~SetSimulationOptionDoubleValue.html"
---

# SetSimulationOptionDoubleValue Method (ICWModelDoc)

Sets the double value for the specified user preference.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSimulationOptionDoubleValue( _
   ByVal NUserPreferenceValue As System.Integer, _
   ByVal DVal As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWModelDoc
Dim NUserPreferenceValue As System.Integer
Dim DVal As System.Double
Dim value As System.Boolean

value = instance.SetSimulationOptionDoubleValue(NUserPreferenceValue, DVal)
```

### C#

```csharp
System.bool SetSimulationOptionDoubleValue(
   System.int NUserPreferenceValue,
   System.double DVal
)
```

### C++/CLI

```cpp
System.bool SetSimulationOptionDoubleValue(
   System.int NUserPreferenceValue,
   System.double DVal
)
```

### Parameters

- `NUserPreferenceValue`: User preference as defined by [swsUserPreferenceDoubleValue_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUserPreferenceDoubleValue_e.html)
- `DVal`: Double value

### Return Value

True if option successfully set, false if not

## VBA Syntax

See [CWModelDoc::SetSimulationOptionDoubleValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~SetSimulationOptionDoubleValue.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)
[ICWModelDoc::GetSimulationOptionDoubleValue Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~GetSimulationOptionDoubleValue.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
