---
title: "Type2 Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "Type2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Type2.html"
---

# Type2 Property (IDisplayDimension)

Gets the type of dimension.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Type2 As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Integer

value = instance.Type2
```

### C#

```csharp
System.int Type2 {get;}
```

### C++/CLI

```cpp
property System.int Type2 {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of dimension as defined by [swDimensionType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionType_e.html)

## VBA Syntax

See [DisplayDimension::Type2](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~Type2.html).

## Examples

[Get Chamfer Display Dimension (C#)](Get_Chamfer_Display_Dimension_Example_CSharp.htm)
[Get Chamfer Display Dimension (VB.NET)](Get_Chamfer_Display_Dimension_Example_VBNET.htm)
[Get Chamfer Display Dimension (VBA)](Get_Chamfer_Display_Dimension_Example_VB.htm)
[Get DimXpert Display Dimensions and Feature (C#)](Get_DimXpert_Display_Dimensions_and_Feature_Example_CSharp.htm)
[Get DimXpert Display Dimensions and Feature (VB.NET)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VBNET.htm)
[Get DimXpert Display Dimensions and Feature (VBA)](Get_DimXpert_Display_Dimensions_and_Feature_Example_VB.htm)

## Remarks

After using this property, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to redraw the graphics window to see your changes.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetType.html)
[IDisplayDimension::Diametric Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Diametric.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
