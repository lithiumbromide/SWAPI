---
title: "ShowDimensionValue Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "ShowDimensionValue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ShowDimensionValue.html"
---

# ShowDimensionValue Property (IDisplayDimension)

Gets or sets whether the dimension value is displayed as part of the dimension text.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowDimensionValue As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

instance.ShowDimensionValue = value

value = instance.ShowDimensionValue
```

### C#

```csharp
System.bool ShowDimensionValue {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowDimensionValue {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True displays the dimension value, false does not

## VBA Syntax

See [DisplayDimension::ShowDimensionValue](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~ShowDimensionValue.html).

## Examples

[Get Display Dimension Properties (VBA)](Get_Display_Dimension_Properties_Example_VB.htm)

## Remarks

After using this property, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to redraw the graphics window to see your changes.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::SetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetText.html)
[IDisplayDimension::GetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetText.html)
