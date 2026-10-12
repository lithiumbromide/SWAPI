---
title: "ShowBubbleTooltip Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "ShowBubbleTooltip"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowBubbleTooltip.html"
---

# ShowBubbleTooltip Method (ISldWorks)

Displays a bubble ToolTip and flashes the specified toolbar button.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ShowBubbleTooltip( _
   ByVal PointAt As System.Integer, _
   ByVal FlashButtonIDs As System.String, _
   ByVal TitleResID As System.Integer, _
   ByVal TitleString As System.String, _
   ByVal MessageString As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim PointAt As System.Integer
Dim FlashButtonIDs As System.String
Dim TitleResID As System.Integer
Dim TitleString As System.String
Dim MessageString As System.String

instance.ShowBubbleTooltip(PointAt, FlashButtonIDs, TitleResID, TitleString, MessageString)
```

### C#

```csharp
void ShowBubbleTooltip(
   System.int PointAt,
   System.string FlashButtonIDs,
   System.int TitleResID,
   System.string TitleString,
   System.string MessageString
)
```

### C++/CLI

```cpp
void ShowBubbleTooltip(
   System.int PointAt,
   System.String^ FlashButtonIDs,
   System.int TitleResID,
   System.String^ TitleString,
   System.String^ MessageString
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointAt`: Toolbar button ID
- `FlashButtonIDs`: Array of strings for the toolbar buttons
- `TitleResID`: Title resource ID of bubble Tooltip or 0
- `TitleString`: Title of bubble ToolTip
- `MessageString`: Message string of bubble ToolTip

## VBA Syntax

See [SldWorks::ShowBubbleTooltip](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~ShowBubbleTooltip.html).

## Examples

[Flash an Add-in's Toolbar Button (VBA)](Flash_an_Add-in_s_Toolbar_Button_Example_VB.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::ShowBubbleTooltipAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowBubbleTooltipAt2.html)

## Availability

SOLIDWORKS 2006 SP3, Revision Number 14.3
