---
title: "AddDefaultThermalStudyPlot Method (ICWModelDoc)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWModelDoc"
member: "AddDefaultThermalStudyPlot"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~AddDefaultThermalStudyPlot.html"
---

# AddDefaultThermalStudyPlot Method (ICWModelDoc)

Specifies a default thermal study result plot for the active document.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddDefaultThermalStudyPlot( _
   ByVal NResultComponent As System.Integer, _
   ByVal BTransient As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWModelDoc
Dim NResultComponent As System.Integer
Dim BTransient As System.Boolean
Dim value As System.Integer

value = instance.AddDefaultThermalStudyPlot(NResultComponent, BTransient)
```

### C#

```csharp
System.int AddDefaultThermalStudyPlot(
   System.int NResultComponent,
   System.bool BTransient
)
```

### C++/CLI

```cpp
System.int AddDefaultThermalStudyPlot(
   System.int NResultComponent,
   System.bool BTransient
)
```

### Parameters

- `NResultComponent`: Type of thermal study result to plot as defined by [swsThermalResultComponentTypes_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsThermalResultComponentTypes_e.html)
- `BTransient`: True if transient, false if steady state (see **Remarks**)

### Return Value

Error code as defined by [swsAddDefaultThermalStudyPlotResultError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsAddDefaultThermalStudyPlotResultError_e.html)

## VBA Syntax

See [CWModelDoc::AddDefaultThermalStudyPlot](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWModelDoc~AddDefaultThermalStudyPlot.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)

## Remarks

If BTransient is true, this plot is for a transient thermal study in which an initial temperature profile is defined for the thermal load.

## See Also

[ICWModelDoc Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc.html)
[ICWModelDoc Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc_members.html)
[ICWModelDoc::DeleteAllDefaultThermalStudyPlots Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~DeleteAllDefaultThermalStudyPlots.html)
[ICWModelDoc::DeleteDefaultThermalStudyPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWModelDoc~DeleteDefaultThermalStudyPlot.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
