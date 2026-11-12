---
title: "DModelViewEvents_PrintNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DModelViewEvents_PrintNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_PrintNotifyEventHandler.html"
---

# DModelViewEvents_PrintNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Obsolete. Superseded by [DModelViewEvents_PrintNotify2EventHandler](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DModelViewEvents_PrintNotify2EventHandler.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DModelViewEvents_PrintNotifyEventHandler( _
   ByVal pDC As System.Long _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DModelViewEvents_PrintNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DModelViewEvents_PrintNotifyEventHandler(
   System.long pDC
)
```

### C++/CLI

```cpp
public delegate System.int DModelViewEvents_PrintNotifyEventHandler(
   System.int64 pDC
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `pDC`: HDC of the printer device context used to print the document

## VBA Syntax

See [PrintNotify Event (ModelView)](ms-its:sldworksapivb6.chm::/SldWorks~ModelView~PrintNotify_EV.html).

## Remarks

Always return S_OK in the swViewPrintNotify event handler.

If developing a C++ application, use [swViewPrintNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2007 SP2, Revision Number 15.2
