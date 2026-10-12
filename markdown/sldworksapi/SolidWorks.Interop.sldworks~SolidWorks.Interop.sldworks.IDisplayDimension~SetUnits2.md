---
title: "SetUnits2 Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "SetUnits2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetUnits2.html"
---

# SetUnits2 Method (IDisplayDimension)

Sets the unit display characteristics of this display dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetUnits2( _
   ByVal UseDoc As System.Boolean, _
   ByVal UType As System.Integer, _
   ByVal FractBase As System.Integer, _
   ByVal FractDenom As System.Integer, _
   ByVal RoundToFraction As System.Boolean, _
   ByVal DecimalRounding As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim UseDoc As System.Boolean
Dim UType As System.Integer
Dim FractBase As System.Integer
Dim FractDenom As System.Integer
Dim RoundToFraction As System.Boolean
Dim DecimalRounding As System.Integer
Dim value As System.Integer

value = instance.SetUnits2(UseDoc, UType, FractBase, FractDenom, RoundToFraction, DecimalRounding)
```

### C#

```csharp
System.int SetUnits2(
   System.bool UseDoc,
   System.int UType,
   System.int FractBase,
   System.int FractDenom,
   System.bool RoundToFraction,
   System.int DecimalRounding
)
```

### C++/CLI

```cpp
System.int SetUnits2(
   System.bool UseDoc,
   System.int UType,
   System.int FractBase,
   System.int FractDenom,
   System.bool RoundToFraction,
   System.int DecimalRounding
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseDoc`: True to use the document settings for units, false to use the setting values passed to this method (see **Remarks**)
- `UType`: Unit display setting as defined in [swLengthUnit_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLengthUnit_e.html) or [swAngleUnit_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAngleUnit_e.html); valid only if UseDoc is false
- `FractBase`: Decimal or fraction display setting as defined in [swFractionDisplay_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFractionDisplay_e.html); valid only if UseDoc is false
- `FractDenom`: Denominator for fraction display; valid only if UseDoc is false
- `RoundToFraction`: True to round values to the nearest fraction, false to display fractions only if the values are exact; valid only if UseDoc is false
- `DecimalRounding`: Decimal rounding as defined by [swUnitsDecimalRounding_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUnitsDecimalRounding_e.html); valid only if FractBase is swFractionDisplay_e.swDECIMAL and UseDoc is false

### Return Value

Return status (see Remarks)

## VBA Syntax

See [DisplayDimension::SetUnits2](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~SetUnits2.html).

## Examples

[Set Rounding of Decimal Units in Display Dimensions (VBA)](Set_Rounding_of_Decimal_Units_in_Display_Dimensions_Example_VB.htm)
[Set Rounding of Decimal Units in Display Dimensions (VB.NET)](Set_Rounding_of_Decimal_Units_in_Display_Dimensions_Example_VBNET.htm)
[Set Rounding of Decimal Units in Display Dimensions (C#)](Set_Rounding_of_Decimal_Units_in_Display_Dimensions_Example_CSharp.htm)

## Remarks

The unit display settings of a display dimension are controlled by a value stored in one of two places: in the owning document or in the individual display dimension. This method allows you to determine which setting to use, the document default or the values specified by UType, FractBase, FractDenom, RoundToFraction, and DecimalRounding.

If UseDoc is true, then the display dimension unit information follows the document settings, and SOLIDWORKS ignores the remaining arguments. SOLIDWORKS also removes any local settings so that if you switch back to the local settings, they are set to default values.

UType indicates the units. Depending on the type of dimension (angular or linear), this parameter takes a value from [swLengthUnit_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLengthUnit_e.html) or [swAngleUnit_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAngleUnit_e.html). If the specified value is invalid, SOLIDWORKS does not change the existing setting, and this method returns an error.

FractBase indicates whether the dimension is displayed as a fraction or a decimal. SOLIDWORKS displays the dimension as a fraction only if it can precisely represent the dimension as a fraction based on the FractDenom setting. However, if the RoundToFraction argument is true, then SOLIDWORKS displays the dimension rounded to the nearest fraction.

FractDenom indicates the fraction precision by specifying the largest fraction denominator used (for example, 4 for 1/4 or 32 for 1/32). Fraction display is valid only if UType is swINCHES or swFEETINCHES.

The return value indicates the success or failure of this method as follows:

| If Return Value is... | Then this method... |
| --- | --- |
| 2 | Failed because UType is invalid |
| 1 | Failed for an unknown reason |
| 0 | Succeeded |

After using this method, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to redraw the graphics window to see your changes.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetUnits Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUnits.html)
[IDisplayDimension::GetUseDocUnits Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocUnits.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
