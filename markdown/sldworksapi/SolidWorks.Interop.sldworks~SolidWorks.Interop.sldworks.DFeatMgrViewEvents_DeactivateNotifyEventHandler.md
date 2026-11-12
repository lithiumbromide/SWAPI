---
title: "DFeatMgrViewEvents_DeactivateNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DFeatMgrViewEvents_DeactivateNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DFeatMgrViewEvents_DeactivateNotifyEventHandler.html"
---

# DFeatMgrViewEvents_DeactivateNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program once a FeatureManager design tree view is deactivated and returns the view handle.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DFeatMgrViewEvents_DeactivateNotifyEventHandler( _
   ByRef View As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DFeatMgrViewEvents_DeactivateNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DFeatMgrViewEvents_DeactivateNotifyEventHandler(
   ref System.object View
)
```

### C++/CLI

```cpp
public delegate System.int DFeatMgrViewEvents_DeactivateNotifyEventHandler(
   System.Object^% View
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `View`: [View](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html)

## VBA Syntax

See [DeactivateNotify Event (FeatMgrView)](ms-its:sldworksapivb6.chm::/SldWorks~FeatMgrView~DeactivateNotify_EV.html).

## Remarks

This notification is generated if you created the FeatureManager design tree view using [IModelViewManager::CreateFeatureMgrView2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.html) instead of [IModelDoc2::AddFeatureMgrView3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddFeatureMgrView3.html).

If developing a C++ application, use [swFMViewDeactivateNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFMViewNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
