---
title: "ShowBubbleTooltipAt Method (ISwHtmlInterface)"
project: "SOLIDWORKS HTML Control Type Library"
interface: "ISwHtmlInterface"
member: "ShowBubbleTooltipAt"
kind: "method"
source: "swhtmlcontrolapi/SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface~ShowBubbleTooltipAt.html"
---

# ShowBubbleTooltipAt Method (ISwHtmlInterface)

Displays a Bubble ToolTip at the specified location.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ShowBubbleTooltipAt( _
   ByVal pointX As System.Integer, _
   ByVal pointY As System.Integer, _
   ByVal arrowPos As System.Integer, _
   ByVal titleString As System.String, _
   ByVal messageString As System.String, _
   ByVal urlLoc As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwHtmlInterface
Dim pointX As System.Integer
Dim pointY As System.Integer
Dim arrowPos As System.Integer
Dim titleString As System.String
Dim messageString As System.String
Dim urlLoc As System.String

instance.ShowBubbleTooltipAt(pointX, pointY, arrowPos, titleString, messageString, urlLoc)
```

### C#

```csharp
void ShowBubbleTooltipAt(
   System.int pointX,
   System.int pointY,
   System.int arrowPos,
   System.string titleString,
   System.string messageString,
   System.string urlLoc
)
```

### C++/CLI

```cpp
void ShowBubbleTooltipAt(
   System.int pointX,
   System.int pointY,
   System.int arrowPos,
   System.String^ titleString,
   System.String^ messageString,
   System.String^ urlLoc
)
```

### Parameters

- `pointX`: x coordinate in pixels relative to upper-left corner of screen
- `pointY`: y coordinate in pixels relative to upper-left corner of screen
- `arrowPos`: Arrow position as defined in [swArrowPosition_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowPosition.html)
- `titleString`: Title of Bubble ToolTip
- `messageString`: Message string of Bubble ToolTip
- `urlLoc`: Any valid Windows Internet Explorer file

## VBA Syntax

See [SwHtmlInterface::ShowBubbleTooltipAt](ms-its:swhtmlcontrolapivb6.chm::/SWHTMLCONTROLLib~SwHtmlInterface~ShowBubbleTooltipAt.html).

## Examples

**Visual Basic for Applications (VBA)**

This example shows how to display and hide a Bubble ToolTip.

```vb
'--------------------------------------------
'
' Preconditions: Substitute the path and filename of your HTML file for "path_filename".
'
' Postconditions: Contents of the HTML file are displayed in a Bubble ToolTip,
'                 and then are hidden from view.
'
'--------------------------------------------
Option Explicit

Sub main()
    Const sURLpath As String = "path_filename"
    Dim pSldWorks As Object

    Set pSldWorks = CreateObject("SwHtmlControl.SwHtmlInterface")

    ' Show Bubble ToolTip
    pSldWorks.ShowBubbleTooltipAt 300, 400, swArrowLeftTop, "Sample Bubble ToolTip", "Message of Sample Bubble ToolTip", sURLpath

    Stop

    ' Hide Bubble ToolTip
    pSldWorks.HidebubbleTooltip

End Sub
'--------------------------------------------
```

## Examples

[Show Bubble ToolTip (VBA)](Show_Bubble_ToolTip_Example_VB.htm)

## Remarks

Remarks

| If you specified a ... | Then the ToolTip's bubble... |
| --- | --- |
| gif, .jpg, or .jpeg image for urlLoc | Is automatically expanded to accommodate the image |
| URL for urlLoc | Cannot be resized and shows only the URL |

## See Also

[ISwHtmlInterface Interface](SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface.html)
[ISwHtmlInterface Members](SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface_members.html)
[ISwHtmlInterface::ShowTooltip Method](SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface~ShowTooltip.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
