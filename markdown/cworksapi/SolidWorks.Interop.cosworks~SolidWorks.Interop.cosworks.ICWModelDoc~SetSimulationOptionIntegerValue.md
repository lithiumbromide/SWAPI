---
title: "SetSimulationOptionIntegerValue Method (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "SetSimulationOptionIntegerValue"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~SetSimulationOptionIntegerValue.html"
---

# SetSimulationOptionIntegerValue Method (ICWModelDoc)

Sets the integer value for the specified user preference.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSimulationOptionIntegerValue( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal Value As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWModelDoc
Dim UserPreferenceValue As System.Integer
Dim Value As System.Integer
Dim value As System.Boolean

value = instance.SetSimulationOptionIntegerValue(UserPreferenceValue, Value)
```

### C#

```csharp
System.bool SetSimulationOptionIntegerValue(
   System.int UserPreferenceValue,
   System.int Value
)
```

### C++/CLI

```cpp
System.bool SetSimulationOptionIntegerValue(
   System.int UserPreferenceValue,
   System.int Value
)
```

### Parameters

- `UserPreferenceValue`: User preference as defined by [swsUserPreferenceIntegerValue_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUserPreferenceIntegerValue_e.html)
- `Value`: Integer value (see **Remarks**)

### Return Value

True if option successfully set, false if not

## VBA Syntax

See [CWModelDoc::SetSimulationOptionIntegerValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~SetSimulationOptionIntegerValue.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)

## Remarks

To set color options you can either:

1. Locate the color you want, for example swsAqua, from [swsWindowsBasicColors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsWindowsBasicColors_e.html).
2. Call this method, specifying Value with the integer value for swsAqua, 16776960, e.g., ICWModelDoc::SetSimulationOptionIntegerValue(swsUserPreferenceIntegerValue_e.swsPlotShowHiddenBodyTranslucentSingleColor, 16776960).

-or-

1. Select a color from [http://cloford.com/resources/colours/500col.htm](http://cloford.com/resources/colours/500col.htm) (e.g., #FF0000 is the hexadecimal for Red 1).
2. Reverse the hexadecimal value of the selected color (e.g., #0000FF is the reverse hexadecimal for Red 1).
3. Call [ICWModelDoc::SetSimulationOptionIntegerValue](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWModelDoc~SetSimulationOptionIntegerValue.html)(swsUserPreferenceIntegerValue_e.`option`, &h`color_reverse_hexadecimal`), e.g., ICWModelDoc::SetSimulationOptionIntegerValue(swsUserPreferenceIntegerValue_e.swsPlotShowHiddenBodyTranslucentSingleColor, &h0000ff).

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)
[ICWModelDoc::GetSimulationOptionIntegerValue Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~GetSimulationOptionIntegerValue.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
