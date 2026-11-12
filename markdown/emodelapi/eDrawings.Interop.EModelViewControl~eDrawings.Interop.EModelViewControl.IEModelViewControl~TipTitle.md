---
title: "TipTitle Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "TipTitle"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TipTitle.html"
---

# TipTitle Property (IEModelViewControl)

Gets or sets the title of the specified ToolTip.

## Syntax

### Visual Basic (Declaration)

```vb
Property TipTitle( _
   ByVal TooltipID As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim TooltipID As System.Integer
Dim value As System.String

instance.TipTitle(TooltipID) = value

value = instance.TipTitle(TooltipID)
```

### C#

```csharp
System.string TipTitle(
   System.int TooltipID
) {get; set;}
```

### C++/CLI

```cpp
property System.String^ TipTitle {
   System.String^ get(System.int TooltipID);
   void set (System.int TooltipID, System.String^ value);
}
```

### Parameters

- `TooltipID`: ID of ToolTip

### Property Value

ToolTip

## VBA Syntax

See [EModelViewControl::TipTitle](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~TipTitle.html).

## Remarks

Call [IEModelViewControl::TootipID](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TooltipID.html) to get the index number of the ToolTip.

Only the ToolTip text is displayed if you set the string to an empty string ("").

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
[IEModelViewControl::TipXCoordinate Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TipXCoordinate.html)
[IEModelViewControl::TipYCoordinate Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TipYCoordinate.html)
[IEModelViewControl::TooltipCount Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TooltipCount.html)

## Availability

eDrawings API 2005 SP0
