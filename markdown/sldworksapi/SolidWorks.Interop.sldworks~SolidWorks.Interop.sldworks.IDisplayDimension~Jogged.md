---
title: "Jogged Property (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "Jogged"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Jogged.html"
---

# Jogged Property (IDisplayDimension)

Gets or sets whether this ordinate or angular running dimension is jogged.

## Syntax

### Visual Basic (Declaration)

```vb
Property Jogged As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim value As System.Boolean

instance.Jogged = value

value = instance.Jogged
```

### C#

```csharp
System.bool Jogged {get; set;}
```

### C++/CLI

```cpp
property System.bool Jogged {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if dimension is jogged, false if it is not

## VBA Syntax

See [DisplayDimension::Jogged](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~Jogged.html).

## Examples

[Insert Angular Running Dimension (VBA)](Set_Properties_of_Angular_Running_Dimension_Example_VB.htm)
[Insert Angular Running Dimension (VB.NET)](Set_Properties_of_Angular_Running_Dimension_Example_VBNET.htm)
[Insert Angular Running Dimension (C#)](Set_Properties_of_Angular_Running_Dimension_Example_CSharp.htm)

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::AutoJogOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~AutoJogOrdinate.html)
[IDisplayDimension::DisplayAsChain Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~DisplayAsChain.html)
[IDisplayDimension::Elevation Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Elevation.html)
[IDisplayDimension::EndSymbol Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~EndSymbol.html)
[IDisplayDimension::GridBubble Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GridBubble.html)
[IDisplayDimension::ExtensionLineExtendsFromCenterOfSet Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineExtendsFromCenterOfSet.html)
[IDisplayDimension::RunBidirectionally Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~RunBidirectionally.html)
[IDisplayDimension::ExtensionLineSameAsLeaderStyle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineSameAsLeaderStyle.html)
[IDisplayDimension::ExtensionLineUseDocumentDisplay Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ExtensionLineUseDocumentDisplay.html)
[IDisplayDimension::ResetExtensionLineStyle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ResetExtensionLineStyle.html)
[IModelDocExtension::AddOrdinateDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddOrdinateDimension.html)
[IDisplayDimension::SetOrdinateDimensionArrowSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetOrdinateDimensionArrowSize.html)
[IDisplayDimension::GetOrdinateDimensionArrowSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetOrdinateDimensionArrowSize.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
