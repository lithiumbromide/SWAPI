---
title: "DFeatMgrViewEvents_DestroyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DFeatMgrViewEvents_DestroyNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DFeatMgrViewEvents_DestroyNotifyEventHandler.html"
---

# DFeatMgrViewEvents_DestroyNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Pre-notifies the user program when a FeatureManager design tree view is about to be destroyed and returns the view handle.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DFeatMgrViewEvents_DestroyNotifyEventHandler( _
   ByRef View As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DFeatMgrViewEvents_DestroyNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DFeatMgrViewEvents_DestroyNotifyEventHandler(
   ref System.object View
)
```

### C++/CLI

```cpp
public delegate System.int DFeatMgrViewEvents_DestroyNotifyEventHandler(
   System.Object^% View
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `View`: [View](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html)

## VBA Syntax

See [DestroyNotify Event (FeatMgrView)](ms-its:sldworksapivb6.chm::/SldWorks~FeatMgrView~DestroyNotify_EV.html).

## Remarks

If developing a C++ application, use [swFMViewDestroyNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFMViewNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
