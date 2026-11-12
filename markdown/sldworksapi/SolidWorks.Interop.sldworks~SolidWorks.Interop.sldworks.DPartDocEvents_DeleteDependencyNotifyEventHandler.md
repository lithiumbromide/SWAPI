---
title: "DPartDocEvents_DeleteDependencyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_DeleteDependencyNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_DeleteDependencyNotifyEventHandler.html"
---

# DPartDocEvents_DeleteDependencyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the part no longer references the specified document.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_DeleteDependencyNotifyEventHandler( _
   ByVal PathName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_DeleteDependencyNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_DeleteDependencyNotifyEventHandler(
   System.string PathName
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_DeleteDependencyNotifyEventHandler(
   System.String^ PathName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PathName`: The full name and path of the document no longer referenced.

## Remarks

If developing a C++ application, use [swPartDeleteDependencyNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2026 SP03, Revision Number 34.3
