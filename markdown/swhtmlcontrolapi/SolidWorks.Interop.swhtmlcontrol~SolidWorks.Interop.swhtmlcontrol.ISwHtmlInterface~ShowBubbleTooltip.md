---
title: "ShowBubbleTooltip Method (ISwHtmlInterface)"
project: "SOLIDWORKS HTML Control Type Library"
interface: "ISwHtmlInterface"
member: "ShowBubbleTooltip"
kind: "method"
source: "swhtmlcontrolapi/SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface~ShowBubbleTooltip.html"
---

# ShowBubbleTooltip Method (ISwHtmlInterface)

Displays a Bubble ToolTip and flashes the specified toolbar button.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ShowBubbleTooltip( _
   ByVal pointAt As System.Integer, _
   ByVal flashButtonIDs As System.String, _
   ByVal titleResID As System.Integer, _
   ByVal titleString As System.String, _
   ByVal messageString As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwHtmlInterface
Dim pointAt As System.Integer
Dim flashButtonIDs As System.String
Dim titleResID As System.Integer
Dim titleString As System.String
Dim messageString As System.String

instance.ShowBubbleTooltip(pointAt, flashButtonIDs, titleResID, titleString, messageString)
```

### C#

```csharp
void ShowBubbleTooltip(
   System.int pointAt,
   System.string flashButtonIDs,
   System.int titleResID,
   System.string titleString,
   System.string messageString
)
```

### C++/CLI

```cpp
void ShowBubbleTooltip(
   System.int pointAt,
   System.String^ flashButtonIDs,
   System.int titleResID,
   System.String^ titleString,
   System.String^ messageString
)
```

### Parameters

- `pointAt`: Toolbar button ID to which to point
- `flashButtonIDs`: Array of toolbar buttons
- `titleResID`: Title resource ID of Bubble Tooltip or 0
- `titleString`: Title of Bubble ToolTip
- `messageString`: Message string of Bubble ToolTip

## VBA Syntax

See [SwHtmlInterface::ShowBubbleTooltip](ms-its:swhtmlcontrolapivb6.chm::/SWHTMLCONTROLLib~SwHtmlInterface~ShowBubbleTooltip.html).

## Examples

[Flash an Add-in's Toolbar Button (VBA)](Flash_an_Add-in_s_Toolbar_Button_Example_VB.htm)

## See Also

[ISwHtmlInterface Interface](SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface.html)
[ISwHtmlInterface Members](SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface_members.html)

## Availability

SOLIDWORKS 2006 SP3, Revision Number 14.3
