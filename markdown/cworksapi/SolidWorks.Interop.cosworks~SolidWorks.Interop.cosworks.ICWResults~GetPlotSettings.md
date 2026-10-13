---
title: "GetPlotSettings Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "GetPlotSettings"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotSettings.html"
---

# GetPlotSettings Method (ICWResults)

Gets the settings for the specified plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPlotSettings( _
   ByVal SPlotName As System.String, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim SPlotName As System.String
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.GetPlotSettings(SPlotName, ErrorCode)
```

### C#

```csharp
System.object GetPlotSettings(
   System.string SPlotName,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetPlotSettings(
   System.String^ SPlotName,
   [Out] System.int ErrorCode
)
```

### Parameters

- `SPlotName`: Plot name (see **Remarks**)
- `ErrorCode`: Error as defined in [swsResultsError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultsError_e.html)

### Return Value

Array of plot settings (see **Remarks**)

## VBA Syntax

See [CWResults::GetPlotSettings](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~GetPlotSettings.html).

## Examples

[Analyze Part (VBA)](Analyze_Part_Example_VB.htm)
[Analyze Part (VB.NET)](Analyze_Part_Example_VBNET.htm)
[Analyze Part (C#)](Analyze_Part_Example_CSharp.htm)

## Remarks

Call [ICWResults::GetPlotNames](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotNames.html) to populate SPlotName.

The 0-based array contains 11 elements:

| Array element... | Contains... |
| --- | --- |
| 0 | Display option for active fringe plot as defined in swsPlotFringeSettingsOptionValue_e |
| 1 | Display option for model boundary as defined in swsPlotBoundarySettingsOptionValue_e |
| 2 | R[0-255] value for model/mesh color; valid only if array element 1 is not swsPlotBoundarySettingsOptionValue_e.swsPlotBoundaryNone |
| 3 | G[0-255] value for model/mesh color; valid only if array element 1 is not swsPlotBoundarySettingsOptionValue_e.swsPlotBoundaryNone |
| 4 | B[0-255] value for model/mesh color; valid only if array element 1 is not swsPlotBoundarySettingsOptionValue_e.swsPlotBoundaryNone |
| 5 | Boolean; whether to superimpose the undeformed model on the deformed model |
| 6 | Deformed plot translucent color option as defined in swsPlotDeformedShapeOptionSuperImposeValue_e ; valid only if array element 5 is true |
| 7 | R[0-255] value for single translucent color; valid only if array element 5 is true, and array element 6 is swsPlotDeformedShapeOptionSuperImposeValue_e.swsPlotDeformedShapeSuperImposeModel_TranslucentSingleColor |
| 8 | G[0-255] value for single translucent color; valid only if array element 5 is true, and array element 6 is swsPlotDeformedShapeOptionSuperImposeValue_e.swsPlotDeformedShapeSuperImposeModel_TranslucentSingleColor |
| 9 | B[0-255] value for single translucent color; valid only if array element 5 is true, and array element 6is swsPlotDeformedShapeOptionSuperImposeValue_e.swsPlotDeformedShapeSuperImposeModel_TranslucentSingleColor |
| 10 | 0.0 <= Transparency or intensity of the translucent single color or part colors <= 1.0; valid only if array element 5 is true |

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::SetPlotSettings Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~SetPlotSettings.html)
[ICWResults::GetPlotColorOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotColorOptions.html)
[ICWResults::GetPlotCount Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotCount.html)
[ICWResults::GetPlotDisplayOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotDisplayOptions.html)
[ICWResults::GetPlotPositionFormatOptions Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotPositionFormatOptions.html)
[ICWResults::CreatePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreatePlot.html)
[ICWResults::GetPlotSettingsOptionForHiddenAndExcludedBody Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotSettingsOptionForHiddenAndExcludedBody.html)
[ICWResults::GetLegendContourColors Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetLegendContourColors.html)
[ICWResults::CreateResultsEquationPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateResultsEquationPlot.html)
[ICWResults::GetPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlot.html)
[ICWResults::GetPlotDefinition Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlotDefinition.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
