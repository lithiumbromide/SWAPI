---
title: "RunThinAnalysis Method (gtcocswThicknessAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswThicknessAnalysis"
member: "RunThinAnalysis"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis~RunThinAnalysis.html"
---

# RunThinAnalysis Method (gtcocswThicknessAnalysis)

Obsolete. Superseded by [IThicknessAnalysis::RunThinAnalysis2](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IThicknessAnalysis~RunThinAnalysis2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function RunThinAnalysis( _
   ByVal targetthickness As System.Double, _
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
Dim resolution As System.Integer
Dim lResultOptions As System.Integer
Dim reportname As System.String
Dim vtAddToBinderOption As System.Boolean
Dim vtOverwrite As System.Boolean
Dim value As System.Integer

value = instance.RunThinAnalysis(targetthickness, resolution, lResultOptions, reportname, vtAddToBinderOption, vtOverwrite)
```

### C#

```csharp
System.int RunThinAnalysis(
   System.double targetthickness,
   System.int resolution,
   System.int lResultOptions,
   System.string reportname,
   System.bool vtAddToBinderOption,
   System.bool vtOverwrite
)
```

### C++/CLI

```cpp
System.int RunThinAnalysis(
   System.double targetthickness,
   System.int resolution,
   System.int lResultOptions,
   System.String^ reportname,
   System.bool vtAddToBinderOption,
   System.bool vtOverwrite
)
```

### Parameters

- `targetthickness`:
- `resolution`:
- `lResultOptions`:
- `reportname`:
- `vtAddToBinderOption`:
- `vtOverwrite`:

## VBA Syntax

See [IThicknessAnalysis::RunThinAnalysis](ms-its:swutilitiesapivb6.chm::/swutilities~IThicknessAnalysis~RunThinAnalysis.html).

## See Also

[gtcocswThicknessAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis.html)
[gtcocswThicknessAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswThicknessAnalysis_members.html)
