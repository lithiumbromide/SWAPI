---
title: "RunStressHotSpotDiagnosticsAndDetectSingularities Method (ICWResults)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWResults"
member: "RunStressHotSpotDiagnosticsAndDetectSingularities"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~RunStressHotSpotDiagnosticsAndDetectSingularities.html"
---

# RunStressHotSpotDiagnosticsAndDetectSingularities Method (ICWResults)

Detects stress hot spots and singularities.

## Syntax

### Visual Basic (Declaration)

```vb
Function RunStressHotSpotDiagnosticsAndDetectSingularities( _
   ByVal NSensitivityFactor As System.Integer, _
   ByVal BRunForNodes As System.Boolean, _
   ByVal NMeshRefineLevels As System.Integer, _
   ByVal DElemSizeReductionFactor As System.Double, _
   ByVal dGrowthRatio As System.Double, _
   ByVal NResultsRestoreOption As System.Integer, _
   ByRef BFoundHotSpots As System.Boolean, _
   ByRef BFoundSingularities As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWResults
Dim NSensitivityFactor As System.Integer
Dim BRunForNodes As System.Boolean
Dim NMeshRefineLevels As System.Integer
Dim DElemSizeReductionFactor As System.Double
Dim dGrowthRatio As System.Double
Dim NResultsRestoreOption As System.Integer
Dim BFoundHotSpots As System.Boolean
Dim BFoundSingularities As System.Boolean
Dim value As System.Integer

value = instance.RunStressHotSpotDiagnosticsAndDetectSingularities(NSensitivityFactor, BRunForNodes, NMeshRefineLevels, DElemSizeReductionFactor, dGrowthRatio, NResultsRestoreOption, BFoundHotSpots, BFoundSingularities)
```

### C#

```csharp
System.int RunStressHotSpotDiagnosticsAndDetectSingularities(
   System.int NSensitivityFactor,
   System.bool BRunForNodes,
   System.int NMeshRefineLevels,
   System.double DElemSizeReductionFactor,
   System.double dGrowthRatio,
   System.int NResultsRestoreOption,
   out System.bool BFoundHotSpots,
   out System.bool BFoundSingularities
)
```

### C++/CLI

```cpp
System.int RunStressHotSpotDiagnosticsAndDetectSingularities(
   System.int NSensitivityFactor,
   System.bool BRunForNodes,
   System.int NMeshRefineLevels,
   System.double DElemSizeReductionFactor,
   System.double dGrowthRatio,
   System.int NResultsRestoreOption,
   [Out] System.bool BFoundHotSpots,
   [Out] System.bool BFoundSingularities
)
```

### Parameters

- `NSensitivityFactor`: 5 <= Highest equivalent strain percent <= 100 (see **Remarks**)
- `BRunForNodes`: True to run for nodes, false to run for elements (see **Remarks**)
- `NMeshRefineLevels`: 2 <= Mesh refinement level to detect singularities <= 3
- `DElemSizeReductionFactor`: 0.01 <= Element size reduction factor across levels to detect singularities <= 0.9
- `dGrowthRatio`: 1.0 <= Element size growth ratio to detect singularities <= 3.1
- `NResultsRestoreOption`: Results restore option as defined in [swsStressHotSpotResultsRestoreOptions_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsStressHotSpotResultsRestoreOptions_e.html) use after detecting stress hot spots and singularities
- `BFoundHotSpots`: True if stress hot spots are found, false if not
- `BFoundSingularities`: True if singularities are found, false if not

### Return Value

Error code as defined in [swsRunStressHotSpotDiagnosticsError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRunStressHotSpotDiagnosticsError_e.html)

## VBA Syntax

See [CWResults::RunStressHotSpotDiagnosticsAndDetectSingularities](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWResults~RunStressHotSpotDiagnosticsAndDetectSingularities.html).

## Examples

See the [ICWStaticStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html) examples.

## Remarks

This method corresponds to the Stress Hot Spot diagnostic tool that identifies adjacent elements with high stress gradiants. High stress gradients occur between elements with significantly different stress values which indicates the presence of stress singularities or stress concentrations.

Set NSensitivity to a lower number to restrict the search to elements with the highest strain values. Set NSensitivity to a higher number to expand the search to elements with lower strain values.

After calling this method, you can call:

- [ICWResults::CreateStressHotSpotPlot](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~CreateStressHotSpotPlot.html) and
- [ICWResults::GetDetectedHotSpotElements](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDetectedHotSpotElements.html) if BRunForNodes is false, or
- [ICWResults::GetDetectedHotSpotNodes](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults~GetDetectedHotSpotNodes.html) if BRunForNodes is true.

## See Also

[ICWResults Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults.html)
[ICWResults Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWResults_members.html)

## Availability

SOLIDWORKS Simulation API 2018 SP0
