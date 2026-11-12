---
title: "DDrawingDocEvents_DeleteDependencyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_DeleteDependencyNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_DeleteDependencyNotifyEventHandler.html"
---

# DDrawingDocEvents_DeleteDependencyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the drawing no longer references the specified document.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_DeleteDependencyNotifyEventHandler( _
   ByVal PathName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_DeleteDependencyNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_DeleteDependencyNotifyEventHandler(
   System.string PathName
)
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_DeleteDependencyNotifyEventHandler(
   System.String^ PathName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PathName`: The full name and path of the document no longer referenced.

## Remarks

If developing a C++ application, use [swDrawingDeleteDepndencyNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2026 SP03, Revision Number 34.3
