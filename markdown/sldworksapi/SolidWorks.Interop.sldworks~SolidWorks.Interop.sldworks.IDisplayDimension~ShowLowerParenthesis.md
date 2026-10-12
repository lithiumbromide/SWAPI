---
title: "ShowLowerParenthesis Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "ShowLowerParenthesis"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ShowLowerParenthesis.html"
---

# ShowLowerParenthesis Property (IDisplayDimension)

Gets or sets whether to enclose the text below the dimension line of the display dimension in parentheses.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowLowerParenthesis As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

instance.ShowLowerParenthesis = value

value = instance.ShowLowerParenthesis
```

### C#

```csharp
System.bool ShowLowerParenthesis {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowLowerParenthesis {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enclose the text below the dimension line of the display dimension in parentheses, false to not

## VBA Syntax

See [DisplayDimension::ShowLowerParenthesis](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~ShowLowerParenthesis.html).

## Examples

[Get Chamfer Display Dimension (C#)](Get_Chamfer_Display_Dimension_Example_CSharp.htm)
[Get Chamfer Display Dimension (VB.NET)](Get_Chamfer_Display_Dimension_Example_VBNET.htm)
[Get Chamfer Display Dimension (VBA)](Get_Chamfer_Display_Dimension_Example_VB.htm)

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetLowerText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetLowerText.html)
[IDisplayDimension::SetLowerText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLowerText.html)
[IDisplayDimension::ShowParenthesis Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ShowParenthesis.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
