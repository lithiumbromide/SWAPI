---
title: "DAssemblyDocEvents_DestroyNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_DestroyNotify2EventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_DestroyNotify2EventHandler.html"
---

# DAssemblyDocEvents_DestroyNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user program when an assembly document is about to be destroyed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_DestroyNotify2EventHandler( _
   ByVal DestroyType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_DestroyNotify2EventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_DestroyNotify2EventHandler(
   System.int DestroyType
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_DestroyNotify2EventHandler(
   System.int DestroyType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DestroyType`: Value as defined by [swDestroyNotifyType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDestroyNotifyType_e.html)

## VBA Syntax

See [DestroyNotify2 Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~DestroyNotify2_EV.html).

## Remarks

The DestroyType argument indicates whether the assembly is being removed from memory (swDestroyNotifyDestroy) or if it remains open due to an outside reference (swDestroyNotifyHidden).

If developing a C++ application, use [swAssemblyDestroyNotify2](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
