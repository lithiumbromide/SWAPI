---
title: "DAssemblyDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler.html"
---

# DAssemblyDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired before the active tab in the Manager Pane changes.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler( _
   ByVal CommandIndex As System.Integer, _
   ByVal CommandTabName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler(
   System.int CommandIndex,
   System.string CommandTabName
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_FeatureManagerTabActivatedPreNotifyEventHandler(
   System.int CommandIndex,
   System.String^ CommandTabName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CommandIndex`: Index of the active tab in the Manager Pane
- `CommandTabName`: Name of the active tab in the Manager Pane

## VBA Syntax

See [FeatureManagerTabActivatedPreNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~FeatureManagerTabActivatedPreNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyFeatureManagerTabActivatedPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
