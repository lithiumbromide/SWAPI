---
title: "CreatePlot Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "CreatePlot"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreatePlot.html"
---

# CreatePlot Method (ICWResults)

Creates the specified plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreatePlot( _
   ByVal NResultType As System.Integer, _
   ByVal NComponent As System.Integer, _
   ByVal NUnits As System.Integer, _
   ByVal BValueByElem As System.Boolean, _
   ByRef ErrorCode As System.Integer _
) As CWPlot
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NResultType As System.Integer
Dim NComponent As System.Integer
Dim NUnits As System.Integer
Dim BValueByElem As System.Boolean
Dim ErrorCode As System.Integer
Dim value As CWPlot

value = instance.CreatePlot(NResultType, NComponent, NUnits, BValueByElem, ErrorCode)
```

### C#

```csharp
CWPlot CreatePlot(
   System.int NResultType,
   System.int NComponent,
   System.int NUnits,
   System.bool BValueByElem,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWPlot^ CreatePlot(
   System.int NResultType,
   System.int NComponent,
   System.int NUnits,
   System.bool BValueByElem,
   [Out] System.int ErrorCode
)
```

### Parameters

- `NResultType`: Type of results plot as defined by [swsPlotResultTypes_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsPlotResultTypes_e.html) (see **Remarks**)
- `NComponent`: Component to plot (see **Remarks**)
- `NUnits`: Units as appropriate to NComponent (see **Remarks**)
- `BValueByElem`: True to plot element values, false to plot node values
- `ErrorCode`: Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

### Return Value

[ICWPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)

## VBA Syntax

See [CWResults::CreatePlot](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~CreatePlot.html).

## Examples

[Create Plots for Static Study (VBA)](Create_Plots_for_Static_Study_Example_VB.htm)
[Create Plots for Static Study (VB.NET)](Create_Plots_for_Static_Study_Example_VBNET.htm)
[Create Plots for Static Study (C#)](Create_Plots_for_Static_Study_Example_CSharp.htm)

## Remarks

| If NResultType is swsPlotResultTypes_e... | Then NComponent contains the component to plot as defined by... | And NUnits contains the units as defined by... |
| --- | --- | --- |
| swsResultAcceleration | swsAccelerationComponent_e | swsAccelerationUnit_e |
| swsResultBeamDiagram | swsBeamForceType_e | swsForceUnit_e |
| swsResultBeamStress | swsBeamStressType_e | swsStrengthUnit_e |
| swsResultDesignInsight | N/A | N/A |
| swsResultDisplacementOrAmplitude | swsDisplacementComponent_e (Displacement) swsFrequencyBucklingResultDisplacementComponentTypes_e (Amplitude for frequency and buckling studies) | swsLinearUnit_e (displacement) or swsForceUnit_e (reaction force) |
| swsResultEdgeWeldConnector | N/A | N/A |
| swsResultFactorOfSafety | swsFOS_NonCompositeCriterion_e (Non-composite shells) swsFOS_CompositeCriterion_e (Composite shells) | N/A |
| swsResultFatigue | swsFatigueComponent_e | N/A |
| swsResultPinBoltBearing | N/A | N/A |
| swsResultStrain | swsStrainComponent_e | swsStrengthUnit_e |
| swsResultEquivalentStress* | N/A | swsStrengthUnit_e |
| swsResultStress | swsStressComponent_e | swsStrengthUnit_e |
| swsResultThermal | swsThermalComponent_e | swsTemperatureUnit_e |
| swsResultVelocity | swsVelocityComponent_e | swsVelocityUnit_e |

* The following conditions are required to create an equivalent stress plot:

- Mixed mesh model with beams and solids/shells
- Dynamic study
- **Nodal von Mises stress only (Faster)** option is chosen in **Results Options > Quantity** to calculate stress results

**NOTE:** After calling this method to create a plot of linear dynamic, frequency, or buckling studies, call [ICWPlot::SetModeShape](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~SetModeShape.html) to set the mode shape number of the plot.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::ActivatePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~ActivatePlot.html)
[ICWResults::DeletePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~DeletePlot.html)
[ICWResults::GetPlotColorOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotColorOptions.html)
[ICWResults::GetPlotCount Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotCount.html)
[ICWResults::GetPlotDisplayOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotDisplayOptions.html)
[ICWResults::GetPlotPositionFormatOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotPositionFormatOptions.html)
[ICWResults::GetPlotSettings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotSettings.html)
[ICWResults::SavePlotsAseDrawings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SavePlotsAseDrawings.html)
[ICWResults::SetPlotColorOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotColorOptions.html)
[ICWResults::SetPlotDisplayOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotDisplayOptions.html)
[ICWResults::SetPlotPositionFormatOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotPositionFormatOptions.html)
[ICWResults::SetPlotSettings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotSettings.html)
[ICWResults::AddIsoClippingToPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~AddIsoClippingToPlot.html)
[ICWResults::GetPlotNames Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotNames.html)
[ICWResults::GetPlotSettingsOptionForHiddenAndExcludedBody Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotSettingsOptionForHiddenAndExcludedBody.html)
[ICWResults::SetPlotSettingsOptionForHiddenAndExcludedBody Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotSettingsOptionForHiddenAndExcludedBody.html)
[ICWResults::CreateResultsEquationPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateResultsEquationPlot.html)
[ICWPlot::SetComponentUnitAndValueByElem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~SetComponentUnitAndValueByElem.html)
[ICWResults::GetPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlot.html)
[ICWResults::CreateStressHotSpotPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateStressHotSpotPlot.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
