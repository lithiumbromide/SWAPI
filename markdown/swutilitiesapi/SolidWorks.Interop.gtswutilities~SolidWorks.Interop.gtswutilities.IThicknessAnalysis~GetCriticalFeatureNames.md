---
title: "GetCriticalFeatureNames Method (IThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "IThicknessAnalysis"
member: "GetCriticalFeatureNames"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetCriticalFeatureNames.html"
---

# GetCriticalFeatureNames Method (IThicknessAnalysis)

Gets the names of the features that violate the target thickness.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCriticalFeatureNames( _
   ByRef lErrorcode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IThicknessAnalysis
Dim lErrorcode As System.Integer
Dim value As System.Object

value = instance.GetCriticalFeatureNames(lErrorcode)
```

### C#

```csharp
System.object GetCriticalFeatureNames(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.Object^ GetCriticalFeatureNames(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Array of the names of the features that violate the target thickness

## VBA Syntax

See [IThicknessAnalysis::GetCriticalFeatureNames](ms-its:swutilitiesapivb6.chm::/swutilities~IThicknessAnalysis~GetCriticalFeatureNames.html).

## Examples

[Run Thickness Analysis (VBA)](Run_Thickness_Analysis_VB6.htm)

## Remarks

If a model contains a critical face, then all of the features that share the face are classified as critical features.

## See Also

[IThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis.html)
[IThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis_members.html)
[IThicknessAnalysis::GetAnalysisDetails Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetAnalysisDetails.html)
[IThicknessAnalysis::GetAvgWeightedTckOnCritArea Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetAvgWeightedTckOnCritArea.html)
[IThicknessAnalysis::GetCriticalSurfaceArea Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetCriticalSurfaceArea.html)
[IThicknessAnalysis::GetNumCriticalFaces Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetNumCriticalFaces.html)
[IThicknessAnalysis::GetNumCriticalFeatures Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetNumCriticalFeatures.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
