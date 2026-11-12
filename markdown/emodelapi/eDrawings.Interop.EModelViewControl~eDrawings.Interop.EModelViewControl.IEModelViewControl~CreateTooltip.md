---
title: "CreateTooltip Method (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "CreateTooltip"
kind: "method"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CreateTooltip.html"
---

# CreateTooltip Method (IEModelViewControl)

Creates a ToolTip at the specified location.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateTooltip( _
   ByVal TipTitle As System.String, _
   ByVal TipText As System.String, _
   ByVal ShowAtMousePosition As System.Boolean, _
   ByVal XCoordinate As System.Integer, _
   ByVal YCoordinate As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim TipTitle As System.String
Dim TipText As System.String
Dim ShowAtMousePosition As System.Boolean
Dim XCoordinate As System.Integer
Dim YCoordinate As System.Integer
Dim value As System.Integer

value = instance.CreateTooltip(TipTitle, TipText, ShowAtMousePosition, XCoordinate, YCoordinate)
```

### C#

```csharp
System.int CreateTooltip(
   System.string TipTitle,
   System.string TipText,
   System.bool ShowAtMousePosition,
   System.int XCoordinate,
   System.int YCoordinate
)
```

### C++/CLI

```cpp
System.int CreateTooltip(
   System.String^ TipTitle,
   System.String^ TipText,
   System.bool ShowAtMousePosition,
   System.int XCoordinate,
   System.int YCoordinate
)
```

### Parameters

- `TipTitle`: Title for ToolTip; only the ToolTip text is displayed if you set TipTitle to an empty string ("")
- `TipText`: Text for ToolTip; only the ToolTip title is displayed if you set TipText to an empty string ("")
- `ShowAtMousePosition`: True to show the ToolTip at the cursor's location, false to show the ToolTip at the specified location
- `XCoordinate`: x coordinate for the ToolTip location
- `YCoordinate`: y coordinate for the ToolTip location

### Return Value

ID of ToolTip

## VBA Syntax

See [EModelViewControl::CreateTooltip](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~CreateTooltip.html).

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::HideAllTooltips Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~HideAllTooltips.html)
[IEModelViewControl::HideTooltip Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~HideTooltip.html)
[IEModelViewControl::ShowAllTooltips Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowAllTooltips.html)
[IEModelViewControl::ShowTooltip Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowTooltip.html)
[IEModelViewControl::ShowTipAtMousePosition Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowTipAtMousePosition.html)
[IEModelViewControl::TipText Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TipText.html)
[IEModelViewControl::TipXCoordinate Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TipXCoordinate.html)
[IEModelViewControl::TipYCoordinate Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TipYCoordinate.html)
[IEModelViewControl::TooltipCount Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TooltipCount.html)
[IEModelViewControl::TooltipID Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TooltipID.html)

## Availability

eDrawings API 2005 SP0
