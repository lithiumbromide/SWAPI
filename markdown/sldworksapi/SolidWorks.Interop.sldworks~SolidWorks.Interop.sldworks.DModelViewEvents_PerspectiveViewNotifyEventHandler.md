---
title: "DModelViewEvents_PerspectiveViewNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DModelViewEvents_PerspectiveViewNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_PerspectiveViewNotifyEventHandler.html"
---

# DModelViewEvents_PerspectiveViewNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when the perspective view is changed (for example, if the user rotates the perspective view).

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DModelViewEvents_PerspectiveViewNotifyEventHandler( _
   ByVal Left As System.Double, _
   ByVal Right As System.Double, _
   ByVal bottom As System.Double, _
   ByVal Top As System.Double, _
   ByVal zNear As System.Double, _
   ByVal zFar As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DModelViewEvents_PerspectiveViewNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DModelViewEvents_PerspectiveViewNotifyEventHandler(
   System.double Left,
   System.double Right,
   System.double bottom,
   System.double Top,
   System.double zNear,
   System.double zFar
)
```

### C++/CLI

```cpp
public delegate System.int DModelViewEvents_PerspectiveViewNotifyEventHandler(
   System.double Left,
   System.double Right,
   System.double bottom,
   System.double Top,
   System.double zNear,
   System.double zFar
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Left`: Coordinate of the left vertical clipping plane
- `Right`: Coordinate of the right vertical clipping plane
- `bottom`: Coordinate of the bottom horizontal clipping plane
- `Top`: Coordinate of the top horizontal clipping plane
- `zNear`: Distance to the near depth clipping plane
- `zFar`: Distance to the far depth clipping plane

## VBA Syntax

See [PerspectiveViewNotify Event (ModelView)](ms-its:sldworksapivb6.chm::/SldWorks~ModelView~PerspectiveViewNotify_EV.html).

## Remarks

If developing a C++ application, use [swViewPerspectiveViewNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
