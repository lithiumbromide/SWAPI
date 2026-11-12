---
title: "SaveReport Method (IGeometryAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "IGeometryAnalysis"
member: "SaveReport"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis~SaveReport.html"
---

# SaveReport Method (IGeometryAnalysis)

Obsolete. Superseded by [IGeometryAnalysis::SaveReport2](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IGeometryAnalysis~SaveReport2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveReport( _
   ByVal reportname As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IGeometryAnalysis
Dim reportname As System.String
Dim value As System.Integer

value = instance.SaveReport(reportname)
```

### C#

```csharp
System.int SaveReport(
   System.string reportname
)
```

### C++/CLI

```cpp
System.int SaveReport(
   System.String^ reportname
)
```

### Parameters

- `reportname`:

## VBA Syntax

See [IGeometryAnalysis::SaveReport](ms-its:swutilitiesapivb6.chm::/swutilities~IGeometryAnalysis~SaveReport.html).

## See Also

[IGeometryAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis.html)
[IGeometryAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IGeometryAnalysis_members.html)
