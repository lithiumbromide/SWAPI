---
title: "HideBubbleTooltip Method (ISwHtmlInterface)"
project: "SOLIDWORKS HTML Control Type Library"
interface: "ISwHtmlInterface"
member: "HideBubbleTooltip"
kind: "method"
source: "swhtmlcontrolapi/SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface~HideBubbleTooltip.html"
---

# HideBubbleTooltip Method (ISwHtmlInterface)

Hides the Bubble ToolTip displayed by [ISwHtmlInterface::ShowBubbleTooltipAt](SOLIDWORKS.Interop.swhtmlcontrol~SOLIDWORKS.Interop.swhtmlcontrol.ISwHtmlInterface~ShowBubbleTooltipAt.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub HideBubbleTooltip()
```

### Visual Basic (Usage)

```vb
Dim instance As ISwHtmlInterface

instance.HideBubbleTooltip()
```

### C#

```csharp
void HideBubbleTooltip()
```

### C++/CLI

```cpp
void HideBubbleTooltip();
```

## VBA Syntax

See [SwHtmlInterface::HideBubbleTooltip](ms-its:swhtmlcontrolapivb6.chm::/SWHTMLCONTROLLib~SwHtmlInterface~HideBubbleTooltip.html).

## Examples

**Visual Basic for Applications (VBA)**

This example shows how to display and hide a Bubble ToolTip.

```vb
'--------------------------------------------
'
' Preconditions: Substitute the path and filename of your HTML file for path_filename.
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

## See Also

[ISwHtmlInterface Interface](SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface.html)
[ISwHtmlInterface Members](SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
