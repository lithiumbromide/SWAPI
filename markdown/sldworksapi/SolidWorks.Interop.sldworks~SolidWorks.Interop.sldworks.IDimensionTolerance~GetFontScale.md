---
title: "GetFontScale Method (IDimensionTolerance)"
project: "SOLIDWORKS API Help"
interface: "IDimensionTolerance"
member: "GetFontScale"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFontScale.html"
---

# GetFontScale Method (IDimensionTolerance)

Gets the ratio of the height of the tolerance font to the height of the dimension font.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFontScale() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDimensionTolerance
Dim value As System.Double

value = instance.GetFontScale()
```

### C#

```csharp
System.double GetFontScale()
```

### C++/CLI

```cpp
System.double GetFontScale();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Ratio of the height of the tolerance font to the height of the dimension font

## VBA Syntax

See [DimensionTolerance::GetFontScale](ms-its:sldworksapivb6.chm::/sldworks~DimensionTolerance~GetFontScale.html).

## Examples

[Get Dimension Tolerance (VBA)](Get_Dimension_Tolerance_Example_VB.htm)
[Get Dimension Tolerance (VB.NET)](Get_Dimension_Tolerance_Example_VBNET.htm)
[Get Dimension Tolerance (C#)](Get_Dimension_Tolerance_Example_CSharp.htm)

## Remarks

If [IDimensionTolerance::GetFontUseDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFontUseDimension.html) is true, then the value returned by the [IDimensionTolerance::GetFontUseScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFontUseScale.html) is True and the value returned by IDimensionTolerance::GetFontScale is 1.0.

To get other tolerance font information, use [IDimensionTolerance::GetFontHeight](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFontHeight.html).

To set the tolerance font information, use [IDimensionTolerance::SetFont](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~SetFont.html).

This method deals with the tolerance font information, not the fit tolerance font information. To get or set fit tolerance information, use [IDimensionTolerance::GetFitFontUseDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFitFontUseDimension.html), [IDimensionTolerance::GetFitFontUseScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFitFontUseScale.html), [IDimensionTolerance::GetFitFontScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFitFontScale.html), [IDimensionTolerance::GetFitFontHeight](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFitFontHeight.html), and [IDimensionTolerance::SetFitFont](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~SetFitFont.html).

## See Also

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.html)
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
