---
title: "ThicknessAnalysis Property (IUtilities)"
project: "SOLIDWORKS Utilities API Help"
interface: "IUtilities"
member: "ThicknessAnalysis"
kind: "property"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities~ThicknessAnalysis.html"
---

# ThicknessAnalysis Property (IUtilities)

Gets an IThicknessAnalysis object.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ThicknessAnalysis As gtcocswThicknessAnalysis
```

### Visual Basic (Usage)

```vb
Dim instance As IUtilities
Dim value As gtcocswThicknessAnalysis

value = instance.ThicknessAnalysis
```

### C#

```csharp
gtcocswThicknessAnalysis ThicknessAnalysis {get;}
```

### C++/CLI

```cpp
property gtcocswThicknessAnalysis^ ThicknessAnalysis {
   gtcocswThicknessAnalysis^ get();
}
```

### Property Value

Pointer to an [IThicknessAnalysis](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IThicknessAnalysis.html) object

## VBA Syntax

See [IUtilities::ThicknessAnalysis](ms-its:swutilitiesapivb6.chm::/swutilities~IUtilities~ThicknessAnalysis.html).

## Examples

[Run Thickness Analysis (VBA)](Run_Thickness_Analysis_VB6.htm)

## See Also

[IUtilities Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities.html)
[IUtilities Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IUtilities_members.html)

## Availability

SOLIDWORKS Utilities API 2006 FCS
