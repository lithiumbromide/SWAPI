---
title: "DPartDocEvents_CloseDesignTableNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_CloseDesignTableNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_CloseDesignTableNotifyEventHandler.html"
---

# DPartDocEvents_CloseDesignTableNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies your application that a design table that was opened for editing is about to be closed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_CloseDesignTableNotifyEventHandler( _
   ByVal DesignTable As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_CloseDesignTableNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_CloseDesignTableNotifyEventHandler(
   System.object DesignTable
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_CloseDesignTableNotifyEventHandler(
   System.Object^ DesignTable
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DesignTable`: [Design table](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable.html)

## VBA Syntax

See [CloseDesignTableNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~CloseDesignTableNotify_EV.html).

## Remarks

The IPartDoc event [OpenDesignTableNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_OpenDesignTableNotifyEventHandler.html) post-notifies when a design table has been opened for editing.

If developing a C++ application, use [swPartOpenDesignTableNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2007 SP4, Revision Number 15.4
