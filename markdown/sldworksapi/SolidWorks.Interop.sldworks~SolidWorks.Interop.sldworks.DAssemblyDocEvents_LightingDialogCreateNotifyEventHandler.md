---
title: "DAssemblyDocEvents_LightingDialogCreateNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_LightingDialogCreateNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_LightingDialogCreateNotifyEventHandler.html"
---

# DAssemblyDocEvents_LightingDialogCreateNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when a lighting dialog has been opened by the user.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_LightingDialogCreateNotifyEventHandler( _
   ByVal dialog As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_LightingDialogCreateNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_LightingDialogCreateNotifyEventHandler(
   System.object dialog
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_LightingDialogCreateNotifyEventHandler(
   System.Object^ dialog
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `dialog`: [Light dialog](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILightDialog.html)

## VBA Syntax

See [LightingDialogCreateNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~LightingDialogCreateNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyLightingDialogCreateNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
