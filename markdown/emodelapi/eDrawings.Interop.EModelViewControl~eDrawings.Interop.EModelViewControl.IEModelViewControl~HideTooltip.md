---
title: "HideTooltip Method (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "HideTooltip"
kind: "method"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~HideTooltip.html"
---

# HideTooltip Method (IEModelViewControl)

Hides the specified ToolTip.

## Syntax

### Visual Basic (Declaration)

```vb
Sub HideTooltip( _
   ByVal TooltipID As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim TooltipID As System.Integer

instance.HideTooltip(TooltipID)
```

### C#

```csharp
void HideTooltip(
   System.int TooltipID
)
```

### C++/CLI

```cpp
void HideTooltip(
   System.int TooltipID
)
```

### Parameters

- `TooltipID`: ID of the ToolTip

## VBA Syntax

See [EModelViewControl::HideTooltip](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~HideTooltip.html).

## Examples

See [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) examples.

## Remarks

Before calling this method, call [IEModelViewControl::TooltipID](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TooltipID.html) to determine the ID of the ToolTip to hide.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::CreateTooltip Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~CreateTooltip.html)
[IEModelViewControl::HideAllTooltips Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~HideAllTooltips.html)
[IEModelViewControl::ShowAllTooltips Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowAllTooltips.html)
[IEModelViewControl::ShowTooltip Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowTooltip.html)
[IEModelViewControl::ShowTipAtMousePosition Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowTipAtMousePosition.html)
[IEModelViewControl::TipText Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TipText.html)
[IEModelViewControl::TipTitle Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TipTitle.html)
[IEModelViewControl::TipXCoordinate Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TipXCoordinate.html)
[IEModelViewControl::TipYCoordinate Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TipYCoordinate.html)
[IEModelViewControl::TooltipCount Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TooltipCount.html)
[IEModelViewControl::TooltipID Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~TooltipID.html)

## Availability

eDrawings API 2005 SP0
