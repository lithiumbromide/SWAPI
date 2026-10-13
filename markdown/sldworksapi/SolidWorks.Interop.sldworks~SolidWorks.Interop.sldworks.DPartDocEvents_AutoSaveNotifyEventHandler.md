---
title: "DPartDocEvents_AutoSaveNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_AutoSaveNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_AutoSaveNotifyEventHandler.html"
---

# DPartDocEvents_AutoSaveNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the part document is automatically saved.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_AutoSaveNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_AutoSaveNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_AutoSaveNotifyEventHandler(
   System.string FileName
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_AutoSaveNotifyEventHandler(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: File name to which to save the part document

## VBA Syntax

See [AutoSaveNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~AutoSaveNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartAutoSaveNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
