---
title: "FeaturePaint Property (IUtilities)"
project: "SOLIDWORKS Utilities API Help"
interface: "IUtilities"
member: "FeaturePaint"
kind: "property"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities~FeaturePaint.html"
---

# FeaturePaint Property (IUtilities)

Gets an IFeaturePaint object.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FeaturePaint As gtcocswFeaturePaint
```

### Visual Basic (Usage)

```vb
Dim instance As IUtilities
Dim value As gtcocswFeaturePaint

value = instance.FeaturePaint
```

### C#

```csharp
gtcocswFeaturePaint FeaturePaint {get;}
```

### C++/CLI

```cpp
property gtcocswFeaturePaint^ FeaturePaint {
   gtcocswFeaturePaint^ get();
}
```

### Property Value

Pointer to an [IFeaturePaint](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IFeaturePaint.html) object

## VBA Syntax

See [IUtilities::FeaturePaint](ms-its:swutilitiesapivb6.chm::/swutilities~IUtilities~FeaturePaint.html).

## See Also

[IUtilities Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities.html)
[IUtilities Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities_members.html)

## Availability

SoildWorks Utilities SPI 2005 FCS
