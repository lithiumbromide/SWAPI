---
title: "GetText Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GetText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetText.html"
---

# GetText Method (IDisplayDimension)

Gets the text above the dimension line in a display dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetText( _
   ByVal WhichText As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim WhichText As System.Integer
Dim value As System.String

value = instance.GetText(WhichText)
```

### C#

```csharp
System.string GetText(
   System.int WhichText
)
```

### C++/CLI

```cpp
System.String^ GetText(
   System.int WhichText
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichText`: Aspect of the text to get as defined in [swDimensionTextParts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionTextParts_e.html) (see **Remarks**)

### Return Value

Text above the dimension line

## VBA Syntax

See [DisplayDimension::GetText](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GetText.html).

## Examples

[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)
[Get Dimension Values in Drawing (VBA)](Get_Dimension_Values_in_Drawing_Example_VB.htm)
[Get Whether Display Dimension is a Hole Callout (VBA)](Get_Whether_Display_Dimension_is_a_Hole_Callout_Example_VB.htm)

## Remarks

swDimensionTextParts_e.swDimensionTextAll is not a valid value for the WhichText parameter for this method.

**NOTE:** This method does not support [hole callouts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsHoleCallout.html).

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::SetText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetText.html)
[IDisplayDimension::GetLowerText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetLowerText.html)
[IDisplayDimension::SetLowerText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLowerText.html)
