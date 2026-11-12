---
title: "DAssemblyDocEvents_ActiveDisplayStateChangePostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_ActiveDisplayStateChangePostNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ActiveDisplayStateChangePostNotifyEventHandler.html"
---

# DAssemblyDocEvents_ActiveDisplayStateChangePostNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired after the display state of a configuration is changed or after a configuration is changed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_ActiveDisplayStateChangePostNotifyEventHandler( _
   ByVal DisplayStateName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_ActiveDisplayStateChangePostNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_ActiveDisplayStateChangePostNotifyEventHandler(
   System.string DisplayStateName
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_ActiveDisplayStateChangePostNotifyEventHandler(
   System.String^ DisplayStateName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DisplayStateName`: Name of the active display state

## VBA Syntax

See [ActiveDisplayStateChangePostNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~ActiveDisplayStateChangePostNotify_EV.html).

## Examples

[Fire Events When Display State Changes (C#)](Fire_Events_When_Display_State_Changes_Example_CSharp.htm)
[Fire Events When Display State Changes (VB.NET)](Fire_Events_When_Display_State_Changes_Example_VBNET.htm)
[Fire Events When Display State Changes (VBA)](Fire_Events_When_Display_State_Changes_Example_VB.htm)

## Remarks

When changing configurations, the following events are fired in this order:

- [ActiveConfigChangeNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_ActiveConfigChangeNotifyEventHandler.html)
- [ActiveDisplayStateChangePreNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_ActiveDisplayStateChangePreNotifyEventHandler.html)
- [ActiveConfigChangePostNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_ActiveConfigChangePostNotifyEventHandler.html)
- ActiveDisplayStateChangePostNotify

When changing the display state of a configuration, only ActiveDisplayStateChangePreNotify and ActiveDisplayStateChangePostNotify are fired.

This event is fired even when configurations and display states are not linked; however, the initial and final display states will be the same.

## Availability

SOLIDWORKS 2009 SP2, Revision Number 17.2
