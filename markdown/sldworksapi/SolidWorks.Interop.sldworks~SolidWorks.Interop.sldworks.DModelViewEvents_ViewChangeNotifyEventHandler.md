---
title: "DModelViewEvents_ViewChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DModelViewEvents_ViewChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_ViewChangeNotifyEventHandler.html"
---

# DModelViewEvents_ViewChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when a view is altered and returns the new transform matrix of the view.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DModelViewEvents_ViewChangeNotifyEventHandler( _
   ByVal View As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DModelViewEvents_ViewChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DModelViewEvents_ViewChangeNotifyEventHandler(
   System.object View
)
```

### C++/CLI

```cpp
public delegate System.int DModelViewEvents_ViewChangeNotifyEventHandler(
   System.Object^ View
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `View`: See **Remarks**

## VBA Syntax

See [ViewChangeNotify Event (ModelView)](ms-its:sldworksapivb6.chm::/SldWorks~ModelView~ViewChangeNotify_EV.html).

## Remarks

In Visual Basic for Applications (VBA), the view argument is a VARIANT of type SafeArray of 16 doubles:

| Elements | Values |
| --- | --- |
| First 9 | Standard 3x3 rotation matrix |
| Next 3 | Define translation |
| Next 1 | For scaling |
| Last 3 | Not used |

Your application is responsible for destroying the SafeArray when you are finished with it.

If developing a C++ application, use [swViewChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
