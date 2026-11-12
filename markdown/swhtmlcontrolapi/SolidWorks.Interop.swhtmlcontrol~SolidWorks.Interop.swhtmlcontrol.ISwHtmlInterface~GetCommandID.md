---
title: "GetCommandID Method (ISwHtmlInterface)"
project: "SOLIDWORKS HTML Control Type Library"
interface: "ISwHtmlInterface"
member: "GetCommandID"
kind: "method"
source: "swhtmlcontrolapi/SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface~GetCommandID.html"
---

# GetCommandID Method (ISwHtmlInterface)

Gets the SOLIDWORKS resource ID for an add-in's [CommandManager](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager.html)-style toolbar button.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCommandID( _
   ByVal ClsID As System.String, _
   ByVal UserCmdID As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwHtmlInterface
Dim ClsID As System.String
Dim UserCmdID As System.Integer
Dim value As System.Integer

value = instance.GetCommandID(ClsID, UserCmdID)
```

### C#

```csharp
System.int GetCommandID(
   System.string ClsID,
   System.int UserCmdID
)
```

### C++/CLI

```cpp
System.int GetCommandID(
   System.String^ ClsID,
   System.int UserCmdID
)
```

### Parameters

- `ClsID`: Add-in's class ID
- `UserCmdID`: Unique ID that the add-in application identified as a CommandManager-style toolbar button

### Return Value

Currently bound ID for the CommandManager-style toolbar button

## VBA Syntax

See [SwHtmlInterface::GetCommandID](ms-its:swhtmlcontrolapivb6.chm::/SWHTMLCONTROLLib~SwHtmlInterface~GetCommandID.html).

## Examples

[Flash an Add-in's Toolbar Button (VBA)](Flash_an_Add-in_s_Toolbar_Button_Example_VB.htm)

## See Also

[ISwHtmlInterface Interface](SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface.html)
[ISwHtmlInterface Members](SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface_members.html)
[ISldWorks::ShowBubbleToolTip](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ShowBubbleToolTip.html)
[ISwHtmlInterface::ShowBubbleTooltip Method](SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface~ShowBubbleTooltip.html)
[ISwHtmlInterface::ShowBubbleTooltipForAddinToolbar Method](SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface~ShowBubbleTooltipForAddinToolbar.html)

## Availability

SOLIDWORKS 2006 SP3, Revision Number 14.3
