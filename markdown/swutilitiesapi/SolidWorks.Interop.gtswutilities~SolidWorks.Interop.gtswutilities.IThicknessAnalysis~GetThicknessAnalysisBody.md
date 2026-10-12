---
title: "GetThicknessAnalysisBody Method (IThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "IThicknessAnalysis"
member: "GetThicknessAnalysisBody"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~GetThicknessAnalysisBody.html"
---

# GetThicknessAnalysisBody Method (IThicknessAnalysis)

Gets the SOLIDWORKS body in a multibody part selected for the thickness analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetThicknessAnalysisBody( _
   ByRef lErrorcode As System.Integer _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IThicknessAnalysis
Dim lErrorcode As System.Integer
Dim value As Body2

value = instance.GetThicknessAnalysisBody(lErrorcode)
```

### C#

```csharp
Body2 GetThicknessAnalysisBody(
   out System.int lErrorcode
)
```

### C++/CLI

```cpp
Body2^ GetThicknessAnalysisBody(
   [Out] System.int lErrorcode
)
```

### Parameters

- `lErrorcode`: Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

### Return Value

SOLIDWORKS [IBody2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) object

## Remarks

You do not need to use this method if the part is made up of a single solid body.

This method returns Nothing or Null if the body is a single solid body part.

Use [IThicknessAnalysis::SetThicknessAnalysisBody](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IThicknessAnalysis~SetThicknessAnalysisBody.html) to select the body for the thickness analysis.

## See Also

[IThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis.html)
[IThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
