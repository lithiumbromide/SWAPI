---
title: "GetSimulationOptionIntegerValue Method (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "GetSimulationOptionIntegerValue"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~GetSimulationOptionIntegerValue.html"
---

# GetSimulationOptionIntegerValue Method (ICWModelDoc)

Gets the integer value for the specified user preference.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSimulationOptionIntegerValue( _
   ByVal UserPreferenceValue As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWModelDoc
Dim UserPreferenceValue As System.Integer
Dim value As System.Integer

value = instance.GetSimulationOptionIntegerValue(UserPreferenceValue)
```

### C#

```csharp
System.int GetSimulationOptionIntegerValue(
   System.int UserPreferenceValue
)
```

### C++/CLI

```cpp
System.int GetSimulationOptionIntegerValue(
   System.int UserPreferenceValue
)
```

### Parameters

- `UserPreferenceValue`: User preference as defined by [swsUserPreferenceIntegerValue_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUserPreferenceIntegerValue_e.html)

### Return Value

Integer value (see **Remarks**)

## VBA Syntax

See [CWModelDoc::GetSimulationOptionIntegerValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~GetSimulationOptionIntegerValue.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)

## Remarks

Values for colors are defined in [swsWindowsBasicColors_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsWindowsBasicColors_e.html).

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)
[ICWModelDoc::SetSimulationOptionIntegerValue Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~SetSimulationOptionIntegerValue.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
