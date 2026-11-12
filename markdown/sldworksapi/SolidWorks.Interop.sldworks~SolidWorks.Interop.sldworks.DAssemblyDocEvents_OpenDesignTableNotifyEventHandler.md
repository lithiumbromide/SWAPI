---
title: "DAssemblyDocEvents_OpenDesignTableNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_OpenDesignTableNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_OpenDesignTableNotifyEventHandler.html"
---

# DAssemblyDocEvents_OpenDesignTableNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies your application that a design table has been opened for editing.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_OpenDesignTableNotifyEventHandler( _
   ByVal DesignTable As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_OpenDesignTableNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_OpenDesignTableNotifyEventHandler(
   System.object DesignTable
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_OpenDesignTableNotifyEventHandler(
   System.Object^ DesignTable
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DesignTable`: [Design table](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable.html)

## VBA Syntax

See [OpenDesignTableNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~OpenDesignTableNotify_EV.html).

## Remarks

The IAssemblyDoc event [CloseDesignTableNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_CloseDesignTableNotifyEventHandler.html) pre-notifies your application that a design table that was being edited is about to be closed.

If developing a C++ application, use [swAssemblyOpenDesignTableNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2007 SP4, Revision Number 15.4
