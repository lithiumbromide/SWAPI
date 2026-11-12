---
title: "GetCriticalSurfaceArea Method (IThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "IThicknessAnalysis"
member: "GetCriticalSurfaceArea"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetCriticalSurfaceArea.html"
---

# GetCriticalSurfaceArea Method (IThicknessAnalysis)

Gets the critical surface area.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCriticalSurfaceArea( _
   ByRef lErrorcode As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IThicknessAnalysis
Dim lErrorcode As System.Integer
Dim value As System.Double

value = instance.GetCriticalSurfaceArea(lErrorcode)
```

### C#

```csharp
System.double GetCriticalSurfaceArea(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.double GetCriticalSurfaceArea(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Critical surface area

## VBA Syntax

See [IThicknessAnalysis::GetCriticalSurfaceArea](ms-its:swutilitiesapivb6.chm::/swutilities~IThicknessAnalysis~GetCriticalSurfaceArea.html).

## Examples

[Run Thickness Analysis (VBA)](Run_Thickness_Analysis_VB6.htm)

## See Also

[IThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis.html)
[IThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis_members.html)
[IThicknessAnalysis::GetAnalysisDetails Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetAnalysisDetails.html)
[IThicknessAnalysis::GetAvgWeightedTckOnCritArea Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetAvgWeightedTckOnCritArea.html)
[IThicknessAnalysis::GetCriticalFeatureNames Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetCriticalFeatureNames.html)
[IThicknessAnalysis::GetNumCriticalFaces Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetNumCriticalFaces.html)
[IThicknessAnalysis::GetNumCriticalFeatures Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetNumCriticalFeatures.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
