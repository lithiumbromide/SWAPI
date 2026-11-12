---
title: "GetNumCriticalFaces Method (IThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "IThicknessAnalysis"
member: "GetNumCriticalFaces"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetNumCriticalFaces.html"
---

# GetNumCriticalFaces Method (IThicknessAnalysis)

Gets the number of critical faces in the analyzed area.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNumCriticalFaces( _
   ByRef lErrorcode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IThicknessAnalysis
Dim lErrorcode As System.Integer
Dim value As System.Integer

value = instance.GetNumCriticalFaces(lErrorcode)
```

### C#

```csharp
System.int GetNumCriticalFaces(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.int GetNumCriticalFaces(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Number of critical faces

## VBA Syntax

See [IThicknessAnalysis::GetNumCriticalFaces](ms-its:swutilitiesapivb6.chm::/swutilities~IThicknessAnalysis~GetNumCriticalFaces.html).

## Examples

[Run Thickness Analysis (VBA)](Run_Thickness_Analysis_VB6.htm)

## Remarks

If a model contains a critical face, then all of the features that share the face are classified as [critical features](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IThicknessAnalysis~GetNumCriticalFeatures.html).

## See Also

[IThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis.html)
[IThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis_members.html)
[IThicknessAnalysis::GetAnalysisDetails Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetAnalysisDetails.html)
[IThicknessAnalysis::GetAvgWeightedTckOnCritArea Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetAvgWeightedTckOnCritArea.html)
[IThicknessAnalysis::GetCriticalFeatureNames Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetCriticalFeatureNames.html)
[IThicknessAnalysis::GetCriticalSurfaceArea Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetCriticalSurfaceArea.html)
[IThicknessAnalysis::GetNumCriticalFeatures Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetNumCriticalFeatures.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
