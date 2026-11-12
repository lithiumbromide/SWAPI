---
title: "DMouseEvents_MouseSelectNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DMouseEvents_MouseSelectNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DMouseEvents_MouseSelectNotifyEventHandler.html"
---

# DMouseEvents_MouseSelectNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when the user makes a selection in the model view using the mouse.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DMouseEvents_MouseSelectNotifyEventHandler( _
   ByVal Ix As System.Integer, _
   ByVal Iy As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DMouseEvents_MouseSelectNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DMouseEvents_MouseSelectNotifyEventHandler(
   System.int Ix,
   System.int Iy,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
public delegate System.int DMouseEvents_MouseSelectNotifyEventHandler(
   System.int Ix,
   System.int Iy,
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Ix`: x coordinate of the pointer in the window space
- `Iy`: y coordinate of the pointer in the window space
- `X`: x coordinate of the pointer in world space
- `Y`: y coordinate of the pointer in world space
- `Z`: z coordinate of the pointer in world space

## VBA Syntax

See [MouseSelectNotify Event (Mouse)](ms-its:sldworksapivb6.chm::/SldWorks~Mouse~MouseSelectNotify_EV.html).

## Examples

[Run SOLIDWORKS Commands and Synthesize Mouse Events (C#)](Run_SolidWorks_Commands_and_Synthesize_Mouse_Events_Example_CSharp.htm)
[Run SOLIDWORKS Commands and Synthesize Mouse Events (VB.NET)](Run_SolidWorks_Commands_and_Synthesize_Mouse_Events_Example_VBNET.htm)
[Run SOLIDWORKS Commands and Synthesize Mouse Events (VBA)](Run_SOLIDWORKS_Commands_and_Synthesize_Mouse_Events_Example_VB.htm)

## Remarks

If developing a C++ application, use [swMouseSelectNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMouseNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
