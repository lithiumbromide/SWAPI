---
title: "DAssemblyDocEvents_ActiveDisplayStateChangePreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_ActiveDisplayStateChangePreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ActiveDisplayStateChangePreNotifyEventHandler.html"
---

# DAssemblyDocEvents_ActiveDisplayStateChangePreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired before the display state of a configuration is changed or before a configuration is changed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_ActiveDisplayStateChangePreNotifyEventHandler() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_ActiveDisplayStateChangePreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_ActiveDisplayStateChangePreNotifyEventHandler()
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_ActiveDisplayStateChangePreNotifyEventHandler();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ActiveDisplayStateChangePreNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~ActiveDisplayStateChangePreNotify_EV.html).

## Examples

[Fire Events When Display State Changes (C#)](Fire_Events_When_Display_State_Changes_Example_CSharp.htm)
[Fire Events When Display State Changes (VB.NET)](Fire_Events_When_Display_State_Changes_Example_VBNET.htm)
[Fire Events When Display State Changes (VBA)](Fire_Events_When_Display_State_Changes_Example_VB.htm)

## Remarks

When changing configurations, the following events are fired in this order:

- [ActiveConfigChangeNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_ActiveConfigChangeNotifyEventHandler.html)
- ActiveDisplayStateChangePreNotify
- [ActiveConfigChangePostNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_ActiveConfigChangePostNotifyEventHandler.html)
- [ActiveDisplayStateChangePostNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_ActiveDisplayStateChangePostNotifyEventHandler.html)

When changing the display state of a configuration, only ActiveDisplayStateChangePreNotify and ActiveDisplayStateChangePostNotify are fired.

This event is fired even when configurations and display states are not linked; however, the initial and final display states will be the same.

## Availability

SOLIDWORKS 2009 SP2, Revision Number 17.2
