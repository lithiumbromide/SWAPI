---
title: "GetNumCriticalFaces Method (gtcocswThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswThicknessAnalysis"
member: "GetNumCriticalFaces"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis~GetNumCriticalFaces.html"
---

# GetNumCriticalFaces Method (gtcocswThicknessAnalysis)

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
Dim instance As gtcocswThicknessAnalysis
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

## Remarks

If a model contains a critical face, then all of the features that share the face are classified as [critical features](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IThicknessAnalysis~GetNumCriticalFeatures.html).

## See Also

[gtcocswThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis.html)
[gtcocswThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
