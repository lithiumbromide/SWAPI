---
title: "DSldWorksEvents_FileOpenPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_FileOpenPostNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileOpenPostNotifyEventHandler.html"
---

# DSldWorksEvents_FileOpenPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when a file has been opened.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_FileOpenPostNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_FileOpenPostNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_FileOpenPostNotifyEventHandler(
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_FileOpenPostNotifyEventHandler(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of the opened file

## VBA Syntax

See [FileOpenPostNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~FileOpenPostNotify_EV.html).

## Remarks

This is the last event fired before control returns to the user. This event indicates that methods that modify references, [reload documents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ReloadOrReplace.html), or close documents can be called.

If developing a C++ application, use [swAppFileOpenPostNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
