---
title: "ShowParenthesis Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "ShowParenthesis"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ShowParenthesis.html"
---

# ShowParenthesis Property (IDisplayDimension)

Gets or sets whether to enclose the text above the dimension line of the display dimension in parentheses.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowParenthesis As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

instance.ShowParenthesis = value

value = instance.ShowParenthesis
```

### C#

```csharp
System.bool ShowParenthesis {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowParenthesis {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enclose the text above the dimension line of the display dimension in parentheses, false to not

## VBA Syntax

See [DisplayDimension::ShowParenthesis](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~ShowParenthesis.html).

## Examples

[Get Display Dimension Properties (VBA)](Get_Display_Dimension_Properties_Example_VB.htm)

## Remarks

After using this property, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to redraw the graphics window to see your changes.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::SetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetText.html)
[IDisplayDimension::GetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetText.html)
[IDisplayDimension::ShowLowerParenthesis Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ShowLowerParenthesis.html)
