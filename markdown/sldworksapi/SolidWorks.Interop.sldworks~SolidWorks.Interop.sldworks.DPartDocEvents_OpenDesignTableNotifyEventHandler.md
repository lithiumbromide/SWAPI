---
title: "DPartDocEvents_OpenDesignTableNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_OpenDesignTableNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_OpenDesignTableNotifyEventHandler.html"
---

# DPartDocEvents_OpenDesignTableNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies your application that a design table has been opened for editing.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_OpenDesignTableNotifyEventHandler( _
   ByVal DesignTable As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_OpenDesignTableNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_OpenDesignTableNotifyEventHandler(
   System.object DesignTable
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_OpenDesignTableNotifyEventHandler(
   System.Object^ DesignTable
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DesignTable`: [Design table](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDesignTable.html)

## VBA Syntax

See [OpenDesignTableNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~OpenDesignTableNotify_EV.html).

## Remarks

The IPartDoc event [CloseDesignTableNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_CloseDesignTableNotifyEventHandler.html) pre-notifies your application that a design table that was opened for editing is about to be closed.

If developing a C++ application, use [swPartOpenDesignTableNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2007 SP4, Revision Number 15.4
