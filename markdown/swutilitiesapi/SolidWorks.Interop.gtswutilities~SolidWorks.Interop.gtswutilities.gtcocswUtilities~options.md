---
title: "options Property (gtcocswUtilities)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswUtilities"
member: "options"
kind: "property"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities~options.html"
---

# options Property (gtcocswUtilities)

Gets an IUtilOptions object.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property options As gtcocswUtilOptions
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswUtilities
Dim value As gtcocswUtilOptions

value = instance.options
```

### C#

```csharp
gtcocswUtilOptions options {get;}
```

### C++/CLI

```cpp
property gtcocswUtilOptions^ options {
   gtcocswUtilOptions^ get();
}
```

### Property Value

Pointer to [IUtilOptions](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IUtilOptions.html) object

## VBA Syntax

See [IUtilities::options](ms-its:swutilitiesapivb6.chm::/swutilities~IUtilities~options.html).

## See Also

[gtcocswUtilities Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities.html)
[gtcocswUtilities Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswUtilities_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
