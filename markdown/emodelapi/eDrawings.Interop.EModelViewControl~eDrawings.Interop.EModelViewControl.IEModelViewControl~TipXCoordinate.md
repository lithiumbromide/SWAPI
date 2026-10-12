---
title: "TipXCoordinate Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "TipXCoordinate"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TipXCoordinate.html"
---

# TipXCoordinate Property (IEModelViewControl)

Gets or sets the x coordinate for the specified ToolTip.

## Syntax

### Visual Basic (Declaration)

```vb
Property TipXCoordinate( _
   ByVal TooltipID As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim TooltipID As System.Integer
Dim value As System.Integer

instance.TipXCoordinate(TooltipID) = value

value = instance.TipXCoordinate(TooltipID)
```

### C#

```csharp
System.int TipXCoordinate(
   System.int TooltipID
) {get; set;}
```

### C++/CLI

```cpp
property System.int TipXCoordinate {
   System.int get(System.int TooltipID);
   void set (System.int TooltipID, System.int value);
}
```

### Parameters

- `TooltipID`: ID of ToolTip

### Property Value

x coordinate for ToolTip

## VBA Syntax

See [EModelViewControl::TipXCoordinate](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~TipXCoordinate.html).

## Remarks

Call [IEModelViewControl::TootipID](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TooltipID.html) to get the index number of the ToolTip.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::CreateTooltip Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CreateTooltip.html)
[IEModelViewControl::HideAllTooltips Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~HideAllTooltips.html)
[IEModelViewControl::HideTooltip Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~HideTooltip.html)
[IEModelViewControl::ShowAllTooltips Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowAllTooltips.html)
[IEModelViewControl::ShowTooltip Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowTooltip.html)
[IEModelViewControl::ShowTipAtMousePosition Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowTipAtMousePosition.html)
[IEModelViewControl::TipText Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TipText.html)
[IEModelViewControl::TipTitle Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TipTitle.html)
[IEModelViewControl::TipYCoordinate Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TipYCoordinate.html)
[IEModelViewControl::TooltipCount Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TooltipCount.html)

## Availability

eDrawings API 2005 SP0
