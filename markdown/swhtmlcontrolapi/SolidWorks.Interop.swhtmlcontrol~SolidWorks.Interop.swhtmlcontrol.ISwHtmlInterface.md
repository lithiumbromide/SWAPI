---
title: "ISwHtmlInterface Interface"
project: "SOLIDWORKS HTML Control Type Library"
interface: "ISwHtmlInterface"
member: ""
kind: "interface"
source: "swhtmlcontrolapi/SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface.html"
---

# ISwHtmlInterface Interface

Must be implemented in each add-in's Quick Tips HTML page so that users can interact with the add-in's Quick Tips and see associated Bubble ToolTips.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwHtmlInterface
```

### Visual Basic (Usage)

```vb
Dim instance As ISwHtmlInterface
```

### C#

```csharp
public interface ISwHtmlInterface
```

### C++/CLI

```cpp
public interface class ISwHtmlInterface
```

## VBA Syntax

See [SwHtmlInterface](ms-its:swhtmlcontrolapivb6.chm::/SWHTMLCONTROLLib~SwHtmlInterface.html).

## Examples

[Show Bubble ToolTip (VBA)](Show_Bubble_ToolTip_Example_VB.htm)

## Remarks

To access this API, include the following line of code in your application. See [Quick Tips and Bubble ToolTips](ms-its:sldworksAPIProgGuide.chm::/Overview/Quick_Tips_and_Bubble_ToolTips.htm) for more information.

CreateObject('SwHtmlControl.SwHtmlInterface')

## See Also

[ISwHtmlInterface Members](SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface_members.html)
[SolidWorks.Interop.swhtmlcontrol Namespace](SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol_namespace.html)
[ISldWorks::InstallQuickTipGuide](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~InstallQuickTipGuide.html)
[ISldWorks::RefreshQuickTipWindow](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RefreshQuickTipWindow.html)
[ISldWorks::UnInstallQuickTipGuide](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~UnInstallQuickTipGuide.html)
[ISwQuickTip](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwQuickTip.html)
