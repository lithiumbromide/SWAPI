---
title: "FeaturePaint Method (gtcocswFeaturePaint)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswFeaturePaint"
member: "FeaturePaint"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswFeaturePaint~FeaturePaint.html"
---

# FeaturePaint Method (gtcocswFeaturePaint)

Obsolete. Superseded by [IFeaturePaint::FeaturePaint2](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IFeaturePaint~FeaturePaint2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FeaturePaint( _
   ByVal sourcefeature As System.String, _
   ByVal targetfeature As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswFeaturePaint
Dim sourcefeature As System.String
Dim targetfeature As System.String
Dim value As System.Integer

value = instance.FeaturePaint(sourcefeature, targetfeature)
```

### C#

```csharp
System.int FeaturePaint(
   System.string sourcefeature,
   System.string targetfeature
)
```

### C++/CLI

```cpp
System.int FeaturePaint(
   System.String^ sourcefeature,
   System.String^ targetfeature
)
```

### Parameters

- `sourcefeature`:
- `targetfeature`:

## VBA Syntax

See [IFeaturePaint::FeaturePaint](ms-its:swutilitiesapivb6.chm::/swutilities~IFeaturePaint~FeaturePaint.html).

## See Also

[gtcocswFeaturePaint Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswFeaturePaint.html)
[gtcocswFeaturePaint Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswFeaturePaint_members.html)
