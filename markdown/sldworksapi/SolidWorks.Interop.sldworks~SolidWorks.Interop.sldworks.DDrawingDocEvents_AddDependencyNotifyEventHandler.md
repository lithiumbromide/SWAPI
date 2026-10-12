---
title: "DDrawingDocEvents_AddDependencyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_AddDependencyNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_AddDependencyNotifyEventHandler.html"
---

# DDrawingDocEvents_AddDependencyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the drawing references the specified document for the first time.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_AddDependencyNotifyEventHandler( _
   ByVal PathName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_AddDependencyNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_AddDependencyNotifyEventHandler(
   System.string PathName
)
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_AddDependencyNotifyEventHandler(
   System.String^ PathName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PathName`: The full name and path of the newly referenced document.

## Remarks

If developing a C++ application, use [swDrawingAddDepndencyNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2026 SP03, Revision Number 34.3
