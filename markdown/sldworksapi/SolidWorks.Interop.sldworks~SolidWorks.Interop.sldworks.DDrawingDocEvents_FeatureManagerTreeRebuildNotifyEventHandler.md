---
title: "DDrawingDocEvents_FeatureManagerTreeRebuildNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_FeatureManagerTreeRebuildNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FeatureManagerTreeRebuildNotifyEventHandler.html"
---

# DDrawingDocEvents_FeatureManagerTreeRebuildNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when the active document's FeatureManager design tree is being rebuilt.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_FeatureManagerTreeRebuildNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_FeatureManagerTreeRebuildNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_FeatureManagerTreeRebuildNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_FeatureManagerTreeRebuildNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [FeatureManagerTreeRebuildNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~FeatureManagerTreeRebuildNotify_EV.html).

## Remarks

This notification is only used by SOLIDWORKS Animator.

If developing a C++ application, use [swDrawingFeatureManagerTreeRebuildNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2003 SP3, Revision Number 11.3
