---
title: "Init Method (gtcocswThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswThicknessAnalysis"
member: "Init"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis~Init.html"
---

# Init Method (gtcocswThicknessAnalysis)

Initializes the Thickness Analysis utility with the active SOLIDWORKS document.

## Syntax

### Visual Basic (Declaration)

```vb
Function Init() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswThicknessAnalysis
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

## Remarks

You must use this method to exit a session of a thickness analysis in your application. Otherwise, this tool may not run in the user interface if it was not closed in your application.

## See Also

[gtcocswThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis.html)
[gtcocswThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
