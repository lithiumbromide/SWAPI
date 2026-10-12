---
title: "DAssemblyDocEvents_SelectiveOpenPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_SelectiveOpenPostNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_SelectiveOpenPostNotifyEventHandler.html"
---

# DAssemblyDocEvents_SelectiveOpenPostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when assembly components are selected for Quick View/Selective Open.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_SelectiveOpenPostNotifyEventHandler( _
   ByVal NewAddedDisplayStateName As System.String, _
   ByRef SelectedComponentNames As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_SelectiveOpenPostNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_SelectiveOpenPostNotifyEventHandler(
   System.string NewAddedDisplayStateName,
   ref System.object SelectedComponentNames
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_SelectiveOpenPostNotifyEventHandler(
   System.String^ NewAddedDisplayStateName,
   System.Object^% SelectedComponentNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NewAddedDisplayStateName`: Name of the new display state
- `SelectedComponentNames`: Array of selected component names

## VBA Syntax

See [SelectiveOpenPostNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~SelectiveOpenPostNotify_EV.html).

## Examples

[Selective Open Post-Notify Event (VBA)](Selective_Open_Post_Notify_Event_Example_VB.htm)
[Selective Open Post-Notify Event (VB.NET)](Selective_Open_Post_Notify_Event_Example_VBNET.htm)
[Selective Open Post-Notify Event (C#)](Selective_Open_Post_Notify_Event_Example_CSharp.htm)

## Remarks

If developing a C++ application, use [swAssemblySelectiveOpenPostNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
