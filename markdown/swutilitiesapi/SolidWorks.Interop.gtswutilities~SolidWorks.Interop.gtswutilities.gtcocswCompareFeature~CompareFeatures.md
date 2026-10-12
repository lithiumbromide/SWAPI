---
title: "CompareFeatures Method (gtcocswCompareFeature)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswCompareFeature"
member: "CompareFeatures"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswCompareFeature~CompareFeatures.html"
---

# CompareFeatures Method (gtcocswCompareFeature)

Obsolete. Superseded by [ICompareFeature::CompareFeatures2](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.ICompareFeature~CompareFeatures2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CompareFeatures( _
   ByVal reffile As System.String, _
   ByVal modfile As System.String, _
   ByVal lOptions As System.Integer, _
   ByVal reportname As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswCompareFeature
Dim reffile As System.String
Dim modfile As System.String
Dim lOptions As System.Integer
Dim reportname As System.String
Dim value As System.Integer

value = instance.CompareFeatures(reffile, modfile, lOptions, reportname)
```

### C#

```csharp
System.int CompareFeatures(
   System.string reffile,
   System.string modfile,
   System.int lOptions,
   System.string reportname
)
```

### C++/CLI

```cpp
System.int CompareFeatures(
   System.String^ reffile,
   System.String^ modfile,
   System.int lOptions,
   System.String^ reportname
)
```

### Parameters

- `reffile`:
- `modfile`:
- `lOptions`:
- `reportname`:

## VBA Syntax

See [ICompareFeature::CompareFeatures](ms-its:swutilitiesapivb6.chm::/swutilities~ICompareFeature~CompareFeatures.html).

## See Also

[gtcocswCompareFeature Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswCompareFeature.html)
[gtcocswCompareFeature Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswCompareFeature_members.html)
