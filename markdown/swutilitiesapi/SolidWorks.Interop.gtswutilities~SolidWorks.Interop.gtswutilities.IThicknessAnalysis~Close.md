---
title: "Close Method (IThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "IThicknessAnalysis"
member: "Close"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~Close.html"
---

# Close Method (IThicknessAnalysis)

Ends the current session of a thickness analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function Close() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IThicknessAnalysis
Dim value As System.Integer

value = instance.Close()
```

### C#

```csharp
System.int Close()
```

### C++/CLI

```cpp
System.int Close();
```

### Return Value

Error code as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IThicknessAnalysis::Close](ms-its:swutilitiesapivb6.chm::/swutilities~IThicknessAnalysis~Close.html).

## Examples

[Run Thickness Analysis (VBA)](Run_Thickness_Analysis_VB6.htm)

## Remarks

You must use this method to exit a session of a thickness analysis in your application. Otherwise, this tool may not run in the user interface if it was not closed in your application.

## See Also

[IThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis.html)
[IThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis_members.html)
[IThicknessAnalysis::Init Method](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~Init.html)

## Availability

SOLIDWORKS Utillities API 2006 FCS
