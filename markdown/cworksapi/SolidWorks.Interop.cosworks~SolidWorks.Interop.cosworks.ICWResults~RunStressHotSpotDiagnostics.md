---
title: "RunStressHotSpotDiagnostics Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "RunStressHotSpotDiagnostics"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~RunStressHotSpotDiagnostics.html"
---

# RunStressHotSpotDiagnostics Method (ICWResults)

Obsolete. Superseded by [ICWResults::RunStressHotSpotDiagnosticsAndDetectSingularities](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~RunStressHotSpotDiagnosticsAndDetectSingularities.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function RunStressHotSpotDiagnostics( _
   ByVal NSensitivityFactor As System.Integer, _
   ByVal BRunForNodes As System.Boolean, _
   ByRef BFoundHotSpots As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NSensitivityFactor As System.Integer
Dim BRunForNodes As System.Boolean
Dim BFoundHotSpots As System.Boolean
Dim value As System.Integer

value = instance.RunStressHotSpotDiagnostics(NSensitivityFactor, BRunForNodes, BFoundHotSpots)
```

### C#

```csharp
System.int RunStressHotSpotDiagnostics(
   System.int NSensitivityFactor,
   System.bool BRunForNodes,
   out System.bool BFoundHotSpots
)
```

### C++/CLI

```cpp
System.int RunStressHotSpotDiagnostics(
   System.int NSensitivityFactor,
   System.bool BRunForNodes,
   [Out] System.bool BFoundHotSpots
)
```

### Parameters

- `NSensitivityFactor`: 5 <= Highest equivalent strain percent <= 100
- `BRunForNodes`: True to run for nodes, false to not (see **Remarks**)
- `BFoundHotSpots`: True if stress hot spots are found, false if not (see **Remarks**)

### Return Value

Error code as defined in [swsRunStressHotSpotDiagnosticsError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRunStressHotSpotDiagnosticsError_e.html)

## VBA Syntax

See [CWResults::RunStressHotSpotDiagnostics](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~RunStressHotSpotDiagnostics.html).

## Remarks

After calling this method, you can call:

- [ICWResults::CreateStressHotSpotPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateStressHotSpotPlot.html) and [ICWResults::GetDetectedHotSpotElements](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDetectedHotSpotElements.html) if BRunForNodes is false.
- [ICWResults::GetDetectedHotSpotNodes](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDetectedHotSpotNodes.html) if BRunForNodes is true.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
