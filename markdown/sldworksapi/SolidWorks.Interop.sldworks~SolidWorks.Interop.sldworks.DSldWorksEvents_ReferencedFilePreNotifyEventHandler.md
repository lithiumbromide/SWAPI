---
title: "DSldWorksEvents_ReferencedFilePreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_ReferencedFilePreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_ReferencedFilePreNotifyEventHandler.html"
---

# DSldWorksEvents_ReferencedFilePreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Obsolete. Superseded by [DSldWorksEvents_ReferencedFilePreNotify2EventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_ReferencedFilePreNotify2EventHandler.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_ReferencedFilePreNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_ReferencedFilePreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_ReferencedFilePreNotifyEventHandler(
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_ReferencedFilePreNotifyEventHandler(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Path and filename of referenced file

## VBA Syntax

See [ReferencedFilePreNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~ReferencedFilePreNotify_EV.html).

## Remarks

If developing a C++ application, use [swAppReferencedFilePreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
