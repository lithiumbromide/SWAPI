---
title: "UnInstallQuickTipGuide Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "UnInstallQuickTipGuide"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UnInstallQuickTipGuide.html"
---

# UnInstallQuickTipGuide Method (ISldWorks)

Uninstalls your add-in's [Quick Tips](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwQuickTip.html)

## Syntax

### Visual Basic (Declaration)

```vb
Sub UnInstallQuickTipGuide( _
   ByVal PInterface As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim PInterface As System.Object

instance.UnInstallQuickTipGuide(PInterface)
```

### C#

```csharp
void UnInstallQuickTipGuide(
   System.object PInterface
)
```

### C++/CLI

```cpp
void UnInstallQuickTipGuide(
   System.Object^ PInterface
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PInterface`: Your add-in's [Quick Tips](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwQuickTip.html)

## VBA Syntax

See [SldWorks::UnInstallQuickTipGuide](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~UnInstallQuickTipGuide.html).

## Remarks

See [Quick Tips and Bubble ToopTips](sldworksAPIProgGuide.chm::/OVERVIEW/Quick_Tips_and_Bubble_ToolTips.htm) for for details.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::RefreshQuickTipWindow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RefreshQuickTipWindow.html)
[ISldWorks::InstallQuickTipGuide Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~InstallQuickTipGuide.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
