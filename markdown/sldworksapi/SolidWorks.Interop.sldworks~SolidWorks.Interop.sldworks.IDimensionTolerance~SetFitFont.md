---
title: "SetFitFont Method (IDimensionTolerance)"
project: "SOLIDWORKS API Help"
interface: "IDimensionTolerance"
member: "SetFitFont"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetFitFont.html"
---

# SetFitFont Method (IDimensionTolerance)

Sets the fit tolerance font values.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFitFont( _
   ByVal UseDimension As System.Boolean, _
   ByVal UseScale As System.Boolean, _
   ByVal Value As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimensionTolerance
Dim UseDimension As System.Boolean
Dim UseScale As System.Boolean
Dim Value As System.Double
Dim value As System.Boolean

value = instance.SetFitFont(UseDimension, UseScale, Value)
```

### C#

```csharp
System.bool SetFitFont(
   System.bool UseDimension,
   System.bool UseScale,
   System.double Value
)
```

### C++/CLI

```cpp
System.bool SetFitFont(
   System.bool UseDimension,
   System.bool UseScale,
   System.double Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseDimension`: True if the fit tolerance font should be the same size as the dimension font, false if not
- `UseScale`: True if the fit tolerance font should be scaled based on the dimension font, false if the fit tolerance font size is an absolute height value
- `Value`: Scale ratio if UseScale is true or height value if UseScale is false

### Return Value

True if the fit tolerance font is set, false if not

## VBA Syntax

See [DimensionTolerance::SetFitFont](ms-its:sldworksapivb6.chm::/sldworks~DimensionTolerance~SetFitFont.html).

## Examples

[Get Dimension Tolerance (C#)](Get_Dimension_Tolerance_Example_CSharp.htm)
[Get Dimension Tolerance (VB.NET)](Get_Dimension_Tolerance_Example_VBNET.htm)
[Get Dimension Tolerance (VBA)](Get_Dimension_Tolerance_Example_VB.htm)

## Remarks

| If UseDimension is... | Then... |
| --- | --- |
| True | The other arguments are ignored. UseScale is true. Value is 1.0. |
| False | UseScale determines how Value is interpreted. If UseScale is... Then Value is assumed to be... True Scale value to use, and the height value is not changed. False Height value to use, and the scale value is not changed. |
| If UseScale is... | Then Value is assumed to be... |
| True | Scale value to use, and the height value is not changed. |
| False | Height value to use, and the scale value is not changed. |

To get the fit tolerance font information, use [IDimensionTolerance::GetFitFontUseDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFitFontUseDimension.html), [IDimensionTolerance::GetFitFontUseScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFitFontUseScale.html), [IDimensionTolerance::GetFitFontScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFitFontScale.html), and [IDimensionTolerance::GetFitFontHeight](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFitFontHeight.html).

This method deals with the fit tolerance font information, not the tolerance font information. To get or set tolerance information, use [IDimensionTolerance::GetFontUseDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFontUseDimension.html), [IDimensionTolerance::GetFontUseScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFontUseScale.html), [IDimensionTolerance::GetFontScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFontScale.html), [IDimensionTolerance::GetFontHeight](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~GetFontHeight.html), and [IDimensionTolerance::SetFont](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimensionTolerance~SetFont.html).

To see the effects of changing the fit tolerance font information, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html).

## See Also

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.html)
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.html)
[IDimensionTolerance::FitDisplayStyle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~FitDisplayStyle.html)
[IDimensionTolerance::FitType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~FitType.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
