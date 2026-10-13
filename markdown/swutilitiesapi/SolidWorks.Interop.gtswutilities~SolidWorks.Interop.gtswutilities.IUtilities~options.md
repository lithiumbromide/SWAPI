---
title: "options Property (IUtilities)"
project: "SOLIDWORKS Utilities API Help"
interface: "IUtilities"
member: "options"
kind: "property"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities~options.html"
---

# options Property (IUtilities)

Gets an IUtilOptions object.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property options As gtcocswUtilOptions
```

### Visual Basic (Usage)

```vb
Dim instance As IUtilities
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

## Examples

[Set Tolerances and Compare Geometry (VBA)](Set_Tolerances_and_Compare_Geometry_VB6.htm)
[Set Tolerances and Compare Geometry (VB.NET)](Set_Tolerances_and_Compare_Geometry_VBNET.htm)
[Set Tolerances and Compare Geometry (C#)](Set_Tolerances_and_Compare_Geometry_CSharp.htm)

## See Also

[IUtilities Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities.html)
[IUtilities Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
