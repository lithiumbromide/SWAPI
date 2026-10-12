---
title: "Elevation Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "Elevation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Elevation.html"
---

# Elevation Property (IDisplayDimension)

Gets or sets whether to display an elevation symbol, which is controlled by [IDisplayDimension::EndSymbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~EndSymbol.html), at the end of ordinate dimension extension lines.

## Syntax

### Visual Basic (Declaration)

```vb
Property Elevation As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

instance.Elevation = value

value = instance.Elevation
```

### C#

```csharp
System.bool Elevation {get; set;}
```

### C++/CLI

```cpp
property System.bool Elevation {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display elevation symbol, false to not

## VBA Syntax

See [DisplayDimension::Elevation](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~Elevation.html).

## Examples

[Display Elevation Symbol (VBA)](Display_Elevation_Symbol_Example_VB.htm)

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::Jogged Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Jogged.html)
[IDisplayDimension::GridBubble Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GridBubble.html)
[IDisplayDimension::AutoJogOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~AutoJogOrdinate.html)
[IDisplayDimension::DisplayAsChain Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~DisplayAsChain.html)
[IModelDocExtension::AddOrdinateDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddOrdinateDimension.html)
[IDisplayDimension::GetOrdinateDimensionArrowSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetOrdinateDimensionArrowSize.html)
[IDisplayDimension::SetOrdinateDimensionArrowSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetOrdinateDimensionArrowSize.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
