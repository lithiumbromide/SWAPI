---
title: "GetResultsProbeManager Method (ICWPlot)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPlot"
member: "GetResultsProbeManager"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot~GetResultsProbeManager.html"
---

# GetResultsProbeManager Method (ICWPlot)

Gets the results probe for this plot.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetResultsProbeManager( _
   ByRef ErrorCode As System.Integer _
) As CWResultsProbeManager
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPlot
Dim ErrorCode As System.Integer
Dim value As CWResultsProbeManager

value = instance.GetResultsProbeManager(ErrorCode)
```

### C#

```csharp
CWResultsProbeManager GetResultsProbeManager(
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
CWResultsProbeManager^ GetResultsProbeManager(
   [Out] System.int ErrorCode
)
```

### Parameters

- `ErrorCode`: Error code as defined in [swsResultPlotErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsResultPlotErrorCode_e.html)

### Return Value

[ICWResultsProbeManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResultsProbeManager.html)

## VBA Syntax

See [CWPlot::GetResultsProbeManager](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPlot~GetResultsProbeManager.html).

## Examples

See the [ICWResultsProbeManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResultsProbeManager.html) examples.

## See Also

[ICWPlot Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot.html)
[ICWPlot Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPlot_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
