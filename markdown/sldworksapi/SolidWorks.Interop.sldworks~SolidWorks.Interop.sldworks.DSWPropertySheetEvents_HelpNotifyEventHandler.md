---
title: "DSWPropertySheetEvents_HelpNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSWPropertySheetEvents_HelpNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSWPropertySheetEvents_HelpNotifyEventHandler.html"
---

# DSWPropertySheetEvents_HelpNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the Help button is clicked on a property sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSWPropertySheetEvents_HelpNotifyEventHandler( _
   ByVal PageIndex As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSWPropertySheetEvents_HelpNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSWPropertySheetEvents_HelpNotifyEventHandler(
   System.int PageIndex
)
```

### C++/CLI

```cpp
public delegate System.int DSWPropertySheetEvents_HelpNotifyEventHandler(
   System.int PageIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PageIndex`: Page index of the add-in's Help

## VBA Syntax

See [HelpNotify Event (SWPropertySheet)](ms-its:sldworksapivb6.chm::/SldWorks~SWPropertySheet~HelpNotify_EV.html).

## Remarks

Your application should only display Help if you have added a Help page.

For add-ins, if PageIndex is the same as the value returned by [ISWPropertySheet::AddActivePage](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISWPropertySheet~AddActivePage.html), then the add-in can display its Help.

If developing a C++ application, use [swPropertySheetHelpNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertySheetNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
