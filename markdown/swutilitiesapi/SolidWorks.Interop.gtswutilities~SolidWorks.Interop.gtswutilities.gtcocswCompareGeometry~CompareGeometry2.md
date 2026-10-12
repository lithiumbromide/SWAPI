---
title: "CompareGeometry2 Method (gtcocswCompareGeometry)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswCompareGeometry"
member: "CompareGeometry2"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswCompareGeometry~CompareGeometry2.html"
---

# CompareGeometry2 Method (gtcocswCompareGeometry)

Obsolete. Superseded by [ICompareGeometry::CompareGeometry3](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.ICompareGeometry~CompareGeometry3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CompareGeometry2( _
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
Dim instance As gtcocswCompareGeometry
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

value = instance.CompareGeometry2(reffile, refconfig, modfile, modconfig, lOperationOptions, lResultOptions, reportname, vtAddToBinderOption, vtOverwrite)
```

### C#

```csharp
System.int CompareGeometry2(
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
System.int CompareGeometry2(
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
- `lOperationOptions`: Compare face, volume, or face and volume options as defined by [gtGdfOperationOption_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtGdfOperationOption_e.html)
- `lResultOptions`: Display the results or save the results to a report as defined by [gtResultOptions_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtResultOptions_e.html)
- `reportname`: Path where to save the results report
- `vtAddToBinderOption`: True to add the results report to the Design Binder, false to not
- `vtOverwrite`: True to overwrite an existing results report of the same name, false to not

### Return Value

Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [ICompareGeometry::CompareGeometry2](ms-its:swutilitiesapivb6.chm::/swutilities~ICompareGeometry~CompareGeometry2.html).

## Remarks

The vtAddToBinderOption argument is disabled when comparing:

- Two documents with the same name, but located in different folders, are compared,
- Two configurations of the same part are compared, or
- Documents are selected from the PDM vault

because the documents are saved as temporary files during the comparison.

## See Also

[gtcocswCompareGeometry Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswCompareGeometry.html)
[gtcocswCompareGeometry Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswCompareGeometry_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
