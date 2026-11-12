---
title: "GridBubble Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "GridBubble"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GridBubble.html"
---

# GridBubble Property (IDisplayDimension)

Gets or sets whether to display a grid bubble at the end of ordinate dimension extension lines.

## Syntax

### Visual Basic (Declaration)

```vb
Property GridBubble As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

instance.GridBubble = value

value = instance.GridBubble
```

### C#

```csharp
System.bool GridBubble {get; set;}
```

### C++/CLI

```cpp
property System.bool GridBubble {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display a grid bubble at the end of ordinate dimension extension lines, false to not

## VBA Syntax

See [DisplayDimension::GridBubble](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~GridBubble.html).

## Examples

[Display Grid Bubble (VBA)](Display_Grid_Bubble_Example_VB.htm)

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::AutoJogOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~AutoJogOrdinate.html)
[IDisplayDimension::DisplayAsChain Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~DisplayAsChain.html)
[IDisplayDimension::Elevation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Elevation.html)
[IDisplayDimension::EndSymbol Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~EndSymbol.html)
[IDisplayDimension::Jogged Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Jogged.html)
[IDisplayDimension::GetOrdinateDimensionArrowSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetOrdinateDimensionArrowSize.html)
[IDisplayDimension::SetOrdinateDimensionArrowSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetOrdinateDimensionArrowSize.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
