---
title: "SaveReport2 Method (gtcocswGeometryAnalysis)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswGeometryAnalysis"
member: "SaveReport2"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswGeometryAnalysis~SaveReport2.html"
---

# SaveReport2 Method (gtcocswGeometryAnalysis)

Generates a report containing the results of the geometry analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveReport2( _
   ByVal reportname As System.String, _
   ByVal vtAddToBinderOption As System.Boolean, _
   ByVal vtOverwrite As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswGeometryAnalysis
Dim reportname As System.String
Dim vtAddToBinderOption As System.Boolean
Dim vtOverwrite As System.Boolean
Dim value As System.Integer

value = instance.SaveReport2(reportname, vtAddToBinderOption, vtOverwrite)
```

### C#

```csharp
System.int SaveReport2(
   System.string reportname,
   System.bool vtAddToBinderOption,
   System.bool vtOverwrite
)
```

### C++/CLI

```cpp
System.int SaveReport2(
   System.String^ reportname,
   System.bool vtAddToBinderOption,
   System.bool vtOverwrite
)
```

### Parameters

- `reportname`: Path and filename to which to write the report
- `vtAddToBinderOption`: True to add the report to the Design Binder, false to not
- `vtOverwrite`: True to overwrite an existing report of the same name, false to not

### Return Value

Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IGeometryAnalysis::SaveReport2](ms-its:swutilitiesapivb6.chm::/swutilities~IGeometryAnalysis~SaveReport2.html).

## See Also

[gtcocswGeometryAnalysis Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswGeometryAnalysis.html)
[gtcocswGeometryAnalysis Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswGeometryAnalysis_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
