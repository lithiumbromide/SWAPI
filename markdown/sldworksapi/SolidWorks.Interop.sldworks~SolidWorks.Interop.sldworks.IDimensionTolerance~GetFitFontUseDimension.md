---
title: "GetFitFontUseDimension Method (IDimensionTolerance)"
project: "SOLIDWORKS API Help"
interface: "IDimensionTolerance"
member: "GetFitFontUseDimension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontUseDimension.html"
---

# GetFitFontUseDimension Method (IDimensionTolerance)

Gets whether the fit tolerance font is the same size as the dimension font.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFitFontUseDimension() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimensionTolerance
Dim value As System.Boolean

value = instance.GetFitFontUseDimension()
```

### C#

```csharp
System.bool GetFitFontUseDimension()
```

### C++/CLI

```cpp
System.bool GetFitFontUseDimension();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the fit tolerance font is the same size as the dimension font, false if not

## VBA Syntax

See [DimensionTolerance::GetFitFontUseDimension](ms-its:sldworksapivb6.chm::/sldworks~DimensionTolerance~GetFitFontUseDimension.html).

## Examples

[Get Dimension Tolerance (C#)](Get_Dimension_Tolerance_Example_CSharp.htm)
[Get Dimension Tolerance (VB.NET)](Get_Dimension_Tolerance_Example_VBNET.htm)
[Get Dimension Tolerance (VBA)](Get_Dimension_Tolerance_Example_VB.htm)

## Remarks

To get other fit tolerance font information, use [IDimensionTolerance::GetFitFontUseScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFitFontUseScale.html),
[IDimensionTolerance::GetFitFontScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFitFontScale.html), and [IDimensionTolerance::GetFitFontHeight](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFitFontHeight.html).

To set the fit tolerance font information, use [IDimensionTolerance::SetFitFont](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~SetFitFont.html).

This method deals with the fit tolerance font information, not the tolerance font information. To get or set tolerance information, use [IDimensionTolerance::GetFontUseDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFontUseDimension.html), [IDimensionTolerance::GetFontUseScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFontUseScale.html), [IDimensionTolerance::GetFontScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFontScale.html), [IDimensionTolerance::GetFontHeight](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFontHeight.html), and [IDimensionTolerance::SetFont](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~SetFont.html).

## See Also

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.html)
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.html)
[IDimensionTolerance::FitDisplayStyle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~FitDisplayStyle.html)
[IDimensionTolerance::FitType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~FitType.html)
[IDimensionTolerance::GetHoleFitValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetHoleFitValue.html)
[IDimensionTolerance::GetShaftFitValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetShaftFitValue.html)
[IDimensionTolerance::SetFitValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetFitValues.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
