---
title: "DPartDocEvents_ActiveDisplayStateChangePostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_ActiveDisplayStateChangePostNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ActiveDisplayStateChangePostNotifyEventHandler.html"
---

# DPartDocEvents_ActiveDisplayStateChangePostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired after the display state of a configuration is changed or after a configuration is changed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_ActiveDisplayStateChangePostNotifyEventHandler( _
   ByVal DisplayStateName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_ActiveDisplayStateChangePostNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_ActiveDisplayStateChangePostNotifyEventHandler(
   System.string DisplayStateName
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_ActiveDisplayStateChangePostNotifyEventHandler(
   System.String^ DisplayStateName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DisplayStateName`: Name of the active display state

## VBA Syntax

See [ActiveDisplayStateChangePostNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~ActiveDisplayStateChangePostNotify_EV.html).

## Examples

[Fire Events When Display State Changes in Part Document (C#)](Fire_Events_When_Display_State_Changes_in_Part_Document_Example_CSharp.htm)
[Fire Events When Display State Changes in Part Document (VB.NET)](Fire_Events_When_Display_State_Changes_in_Part_Document_Example_VBNET.htm)
[Fire Events When Display State Changes in Part Document (VBA)](Fire_Events_When_Display_State_Changes_in_Part_Document_Example_VB6.htm)

## Remarks

When changing configurations, the following events are fired in this order:

- [ActiveConfigChangeNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_ActiveConfigChangeNotifyEventHandler.html)
- [ActiveDisplayStateChangePreNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_ActiveDisplayStateChangePreNotifyEventHandler.html)
- [ActiveConfigChangePostNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DPartDocEvents_ActiveConfigChangePostNotifyEventHandler.html)
- ActiveDisplayStateChangePostNotify

When changing the display state of a configuration, only ActiveDisplayStateChangePreNotify and ActiveDisplayStateChangePostNotify are fired.

This event is fired even when configurations and display states are not linked; however, the initial and final display states will be the same.

## Availability

SOLIDWORKS 2010 FCS, Revision Number 17.0
