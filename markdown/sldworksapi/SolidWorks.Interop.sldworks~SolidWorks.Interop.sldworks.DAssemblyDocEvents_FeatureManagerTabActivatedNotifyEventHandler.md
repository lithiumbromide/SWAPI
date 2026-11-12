---
title: "DAssemblyDocEvents_FeatureManagerTabActivatedNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_FeatureManagerTabActivatedNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FeatureManagerTabActivatedNotifyEventHandler.html"
---

# DAssemblyDocEvents_FeatureManagerTabActivatedNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the active tab in the Manager Pane changes.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_FeatureManagerTabActivatedNotifyEventHandler( _
   ByVal CommandIndex As System.Integer, _
   ByVal CommandTabName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_FeatureManagerTabActivatedNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_FeatureManagerTabActivatedNotifyEventHandler(
   System.int CommandIndex,
   System.string CommandTabName
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_FeatureManagerTabActivatedNotifyEventHandler(
   System.int CommandIndex,
   System.String^ CommandTabName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CommandIndex`: Index of the active tab in the Manager Pane
- `CommandTabName`: Name of the active tab in the Manager Pane

## VBA Syntax

See [FeatureManagerTabActivatedNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~FeatureManagerTabActivatedNotify_EV.html).

## Examples

[Change Active Tab in Manager Pane (C#)](Change_Active_Tab_in_Manager_Pane_Example_CSharp.htm)
[Change Active Tab in Manager Pane (VB.NET)](Change_Active_Tab_in_Manager_Pane_Example_VBNET.htm)
[Change Active Tab in Manager Pane (VBA)](Change_Active_Tab_in_Manager_Pane_Example_VB.htm)

## Remarks

If developing a C++ application, use [swAssemblyFeatureManagerTabActivatedNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS FCS 2017, Revision Number 25.0
