---
title: "ShowBubbleTooltipAt Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "ShowBubbleTooltipAt"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowBubbleTooltipAt.html"
---

# ShowBubbleTooltipAt Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::ShowBubbleTooltipAt2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ShowBubbleTooltipAt2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ShowBubbleTooltipAt( _
   ByVal PointX As System.Integer, _
   ByVal PointY As System.Integer, _
   ByVal ArrowPos As System.Integer, _
   ByVal TitleString As System.String, _
   ByVal MessageString As System.String, _
   ByVal UrlLoc As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim PointX As System.Integer
Dim PointY As System.Integer
Dim ArrowPos As System.Integer
Dim TitleString As System.String
Dim MessageString As System.String
Dim UrlLoc As System.String

instance.ShowBubbleTooltipAt(PointX, PointY, ArrowPos, TitleString, MessageString, UrlLoc)
```

### C#

```csharp
void ShowBubbleTooltipAt(
   System.int PointX,
   System.int PointY,
   System.int ArrowPos,
   System.string TitleString,
   System.string MessageString,
   System.string UrlLoc
)
```

### C++/CLI

```cpp
void ShowBubbleTooltipAt(
   System.int PointX,
   System.int PointY,
   System.int ArrowPos,
   System.String^ TitleString,
   System.String^ MessageString,
   System.String^ UrlLoc
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointX`: x coordinate in pixels relative to upper-left corner of screen
- `PointY`: y coordinate in pixels relative to upper-left corner of screen
- `ArrowPos`: Arrow position as defined in [swArrowPosition](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowPosition.html)
- `TitleString`: Title of bubble ToolTip
- `MessageString`: Message string of bubble ToolTip
- `UrlLoc`: Any valid Windows Internet Explorer file (see **Remarks**)

## VBA Syntax

See [SldWorks::ShowBubbleTooltipAt](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~ShowBubbleTooltipAt.html).

## Examples

**Visual Basic for Applications (VBA)**

'--------------------------------------------
'
' Preconditions: Specified HTML file exists at the specified location.
'
' Postconditions: Contents of the HTML file are displayed in a Bubble ToolTip.
'
'--------------------------------------------

Option Explicit

Sub main()

' Substitute a valid HTML file for the string shown below

Const sURLpath As String = "`path_to_a_gif_jpg_or_jpeg_file_or_a_URL`"

Dim swApp As SldWorks.SldWorks
Set swApp = Application.SldWorks

' Show Bubble ToolTip
swApp.**ShowBubbleTooltipAt** 300, 400, swArrowLeftTop, "Sample ShowBubbleTooltipAt", "Message of Sample ShowBubbleTooltipAt", sURLpath

End Sub

'--------------------------------------------

## Remarks

| If you specified a ... | Then the ToolTip's bubble... |
| --- | --- |
| gif, .jpg, or .jpeg image for urlLoc | Is automatically expanded to accommodate the image |
| URL for urlLoc | Cannot be resized; if the URL is: an HTML file, then the contents of the HTML file are displayed in the bubble ToolTip to a website, then the default or specified web page at that website is displayed in the bubble ToolTip |

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::ShowBubbleTooltip Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowBubbleTooltip.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
