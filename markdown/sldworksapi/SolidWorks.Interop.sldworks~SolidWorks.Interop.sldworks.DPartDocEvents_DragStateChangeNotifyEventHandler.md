---
title: "DPartDocEvents_DragStateChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_DragStateChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_DragStateChangeNotifyEventHandler.html"
---

# DPartDocEvents_DragStateChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when starting or stopping the dragging of an Instant3D manipulator.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_DragStateChangeNotifyEventHandler( _
   ByVal State As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_DragStateChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_DragStateChangeNotifyEventHandler(
   System.bool State
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_DragStateChangeNotifyEventHandler(
   System.bool State
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `State`: True if dragging of the Instant3D manipulator has started; false if dragging of the Instant3D manipulator has stopped

## VBA Syntax

See [DragStateChangeNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~DragStateChangeNotify_EV.html).

## Examples

[Fire Events When Dragging Instant3D Manipulator in a Part (C#)](Fire_Events_When_Dragging_Instant3D_Manipulator_in_a_Part_Example_CSharp.htm)
[Fire Events When Dragging Instant3D Manipulator in a Part (VB.NET)](Fire_Events_When_Dragging_Instant3D_Manipulator_in_a_Part_Example_VBNET.htm)
[Fire Events When Dragging Instant3D Manipulator in a Part (VBA)](Fire_Events_When_Dragging_Instant3D_Manipulator_in_a_Part_Example_VB.htm)

## Remarks

If developing a C++ application, use [swPartDragStateChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
