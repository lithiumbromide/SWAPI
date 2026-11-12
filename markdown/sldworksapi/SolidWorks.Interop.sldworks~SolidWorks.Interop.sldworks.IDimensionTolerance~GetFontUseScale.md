---
title: "GetFontUseScale Method (IDimensionTolerance)"
project: "SOLIDWORKS API Help"
interface: "IDimensionTolerance"
member: "GetFontUseScale"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFontUseScale.html"
---

# GetFontUseScale Method (IDimensionTolerance)

Gets whether the tolerance font size is scaled based on the dimension font size, or if it is an absolute height value.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFontUseScale() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimensionTolerance
Dim value As System.Boolean

value = instance.GetFontUseScale()
```

### C#

```csharp
System.bool GetFontUseScale()
```

### C++/CLI

```cpp
System.bool GetFontUseScale();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the tolerance font size is scaled based on the dimension font size, false if the tolerance font size is an absolute height value

## VBA Syntax

See [DimensionTolerance::GetFontUseScale](ms-its:sldworksapivb6.chm::/sldworks~DimensionTolerance~GetFontUseScale.html).

## Remarks

If [IDimensionTolerance::GetFontUseDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFontUseDimension.html) is true, then the value returned by this
IDimensionTolerance::GetFontUseScale is True and the value returned by [IDimensionTolerance::GetFontScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFontScale.html)
is 1.0.

To get other tolerance font information, use the [IDimensionTolerance::GetFontHeight](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFontHeight.html).

To set the tolerance font information, use the [IDimensionTolerance::SetFont](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~SetFont.html) method.

This method deals with the tolerance font information, not the fit tolerance font information. To get or set fit tolerance information, use [IDimensionTolerance::GetFitFontUseDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFitFontUseDimension.html), [IDimensionTolerance::GetFitFontUseScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFitFontUseScale.html), [IDimensionTolerance::GetFitFontScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFitFontScale.html), [IDimensionTolerance::GetFitFontHeight](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFitFontHeight.html), and [IDimensionTolerance::SetFitFont](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~SetFitFont.html).

## See Also

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.html)
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
