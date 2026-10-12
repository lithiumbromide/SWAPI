---
title: "TipText Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "TipText"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TipText.html"
---

# TipText Property (IEModelViewControl)

Gets or sets the text for the specified ToolTip.

## Syntax

### Visual Basic (Declaration)

```vb
Property TipText( _
   ByVal TooltipID As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim TooltipID As System.Integer
Dim value As System.String

instance.TipText(TooltipID) = value

value = instance.TipText(TooltipID)
```

### C#

```csharp
System.string TipText(
   System.int TooltipID
) {get; set;}
```

### C++/CLI

```cpp
property System.String^ TipText {
   System.String^ get(System.int TooltipID);
   void set (System.int TooltipID, System.String^ value);
}
```

### Parameters

- `TooltipID`: ID of ToolTip

### Property Value

Text for ToolTip

## VBA Syntax

See [EModelViewControl::TipText](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~TipText.html).

## Remarks

Call [IEModelViewControl::TootipID](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TooltipID.html) to get the index number of the ToolTip.

Only the ToolTip title is displayed if you set the string to an empty string ("").

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::CreateTooltip Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CreateTooltip.html)
[IEModelViewControl::HideAllTooltips Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~HideAllTooltips.html)
[IEModelViewControl::HideTooltip Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~HideTooltip.html)
[IEModelViewControl::ShowAllTooltips Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowAllTooltips.html)
[IEModelViewControl::ShowTooltip Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowTooltip.html)
[IEModelViewControl::ShowTipAtMousePosition Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowTipAtMousePosition.html)
[IEModelViewControl::TipTitle Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TipTitle.html)
[IEModelViewControl::TipXCoordinate Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TipXCoordinate.html)
[IEModelViewControl::TipYCoordinate Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TipYCoordinate.html)
[IEModelViewControl::TooltipCount Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TooltipCount.html)

## Availability

eDrawings API 2005 SP0
