---
title: "DPartDocEvents_FeatureManagerTreeRebuildNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_FeatureManagerTreeRebuildNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FeatureManagerTreeRebuildNotifyEventHandler.html"
---

# DPartDocEvents_FeatureManagerTreeRebuildNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when the active document's FeatureManager design tree is being rebuilt.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_FeatureManagerTreeRebuildNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_FeatureManagerTreeRebuildNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_FeatureManagerTreeRebuildNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_FeatureManagerTreeRebuildNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [FeatureManagerTreeRebuildNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~FeatureManagerTreeRebuildNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartFeatureManagerTreeRebuildNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2003 SP3, Revision Number 11.3
