---
title: "SavePlotsAseDrawings Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "SavePlotsAseDrawings"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SavePlotsAseDrawings.html"
---

# SavePlotsAseDrawings Method (ICWResults)

Saves the specified results plot as an eDrawings file with the specified name in the specified location.

## Syntax

### Visual Basic (Declaration)

```vb
Function SavePlotsAseDrawings( _
   ByVal SFileLocation As System.String, _
   ByVal SFileName As System.String, _
   ByVal SPlotName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim SFileLocation As System.String
Dim SFileName As System.String
Dim SPlotName As System.String
Dim value As System.Integer

value = instance.SavePlotsAseDrawings(SFileLocation, SFileName, SPlotName)
```

### C#

```csharp
System.int SavePlotsAseDrawings(
   System.string SFileLocation,
   System.string SFileName,
   System.string SPlotName
)
```

### C++/CLI

```cpp
System.int SavePlotsAseDrawings(
   System.String^ SFileLocation,
   System.String^ SFileName,
   System.String^ SPlotName
)
```

### Parameters

- `SFileLocation`: Path where to save the eDrawings file
- `SFileName`: Name of eDrawings file to save
- `SPlotName`: Plot to save as an eDrawings file (see **Remarks**)

### Return Value

Error as defined by [swsSaveeDrawingsErrorCode_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSaveeDrawingsErrorCode_e.html)

## VBA Syntax

See [CWResults::SavePlotsAseDrawings](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~SavePlotsAseDrawings.html).

## Examples

[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VBA)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VB.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (VB.NET)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_VBNET.htm)
[Apply Thermostat-controlled Heat Power for Transient Thermal Study (C#)](Apply_Thermostat-controlled_Heat_Power_for_Transient_Thermal_Study_Example_CSharp.htm)

## Remarks

Call [ICWResults::GetPlotNames](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotNames.html) to populate SPlotName.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetPlotCount Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotCount.html)
[ICWResults::ActivatePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~ActivatePlot.html)
[ICWResults::AddIsoClippingToPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~AddIsoClippingToPlot.html)
[ICWResults::CreatePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreatePlot.html)
[ICWResults::CreateResultsEquationPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateResultsEquationPlot.html)
[ICWResults::GetPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlot.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
