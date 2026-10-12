---
title: "DAssemblyDocEvents_DragStateChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_DragStateChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_DragStateChangeNotifyEventHandler.html"
---

# DAssemblyDocEvents_DragStateChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when starting or stopping the dragging of an Instant3D manipulator.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_DragStateChangeNotifyEventHandler( _
   ByVal State As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_DragStateChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_DragStateChangeNotifyEventHandler(
   System.bool State
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_DragStateChangeNotifyEventHandler(
   System.bool State
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `State`: True if dragging of the Instant3D manipulator has started, false if dragging of the Instant3D manipulator has stopped

## VBA Syntax

See [DragStateChangeNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~DragStateChangeNotify_EV.html).

## Examples

[Fire Events When Dragging Instant3D Manipulator in an Assembly (C#)](Fire_Events_When_Dragging_Instant3D_Manipulator_in_an_Assembly_Example_CSharp.htm)
[Fire Events When Dragging Instant3D Manipulator in an Assembly (VB.NET)](Fire_Events_When_Dragging_Instant3D_Manipulator_in_an_Assembly_Example_VBNET.htm)
[Fire Events When Dragging Instant3D Manipulator in an Assembly (VBA)](Fire_Events_When_Dragging_Instant3D_Manipulator_in_an_Assembly_Example_VB.htm)

## Remarks

If developing a C++ application, use [swAssemblyDragStateChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
