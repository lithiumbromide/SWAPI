---
title: "SetJogParameters Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "SetJogParameters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetJogParameters.html"
---

# SetJogParameters Method (IDisplayDimension)

Set the linear dimension extension line to be jogged.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetJogParameters( _
   ByVal WitnessIndex As System.Short, _
   ByVal Jogged As System.Boolean, _
   ByVal Offset1 As System.Double, _
   ByVal Offset2 As System.Double, _
   ByVal Offset1to2 As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim WitnessIndex As System.Short
Dim Jogged As System.Boolean
Dim Offset1 As System.Double
Dim Offset2 As System.Double
Dim Offset1to2 As System.Double
Dim value As System.Boolean

value = instance.SetJogParameters(WitnessIndex, Jogged, Offset1, Offset2, Offset1to2)
```

### C#

```csharp
System.bool SetJogParameters(
   System.short WitnessIndex,
   System.bool Jogged,
   System.double Offset1,
   System.double Offset2,
   System.double Offset1to2
)
```

### C++/CLI

```cpp
System.bool SetJogParameters(
   System.short WitnessIndex,
   System.bool Jogged,
   System.double Offset1,
   System.double Offset2,
   System.double Offset1to2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WitnessIndex`: Index of the linear dimension extension line to jog
- `Jogged`: True whether the linear dimension extension is jogged, false if not
- `Offset1`: First line segment of the linear dimension extension line
- `Offset2`: Second line segment of the linear dimension extension line; this is the line segment to jog
- `Offset1to2`: Distance by which to offset Offset1 and Offset2 for the jog

## VBA Syntax

See [DisplayDimension::SetJogParameters](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~SetJogParameters.html).

## Examples

[Add and Offset Dimension Lines Jogs (VBA)](Add_and_Offset_Dimension_Extension_Lines_Jogs_Example_VB.htm)

## Remarks

Call [IModelView::GraphicsRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GraphicsRedraw.html) after calling this method to redraw the graphics area.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
[IModelDocExtension::JogDimension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~JogDimension.html)
[IDisplayDimension::GetJogParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetJogParameters.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
