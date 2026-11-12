---
title: "DAssemblyDocEvents_AddDependencyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_AddDependencyNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_AddDependencyNotifyEventHandler.html"
---

# DAssemblyDocEvents_AddDependencyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the assembly references the specified document for the first time.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_AddDependencyNotifyEventHandler( _
   ByVal PathName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_AddDependencyNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_AddDependencyNotifyEventHandler(
   System.string PathName
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_AddDependencyNotifyEventHandler(
   System.String^ PathName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PathName`: The full name and path of the newly referenced document.

## Remarks

If developing a C++ application, use [swAssemblyAddDependencyNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2026 SP03, Revision Number 34.3
