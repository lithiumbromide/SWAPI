---
title: "InstallQuickTipGuide Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "InstallQuickTipGuide"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~InstallQuickTipGuide.html"
---

# InstallQuickTipGuide Method (ISldWorks)

Implements your add-in's copy of the [Quick Tips](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwQuickTip.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InstallQuickTipGuide( _
   ByVal PInterface As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim PInterface As System.Object

instance.InstallQuickTipGuide(PInterface)
```

### C#

```csharp
void InstallQuickTipGuide(
   System.object PInterface
)
```

### C++/CLI

```cpp
void InstallQuickTipGuide(
   System.Object^ PInterface
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PInterface`: Your add-in's copy of the [Quick Tips](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwQuickTip.html)

## VBA Syntax

See [SldWorks::InstallQuickTipGuide](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~InstallQuickTipGuide.html).

## Remarks

The name of your add-in's Quick Tips is added to the SOLIDWORKS Help menu. See [ISwQuickTip::MenuName](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwQuickTip~MenuName.html) for details.

See [Quick Tips and Bubble ToopTips](sldworksAPIProgGuide.chm::/OVERVIEW/Quick_Tips_and_Bubble_ToolTips.htm) for for details.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::RefreshQuickTipWindow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RefreshQuickTipWindow.html)
[ISldWorks::UnInstallQuickTipGuide Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UnInstallQuickTipGuide.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
