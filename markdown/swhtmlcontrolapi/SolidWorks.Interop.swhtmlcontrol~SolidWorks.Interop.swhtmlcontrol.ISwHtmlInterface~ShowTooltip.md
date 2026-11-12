---
title: "ShowTooltip Method (ISwHtmlInterface)"
project: "SOLIDWORKS HTML Control Type Library"
interface: "ISwHtmlInterface"
member: "ShowTooltip"
kind: "method"
source: "swhtmlcontrolapi/SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface~ShowTooltip.html"
---

# ShowTooltip Method (ISwHtmlInterface)

Shows the Bubble ToolTip and flashes the specified toolbar or toolbar buttons.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ShowTooltip( _
   ByVal ToolbarName As System.String, _
   ByVal buttonIndex As System.Integer, _
   ByVal mask1 As System.Integer, _
   ByVal mask2 As System.Integer, _
   ByVal titleString As System.String, _
   ByVal messageString As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwHtmlInterface
Dim ToolbarName As System.String
Dim buttonIndex As System.Integer
Dim mask1 As System.Integer
Dim mask2 As System.Integer
Dim titleString As System.String
Dim messageString As System.String

instance.ShowTooltip(ToolbarName, buttonIndex, mask1, mask2, titleString, messageString)
```

### C#

```csharp
void ShowTooltip(
   System.string ToolbarName,
   System.int buttonIndex,
   System.int mask1,
   System.int mask2,
   System.string titleString,
   System.string messageString
)
```

### C++/CLI

```cpp
void ShowTooltip(
   System.String^ ToolbarName,
   System.int buttonIndex,
   System.int mask1,
   System.int mask2,
   System.String^ titleString,
   System.String^ messageString
)
```

### Parameters

- `ToolbarName`: Name of toolbar
- `buttonIndex`: 0-based index indicating a toolbar button
- `mask1`: 0-31 bitmask indicating the toolbar buttons to flash
- `mask2`: 32-63 bitmask indicating the toolbar buttons to flash
- `titleString`: Title of Bubble ToolTip
- `messageString`: Message of Bubble ToolTip

## VBA Syntax

See [SwHtmlInterface::ShowTooltip](ms-its:swhtmlcontrolapivb6.chm::/SWHTMLCONTROLLib~SwHtmlInterface~ShowTooltip.html).

## See Also

[ISwHtmlInterface Interface](SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface.html)
[ISwHtmlInterface Members](SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
