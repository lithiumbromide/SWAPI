---
title: "DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler.html"
---

# DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when the active [IModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object has changed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ActiveModelDocChangeNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~ActiveModelDocChangeNotify_EV.html).

## Remarks

The active [IModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object represents the document that is currently being edited by the end-user. This notification is not sent when a part or subassembly is being edited in the context of an assembly. On receiving this event, you can call [ISldWorks::ActiveDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ActiveDoc.html) or [ISldWorks:IActiveDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~IActiveDoc2.html) to get the actual IModelDoc2 pointer.

This event is only sent when the active window in the SOLIDWORKS session actually changes to a new active model document. Window changes are not guaranteed during, for example, the shutdown of the SOLIDWORKS application. For example, if the SOLIDWORKS application closes a non-active document, there is no need to activate a new document window.

If developing a C++ application, use [swAppModelDocChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
