---
title: "DAssemblyDocEvents_FeatureManagerTreeRebuildNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_FeatureManagerTreeRebuildNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FeatureManagerTreeRebuildNotifyEventHandler.html"
---

# DAssemblyDocEvents_FeatureManagerTreeRebuildNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when the active document's FeatureManager design tree is being rebuilt.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_FeatureManagerTreeRebuildNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_FeatureManagerTreeRebuildNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_FeatureManagerTreeRebuildNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_FeatureManagerTreeRebuildNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [FeatureManagerTreeRebuildNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~FeatureManagerTreeRebuildNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyFeatureManagerTreeRebuildNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

This notification is only used by SOLIDWORKS Animator.

## Availability

SOLIDWORKS 2003 SP3, Revision Number 11.3
