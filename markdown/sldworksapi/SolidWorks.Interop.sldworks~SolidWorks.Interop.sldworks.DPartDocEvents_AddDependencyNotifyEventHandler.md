---
title: "DPartDocEvents_AddDependencyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_AddDependencyNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_AddDependencyNotifyEventHandler.html"
---

# DPartDocEvents_AddDependencyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the part references the specified document for the first time.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_AddDependencyNotifyEventHandler( _
   ByVal PathName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_AddDependencyNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_AddDependencyNotifyEventHandler(
   System.string PathName
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_AddDependencyNotifyEventHandler(
   System.String^ PathName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PathName`: The full name and path of the newly referenced document.

## Remarks

If developing a C++ application, use [swPartAddDependencyNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2026 SP03, Revision Number 34.3
