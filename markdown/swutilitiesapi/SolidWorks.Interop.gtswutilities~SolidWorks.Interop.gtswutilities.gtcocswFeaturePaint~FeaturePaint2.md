---
title: "FeaturePaint2 Method (gtcocswFeaturePaint)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswFeaturePaint"
member: "FeaturePaint2"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswFeaturePaint~FeaturePaint2.html"
---

# FeaturePaint2 Method (gtcocswFeaturePaint)

Copies the source feature's parameters to the target feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function FeaturePaint2( _
   ByVal sourcefeature As System.String, _
   ByVal targetfeature As System.String, _
   ByVal pasteappearance As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswFeaturePaint
Dim sourcefeature As System.String
Dim targetfeature As System.String
Dim pasteappearance As System.Boolean
Dim value As System.Integer

value = instance.FeaturePaint2(sourcefeature, targetfeature, pasteappearance)
```

### C#

```csharp
System.int FeaturePaint2(
   System.string sourcefeature,
   System.string targetfeature,
   System.bool pasteappearance
)
```

### C++/CLI

```cpp
System.int FeaturePaint2(
   System.String^ sourcefeature,
   System.String^ targetfeature,
   System.bool pasteappearance
)
```

### Parameters

- `sourcefeature`: <source feature name>@<path\filename>.sldprt
- `targetfeature`: <target feature name>@<path\filename>.sldprt
- `pasteappearance`: True if the source feature's parameters are copied to the target feature, false if not

### Return Value

Error as defined by [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IFeaturePaint::FeaturePaint2](ms-its:swutilitiesapivb6.chm::/swutilities~IFeaturePaint~FeaturePaint2.html).

## See Also

[gtcocswFeaturePaint Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswFeaturePaint.html)
[gtcocswFeaturePaint Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswFeaturePaint_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
