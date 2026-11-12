---
title: "LeaderVisibility Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "LeaderVisibility"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~LeaderVisibility.html"
---

# LeaderVisibility Property (IDisplayDimension)

Gets or sets which leader lines (dimension lines) are visible on a display dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Property LeaderVisibility As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Integer

instance.LeaderVisibility = value

value = instance.LeaderVisibility
```

### C#

```csharp
System.int LeaderVisibility {get; set;}
```

### C++/CLI

```cpp
property System.int LeaderVisibility {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Leader visibility state as defined in [swLeaderLineVisibility_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLeaderLineVisibility_e.html)

## VBA Syntax

See [DisplayDimension::LeaderVisibility](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~LeaderVisibility.html).

## Examples

[Get Display Dimension Properties (VBA)](Get_Display_Dimension_Properties_Example_VB.htm)

## Remarks

After using this property, use [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) to redraw the graphics window to see your changes.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
