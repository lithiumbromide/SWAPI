---
title: "DAssemblyDocEvents_CloseDesignTableNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_CloseDesignTableNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_CloseDesignTableNotifyEventHandler.html"
---

# DAssemblyDocEvents_CloseDesignTableNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies your application that a design table that was being edited is about to be closed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_CloseDesignTableNotifyEventHandler( _
   ByVal DesignTable As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_CloseDesignTableNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_CloseDesignTableNotifyEventHandler(
   System.object DesignTable
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_CloseDesignTableNotifyEventHandler(
   System.Object^ DesignTable
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DesignTable`: [Design table](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable.html)

## VBA Syntax

See [CloseDesignTableNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~CloseDesignTableNotify_EV.html).

## Remarks

The IAssemblyDoc event [OpenDesignTableNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_OpenDesignTableNotifyEventHandler.html) post-notifies your application that a design table has just been opened for editing.

If developing a C++ application, use [swAssemblyCloseDesignTableNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2007 SP4, Revision Number 15.4
