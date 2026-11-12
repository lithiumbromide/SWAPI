---
title: "DPartDocEvents_FeatureManagerTabActivatedNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_FeatureManagerTabActivatedNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FeatureManagerTabActivatedNotifyEventHandler.html"
---

# DPartDocEvents_FeatureManagerTabActivatedNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the active tab changes in the Manager Pane.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_FeatureManagerTabActivatedNotifyEventHandler( _
   ByVal CommandIndex As System.Integer, _
   ByVal CommandTabName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_FeatureManagerTabActivatedNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_FeatureManagerTabActivatedNotifyEventHandler(
   System.int CommandIndex,
   System.string CommandTabName
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_FeatureManagerTabActivatedNotifyEventHandler(
   System.int CommandIndex,
   System.String^ CommandTabName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CommandIndex`: Index of the active tab in the Manager Pane
- `CommandTabName`: Index of the active tab in the Manager Pane

## VBA Syntax

See [FeatureManagerTabActivatedNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~FeatureManagerFilterStringChangeNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartFeatureManagerTabActivatedNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
