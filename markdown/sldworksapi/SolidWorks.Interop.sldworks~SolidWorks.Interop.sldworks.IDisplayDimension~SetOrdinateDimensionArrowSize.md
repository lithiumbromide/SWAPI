---
title: "SetOrdinateDimensionArrowSize Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "SetOrdinateDimensionArrowSize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetOrdinateDimensionArrowSize.html"
---

# SetOrdinateDimensionArrowSize Method (IDisplayDimension)

Sets the diameter of the circle for the arrow of the base ordinate dimension if the base ordinate dimension standard is set to DIN.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetOrdinateDimensionArrowSize( _
   ByVal UseDoc As System.Boolean, _
   ByVal ArrowSize As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim UseDoc As System.Boolean
Dim ArrowSize As System.Double

instance.SetOrdinateDimensionArrowSize(UseDoc, ArrowSize)
```

### C#

```csharp
void SetOrdinateDimensionArrowSize(
   System.bool UseDoc,
   System.double ArrowSize
)
```

### C++/CLI

```cpp
void SetOrdinateDimensionArrowSize(
   System.bool UseDoc,
   System.double ArrowSize
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseDoc`: True to use the document setting for the diameter of the circle for the arrow of the base ordinate dimension, false to use the diameter of the circle for the arrow of the base ordinate dimension set by this method if the base ordinate dimension standard is set to DIN
- `ArrowSize`: Diameter of the circle for the arrow of the base ordinate dimension if the base ordinate dimension standard is set to DIN

## VBA Syntax

See [DisplayDimension::SetOrdinateDimensionArrowSize](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~SetOrdinateDimensionArrowSize.html).

## Examples

[Create Ordinate Dimensions (C#)](Create_Ordinate_Dimensions_Example_CSharp.htm)
[Create Ordinate Dimensions (VB.NET)](Create_Ordinate_Dimensions_Example_VBNET.htm)
[Create Ordinate Dimensions (VBA)](Create_Ordinate_Dimensions_Example_VB.htm)

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IDisplayDimension::GetOrdinateDimensionArrowSize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetOrdinateDimensionArrowSize.html)
[IDisplayDimension::AutoJogOrdinate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~AutoJogOrdinate.html)
[IDisplayDimension::DisplayAsChain Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~DisplayAsChain.html)
[IDisplayDimension::Elevation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Elevation.html)
[IDisplayDimension::EndSymbol Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~EndSymbol.html)
[IDisplayDimension::GridBubble Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GridBubble.html)
[IDisplayDimension::Jogged Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Jogged.html)
[IModelDocExtension::AddOrdinateDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddOrdinateDimension.html)
[IDrawingDoc::CreateOrdinateDim4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateOrdinateDim4.html)
[IDrawingDoc::InsertOrdinate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertOrdinate.html)
[IDrawingDoc::InsertHorizontalOrdinate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertHorizontalOrdinate.html)
[IDrawingDoc::InsertVerticalOrdinate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertVerticalOrdinate.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
