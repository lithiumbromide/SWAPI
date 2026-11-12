---
title: "DAssemblyDocEvents_ComponentVisualPropertiesChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_ComponentVisualPropertiesChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentVisualPropertiesChangeNotifyEventHandler.html"
---

# DAssemblyDocEvents_ComponentVisualPropertiesChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when a visual property, such as color, transparency, and so on, of a component is changed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_ComponentVisualPropertiesChangeNotifyEventHandler( _
   ByVal Component As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_ComponentVisualPropertiesChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_ComponentVisualPropertiesChangeNotifyEventHandler(
   System.object Component
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_ComponentVisualPropertiesChangeNotifyEventHandler(
   System.Object^ Component
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Component`: [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [ComponentVisualPropertiesChangeNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~ComponentVisualPropertiesChangeNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyComponentVisualPropertiesChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
