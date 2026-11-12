---
title: "Init Method (IThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "IThicknessAnalysis"
member: "Init"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis~Init.html"
---

# Init Method (IThicknessAnalysis)

Initializes the Thickness Analysis utility with the active SOLIDWORKS document.

## Syntax

### Visual Basic (Declaration)

```vb
Function Init() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IThicknessAnalysis
Dim value As System.Integer

value = instance.Init()
```

### C#

```csharp
System.int Init()
```

### C++/CLI

```cpp
System.int Init();
```

### Return Value

Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IThicknessAnalysis::Init](ms-its:swutilitiesapivb6.chm::/swutilities~IThicknessAnalysis~Init.html).

## Examples

[Run Thickness Analysis (VBA)](Run_Thickness_Analysis_VB6.htm)

## Remarks

You must use this method to exit a session of a thickness analysis in your application. Otherwise, this tool may not run in the user interface if it was not closed in your application.

## See Also

[IThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis.html)
[IThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IThicknessAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
