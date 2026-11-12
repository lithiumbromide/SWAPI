---
title: "CompareFeatures2 Method (ICompareFeature)"
project: "SOLIDWORKS Utilities API Help"
interface: "ICompareFeature"
member: "CompareFeatures2"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.ICompareFeature~CompareFeatures2.html"
---

# CompareFeatures2 Method (ICompareFeature)

Identifies the differences in solid features between two versions of the same SOLIDWORKS part and generates a report.

## Syntax

### Visual Basic (Declaration)

```vb
Function CompareFeatures2( _
   ByVal reffile As System.String, _
   ByVal refconfig As System.String, _
   ByVal modfile As System.String, _
   ByVal modconfig As System.String, _
   ByVal lOptions As System.Integer, _
   ByVal reportname As System.String, _
   ByVal vtAddToBinderOption As System.Boolean, _
   ByVal vtOverwrite As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICompareFeature
Dim reffile As System.String
Dim refconfig As System.String
Dim modfile As System.String
Dim modconfig As System.String
Dim lOptions As System.Integer
Dim reportname As System.String
Dim vtAddToBinderOption As System.Boolean
Dim vtOverwrite As System.Boolean
Dim value As System.Integer

value = instance.CompareFeatures2(reffile, refconfig, modfile, modconfig, lOptions, reportname, vtAddToBinderOption, vtOverwrite)
```

### C#

```csharp
System.int CompareFeatures2(
   System.string reffile,
   System.string refconfig,
   System.string modfile,
   System.string modconfig,
   System.int lOptions,
   System.string reportname,
   System.bool vtAddToBinderOption,
   System.bool vtOverwrite
)
```

### C++/CLI

```cpp
System.int CompareFeatures2(
   System.String^ reffile,
   System.String^ refconfig,
   System.String^ modfile,
   System.String^ modconfig,
   System.int lOptions,
   System.String^ reportname,
   System.bool vtAddToBinderOption,
   System.bool vtOverwrite
)
```

### Parameters

- `reffile`: Path and filename of the SOLIDWORKS document containing the referenced part
- `refconfig`: Name of the reference part's configuration; if blank, then the active configuration is used
- `modfile`: Path and filename of the SOLIDWORKS document containing the modified part
- `modconfig`: Name of modified part's configuration
- `lOptions`: Display the results or save the results to a report as defined by [gtResultOptions_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtResultOptions_e.html)
- `reportname`: Path where to save the results report
- `vtAddToBinderOption`: True to add the results report to the Design Binder, false to not
- `vtOverwrite`: True to overwrite an existing results report of the same name, false to not

### Return Value

Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [ICompareFeature::CompareFeatures2](ms-its:swutilitiesapivb6.chm::/swutilities~ICompareFeature~CompareFeatures2.html).

## Examples

[Compare Features (VBA)](Compare_Features_VB6.htm)

## See Also

[ICompareFeature Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.ICompareFeature.html)
[ICompareFeature Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.ICompareFeature_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
