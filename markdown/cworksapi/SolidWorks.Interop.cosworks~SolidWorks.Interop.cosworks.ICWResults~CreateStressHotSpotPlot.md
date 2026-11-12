---
title: "CreateStressHotSpotPlot Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "CreateStressHotSpotPlot"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateStressHotSpotPlot.html"
---

# CreateStressHotSpotPlot Method (ICWResults)

Creates a stress hot spot plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateStressHotSpotPlot( _
   ByVal BIsolateHotSpots As System.Boolean, _
   ByVal BValueByNodes As System.Boolean, _
   ByRef ErrorCode As System.Integer _
) As CWPlot
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim BIsolateHotSpots As System.Boolean
Dim BValueByNodes As System.Boolean
Dim ErrorCode As System.Integer
Dim value As CWPlot

value = instance.CreateStressHotSpotPlot(BIsolateHotSpots, BValueByNodes, ErrorCode)
```

### C#

```csharp
CWPlot CreateStressHotSpotPlot(
   System.bool BIsolateHotSpots,
   System.bool BValueByNodes,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWPlot^ CreateStressHotSpotPlot(
   System.bool BIsolateHotSpots,
   System.bool BValueByNodes,
   [Out] System.int ErrorCode
)
```

### Parameters

- `BIsolateHotSpots`: True to isolate stress hot spots, false to not
- `BValueByNodes`: True to plot node values, false to plot element values
- `ErrorCode`: Error code as defined in [swsStressHotSpotPlotError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsStressHotSpotPlotError_e.html)

### Return Value

[ICWPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)

## VBA Syntax

See [CWResults::CreateStressHotSpotPlot](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~CreateStressHotSpotPlot.html).

## Examples

See the [ICWStaticStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html) examples.

## Remarks

Before calling this method, you must call [ICWResults::RunStressHotSpotDiagnostics](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~RunStressHotSpotDiagnostics.html).

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)
[ICWResults::GetDetectedHotSpotElements Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDetectedHotSpotElements.html)
[ICWResults::GetDetectedHotSpotNodes Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDetectedHotSpotNodes.html)
[ICWResults::CreatePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreatePlot.html)
[ICWResults::CreateResultsEquationPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateResultsEquationPlot.html)
[ICWResults::ActivatePlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~ActivatePlot.html)
[ICWResults::GetPlot Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetPlot.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
