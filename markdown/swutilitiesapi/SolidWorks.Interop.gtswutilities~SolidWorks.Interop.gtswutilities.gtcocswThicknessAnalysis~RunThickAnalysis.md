---
title: "RunThickAnalysis Method (gtcocswThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswThicknessAnalysis"
member: "RunThickAnalysis"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis~RunThickAnalysis.html"
---

# RunThickAnalysis Method (gtcocswThicknessAnalysis)

Obsolete. Superseded by [IThicknessAnalysis::RunThickAnalysis2](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IThicknessAnalysis~RunThickAnalysis2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function RunThickAnalysis( _
   ByVal targetthickness As System.Double, _
   ByVal thicklimit As System.Double, _
   ByVal treatcornerzero As System.Boolean, _
   ByVal resolution As System.Integer, _
   ByVal lResultOptions As System.Integer, _
   ByVal reportname As System.String, _
   ByVal vtAddToBinderOption As System.Boolean, _
   ByVal vtOverwrite As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswThicknessAnalysis
Dim targetthickness As System.Double
Dim thicklimit As System.Double
Dim treatcornerzero As System.Boolean
Dim resolution As System.Integer
Dim lResultOptions As System.Integer
Dim reportname As System.String
Dim vtAddToBinderOption As System.Boolean
Dim vtOverwrite As System.Boolean
Dim value As System.Integer

value = instance.RunThickAnalysis(targetthickness, thicklimit, treatcornerzero, resolution, lResultOptions, reportname, vtAddToBinderOption, vtOverwrite)
```

### C#

```csharp
System.int RunThickAnalysis(
   System.double targetthickness,
   System.double thicklimit,
   System.bool treatcornerzero,
   System.int resolution,
   System.int lResultOptions,
   System.string reportname,
   System.bool vtAddToBinderOption,
   System.bool vtOverwrite
)
```

### C++/CLI

```cpp
System.int RunThickAnalysis(
   System.double targetthickness,
   System.double thicklimit,
   System.bool treatcornerzero,
   System.int resolution,
   System.int lResultOptions,
   System.String^ reportname,
   System.bool vtAddToBinderOption,
   System.bool vtOverwrite
)
```

### Parameters

- `targetthickness`:
- `thicklimit`:
- `treatcornerzero`:
- `resolution`:
- `lResultOptions`:
- `reportname`:
- `vtAddToBinderOption`:
- `vtOverwrite`:

## VBA Syntax

See [IThicknessAnalysis::RunThickAnalysis](ms-its:swutilitiesapivb6.chm::/swutilities~IThicknessAnalysis~RunThickAnalysis.html).

## See Also

[gtcocswThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis.html)
[gtcocswThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis_members.html)
