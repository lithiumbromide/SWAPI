---
title: "JogDimension Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "JogDimension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~JogDimension.html"
---

# JogDimension Method (IModelDocExtension)

Gets or sets whether jog points are on or off on an interactively selected linear or ordinate dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function JogDimension( _
   ByVal Jog As System.Boolean, _
   ByVal WitnessIndex As System.Short _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Jog As System.Boolean
Dim WitnessIndex As System.Short
Dim value As System.Boolean

value = instance.JogDimension(Jog, WitnessIndex)
```

### C#

```csharp
System.bool JogDimension(
   System.bool Jog,
   System.short WitnessIndex
)
```

### C++/CLI

```cpp
System.bool JogDimension(
   System.bool Jog,
   System.short WitnessIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Jog`: True if jog points are on, false if not
- `WitnessIndex`: Index, 0 or 1, of linear dimension extension line; ignored if an ordinate dimension

### Return Value

True if operation succeeds, false if it fails

## VBA Syntax

See [ModelDocExtension::JogDimension](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~JogDimension.html).

## Examples

[Add and Offset Dimension Extension Lines Jogs (VBA)](Add_and_Offset_Dimension_Extension_Lines_Jogs_Example_VB.htm)

## Remarks

This method is equivalent to clicking the right-mouse button on a linear or ordinate dimension in the SOLIDWORKS Design user-interface, selecting **Display** **Options** on the shortcut menu, and selecting **Jog**.

Call [IModelView::GraphicsRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GraphicsRedraw.html) after setting jog points to redraw the graphics area.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IDisplayDimension::GetJogParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetJogParameters.html)
[IDisplayDimension::SetJogParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetJogParameters.html)
[IDisplayDimension::Jogged Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Jogged.html)
[IModelDocExtension::AddOrdinateDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddOrdinateDimension.html)
[IDisplayDimension::AutoJogOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~AutoJogOrdinate.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
