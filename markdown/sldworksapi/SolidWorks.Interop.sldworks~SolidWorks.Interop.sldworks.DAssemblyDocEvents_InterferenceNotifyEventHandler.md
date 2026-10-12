---
title: "DAssemblyDocEvents_InterferenceNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_InterferenceNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_InterferenceNotifyEventHandler.html"
---

# DAssemblyDocEvents_InterferenceNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies your program about an interference between parts in the assembly during the **Move/Rotate Component** command.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_InterferenceNotifyEventHandler( _
   ByRef PComp As System.Object, _
   ByRef PFace As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_InterferenceNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_InterferenceNotifyEventHandler(
   ref System.object PComp,
   ref System.object PFace
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_InterferenceNotifyEventHandler(
   System.Object^% PComp,
   System.Object^% PFace
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PComp`: Array of [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) that interfere
- `PFace`: Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) that interfere

## VBA Syntax

See [InterferenceNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~InterferenceNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyInterferenceNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

This notification is only sent when faces clash during the **Move/Rotate Component** command, which executes as an interactive drag of a component, and if collision detection is enabled in the user interface.

You can use this notification with [IAssemblyDoc::IToolsCheckInterference3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~IToolsCheckInterference3.html).

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
