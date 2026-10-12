---
title: "GetCriticalFeatureNames Method (gtcocswThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswThicknessAnalysis"
member: "GetCriticalFeatureNames"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis~GetCriticalFeatureNames.html"
---

# GetCriticalFeatureNames Method (gtcocswThicknessAnalysis)

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
Dim instance As gtcocswThicknessAnalysis
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

## Remarks

If a model contains a critical face, then all of the features that share the face are classified as critical features.

## See Also

[gtcocswThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis.html)
[gtcocswThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
