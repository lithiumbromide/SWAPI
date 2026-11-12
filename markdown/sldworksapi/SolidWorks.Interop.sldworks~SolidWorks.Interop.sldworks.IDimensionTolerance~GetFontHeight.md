---
title: "GetFontHeight Method (IDimensionTolerance)"
project: "SOLIDWORKS API Help"
interface: "IDimensionTolerance"
member: "GetFontHeight"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFontHeight.html"
---

# GetFontHeight Method (IDimensionTolerance)

Gets the height of the tolerance font.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFontHeight() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDimensionTolerance
Dim value As System.Double

value = instance.GetFontHeight()
```

### C#

```csharp
System.double GetFontHeight()
```

### C++/CLI

```cpp
System.double GetFontHeight();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Height of the tolerance font in system units

## VBA Syntax

See [DimensionTolerance::GetFontHeight](ms-its:sldworksapivb6.chm::/sldworks~DimensionTolerance~GetFontHeight.html).

## Examples

[Get Dimension Tolerance (VBA)](Get_Dimension_Tolerance_Example_VB.htm)
[Get Dimension Tolerance (VB.NET)](Get_Dimension_Tolerance_Example_VBNET.htm)
[Get Dimension Tolerance (C#)](Get_Dimension_Tolerance_Example_CSharp.htm)

## Remarks

This value is used only if [IDimensionTolerance::GetFontUseDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFitFontUseDimension.html) and [IDimensionTolerance::GetFontUseScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFontUseScale.html)
are false.

To get other tolerance font information, use [IDimensionTolerance::GetFontScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFitFontScale.html).

To set the tolerance font information, use [IDimensionTolerance::SetFont](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~SetFont.html).

This method deals with the tolerance font information, not the fit tolerance font information. To get or set fit tolerance information, use [IDimensionTolerance::GetFitFontUseDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFitFontUseDimension.html), [IDimensionTolerance::GetFitFontUseScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFitFontUseScale.html), [IDimensionTolerance::GetFitFontScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFitFontScale.html), [IDimensionTolerance::GetFitFontHeight](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFitFontHeight.html), and [IDimensionTolerance::SetFitFont](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~SetFitFont.html).

## See Also

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.html)
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
