---
title: "GetNumCriticalFeatures Method (gtcocswThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswThicknessAnalysis"
member: "GetNumCriticalFeatures"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis~GetNumCriticalFeatures.html"
---

# GetNumCriticalFeatures Method (gtcocswThicknessAnalysis)

Gets the number of critical features in the analyzed area.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNumCriticalFeatures( _
   ByRef lErrorcode As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswThicknessAnalysis
Dim lErrorcode As System.Integer
Dim value As System.Integer

value = instance.GetNumCriticalFeatures(lErrorcode)
```

### C#

```csharp
System.int GetNumCriticalFeatures(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
System.int GetNumCriticalFeatures(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

Number of critical features

## VBA Syntax

See [IThicknessAnalysis::GetNumCriticalFeatures](ms-its:swutilitiesapivb6.chm::/swutilities~IThicknessAnalysis~GetNumCriticalFeatures.html).

## Remarks

If a model contains a [critical face](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IThicknessAnalysis~GetNumCriticalFaces.html), then all of the features that share the face are classified as critical features.

Use [IThicknessAnalysis::GetCriticalFeatureNames](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IThicknessAnalysis~GetCriticalFeatureNames.html) to get the names of the critical features.

## See Also

[gtcocswThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis.html)
[gtcocswThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
