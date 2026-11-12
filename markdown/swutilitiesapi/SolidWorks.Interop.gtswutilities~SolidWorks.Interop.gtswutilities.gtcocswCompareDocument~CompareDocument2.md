---
title: "CompareDocument2 Method (gtcocswCompareDocument)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswCompareDocument"
member: "CompareDocument2"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswCompareDocument~CompareDocument2.html"
---

# CompareDocument2 Method (gtcocswCompareDocument)

Compares the properties of the specified SOLIDWORKS documents and generates a report.

## Syntax

### Visual Basic (Declaration)

```vb
Function CompareDocument2( _
   ByVal reffile As System.String, _
   ByVal refconfig As System.String, _
   ByVal modfile As System.String, _
   ByVal modconfig As System.String, _
   ByVal lOperationOptions As System.Integer, _
   ByVal lResultOptions As System.Integer, _
   ByVal reportname As System.String, _
   ByVal vtAddToBinderOption As System.Boolean, _
   ByVal vtOverwrite As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswCompareDocument
Dim reffile As System.String
Dim refconfig As System.String
Dim modfile As System.String
Dim modconfig As System.String
Dim lOperationOptions As System.Integer
Dim lResultOptions As System.Integer
Dim reportname As System.String
Dim vtAddToBinderOption As System.Boolean
Dim vtOverwrite As System.Boolean
Dim value As System.Integer

value = instance.CompareDocument2(reffile, refconfig, modfile, modconfig, lOperationOptions, lResultOptions, reportname, vtAddToBinderOption, vtOverwrite)
```

### C#

```csharp
System.int CompareDocument2(
   System.string reffile,
   System.string refconfig,
   System.string modfile,
   System.string modconfig,
   System.int lOperationOptions,
   System.int lResultOptions,
   System.string reportname,
   System.bool vtAddToBinderOption,
   System.bool vtOverwrite
)
```

### C++/CLI

```cpp
System.int CompareDocument2(
   System.String^ reffile,
   System.String^ refconfig,
   System.String^ modfile,
   System.String^ modconfig,
   System.int lOperationOptions,
   System.int lResultOptions,
   System.String^ reportname,
   System.bool vtAddToBinderOption,
   System.bool vtOverwrite
)
```

### Parameters

- `reffile`: Path and filename of the SOLIDWORKS document containing the referenced part
- `refconfig`: Name of reference part's configuration; if blank, then the active configuration is used
- `modfile`: Path and filename of the SOLIDWORKS document containing the modified part
- `modconfig`: Name of modified part's configuration
- `lOperationOptions`: Compare face, volume, or feature as defined by [gtCodOperationOption_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtCodOperationOption_e.html)
- `lResultOptions`: Display the results or save the results to a report as defined by [gtResultOptions_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtResultOptions_e.html)
- `reportname`: Path where to write the results report
- `vtAddToBinderOption`: True to add the results report to the Design Binder, false to not
- `vtOverwrite`: True to overwrite an existing results report of the same name, false to not

### Return Value

Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [ICompareDocument::CompareDocument2](ms-its:swutilitiesapivb6.chm::/swutilities~ICompareDocument~CompareDocument2.html).

## See Also

[gtcocswCompareDocument Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswCompareDocument.html)
[gtcocswCompareDocument Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswCompareDocument_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
