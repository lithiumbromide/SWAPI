---
title: "RefreshQuickTipWindow Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "RefreshQuickTipWindow"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RefreshQuickTipWindow.html"
---

# RefreshQuickTipWindow Method (ISldWorks)

Tells the SOLIDWORKS Design application that your add-in's state has changed and triggers a query for the current URL page.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RefreshQuickTipWindow()
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks

instance.RefreshQuickTipWindow()
```

### C#

```csharp
void RefreshQuickTipWindow()
```

### C++/CLI

```cpp
void RefreshQuickTipWindow();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [SldWorks::RefreshQuickTipWindow](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~RefreshQuickTipWindow.html).

## Remarks

See [Quick Tips and Bubble ToopTips](sldworksAPIProgGuide.chm::/OVERVIEW/Quick_Tips_and_Bubble_ToolTips.htm) for for details.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::InstallQuickTipGuide Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~InstallQuickTipGuide.html)
[ISldWorks::UnInstallQuickTipGuide Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UnInstallQuickTipGuide.html)

## Availability

SOLIDWORKS 2005 FCS, Revision number 13.0
