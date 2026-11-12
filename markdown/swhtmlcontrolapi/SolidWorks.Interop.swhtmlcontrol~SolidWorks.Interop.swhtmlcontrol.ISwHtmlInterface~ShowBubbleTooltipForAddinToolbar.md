---
title: "ShowBubbleTooltipForAddinToolbar Method (ISwHtmlInterface)"
project: "SOLIDWORKS HTML Control Type Library"
interface: "ISwHtmlInterface"
member: "ShowBubbleTooltipForAddinToolbar"
kind: "method"
source: "swhtmlcontrolapi/SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface~ShowBubbleTooltipForAddinToolbar.html"
---

# ShowBubbleTooltipForAddinToolbar Method (ISwHtmlInterface)

Displays a Bubble Tooltip for the specified add-in and flashes the specified toolbar button.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ShowBubbleTooltipForAddinToolbar( _
   ByVal addInCLSID As System.String, _
   ByVal pointAt_UserID As System.Integer, _
   ByVal flashButton_UserIDs As System.String, _
   ByVal titleResID As System.Integer, _
   ByVal titleString As System.String, _
   ByVal messageString As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwHtmlInterface
Dim addInCLSID As System.String
Dim pointAt_UserID As System.Integer
Dim flashButton_UserIDs As System.String
Dim titleResID As System.Integer
Dim titleString As System.String
Dim messageString As System.String

instance.ShowBubbleTooltipForAddinToolbar(addInCLSID, pointAt_UserID, flashButton_UserIDs, titleResID, titleString, messageString)
```

### C#

```csharp
void ShowBubbleTooltipForAddinToolbar(
   System.string addInCLSID,
   System.int pointAt_UserID,
   System.string flashButton_UserIDs,
   System.int titleResID,
   System.string titleString,
   System.string messageString
)
```

### C++/CLI

```cpp
void ShowBubbleTooltipForAddinToolbar(
   System.String^ addInCLSID,
   System.int pointAt_UserID,
   System.String^ flashButton_UserIDs,
   System.int titleResID,
   System.String^ titleString,
   System.String^ messageString
)
```

### Parameters

- `addInCLSID`: Add-in's class ID
- `pointAt_UserID`: Toolbar button ID to which to point
- `flashButton_UserIDs`: Array of toolbar buttons
- `titleResID`: Title resource ID of Bubble Tooltip or 0
- `titleString`: Title of Bubble ToolTip
- `messageString`: Message string of Bubble ToolTip

## VBA Syntax

See [SwHtmlInterface::ShowBubbleTooltipForAddinToolbar](ms-its:swhtmlcontrolapivb6.chm::/SWHTMLCONTROLLib~SwHtmlInterface~ShowBubbleTooltipForAddinToolbar.html).

## See Also

[ISwHtmlInterface Interface](SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface.html)
[ISwHtmlInterface Members](SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface_members.html)
[ISldWorks::ShowBubbleTooltip](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ShowBubbleTooltip.html)
[ISwHtmlInterface::GetCommandID Method](SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface~GetCommandID.html)
[ISwHtmlInterface::ShowBubbleTooltip Method](SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface~ShowBubbleTooltip.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
