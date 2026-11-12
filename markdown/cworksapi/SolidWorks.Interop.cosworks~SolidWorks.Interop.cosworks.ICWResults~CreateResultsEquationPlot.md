---
title: "CreateResultsEquationPlot Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "CreateResultsEquationPlot"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateResultsEquationPlot.html"
---

# CreateResultsEquationPlot Method (ICWResults)

Creates a plot of the specified results equation.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateResultsEquationPlot( _
   ByVal SResultsEquation As System.String, _
   ByVal SLegendTitle As System.String, _
   ByVal BValueByElem As System.Boolean, _
   ByVal NUnits As System.Integer, _
   ByVal NStepNumber As System.Integer, _
   ByVal NShellOptions As System.Integer, _
   ByRef ErrorCode As System.Integer _
) As CWPlot
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim SResultsEquation As System.String
Dim SLegendTitle As System.String
Dim BValueByElem As System.Boolean
Dim NUnits As System.Integer
Dim NStepNumber As System.Integer
Dim NShellOptions As System.Integer
Dim ErrorCode As System.Integer
Dim value As CWPlot

value = instance.CreateResultsEquationPlot(SResultsEquation, SLegendTitle, BValueByElem, NUnits, NStepNumber, NShellOptions, ErrorCode)
```

### C#

```csharp
CWPlot CreateResultsEquationPlot(
   System.string SResultsEquation,
   System.string SLegendTitle,
   System.bool BValueByElem,
   System.int NUnits,
   System.int NStepNumber,
   System.int NShellOptions,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWPlot^ CreateResultsEquationPlot(
   System.String^ SResultsEquation,
   System.String^ SLegendTitle,
   System.bool BValueByElem,
   System.int NUnits,
   System.int NStepNumber,
   System.int NShellOptions,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SResultsEquation`: Results equation
- `SLegendTitle`: Title of the plot
- `BValueByElem`: True to plot element values, false to plot node values
- `NUnits`: Units as defined in [swsUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnit_e.html)
- `NStepNumber`: Number of solution step to plot
- `NShellOptions`: Shell face as defined in [swsShellFace_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsShellFace_e.html); valid only for shell and mixed mesh models
- `ErrorCode`: Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

### Return Value

[ICWPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)

## VBA Syntax

See [CWResults::CreateResultsEquationPlot](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~CreateResultsEquationPlot.html).

## Examples

[Create Results Equation Plot (VBA)](Create_Results_Equation_Plot_Example_VB.htm)
[Create Results Equation Plot (VB.NET)](Create_Results_Equation_Plot_Example_VBNET.htm)
[Create Results Equation Plot (C#)](Create_Results_Equation_Plot_Example_CSharp.htm)

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::ActivatePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~ActivatePlot.html)
[ICWResults::AddIsoClippingToPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~AddIsoClippingToPlot.html)
[ICWResults::CreatePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreatePlot.html)
[ICWResults::DeletePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~DeletePlot.html)
[ICWResults::GetPlotColorOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotColorOptions.html)
[ICWResults::GetPlotCount Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotCount.html)
[ICWResults::GetPlotDisplayOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotDisplayOptions.html)
[ICWResults::GetPlotNames Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotNames.html)
[ICWResults::GetPlotPositionFormatOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotPositionFormatOptions.html)
[ICWResults::GetPlotSettings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotSettings.html)
[ICWResults::GetPlotSettingsOptionForHiddenAndExcludedBody Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotSettingsOptionForHiddenAndExcludedBody.html)
[ICWResults::SavePlotsAseDrawings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SavePlotsAseDrawings.html)
[ICWResults::SetPlotColorOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotColorOptions.html)
[ICWResults::SetPlotDisplayOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotDisplayOptions.html)
[ICWResults::SetPlotPositionFormatOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotPositionFormatOptions.html)
[ICWResults::SetPlotSettings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotSettings.html)
[ICWResults::SetPlotSettingsOptionForHiddenAndExcludedBody Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotSettingsOptionForHiddenAndExcludedBody.html)
[ICWResults::GetMinMaxResultsEquationValues Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetMinMaxResultsEquationValues.html)
[ICWResults::GetResultsEquationValuesForEntities Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetResultsEquationValuesForEntities.html)
[ICWResults::GetPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlot.html)
[ICWResults::CreateStressHotSpotPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateStressHotSpotPlot.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
