---
title: "DAssemblyDocEvents_ComponentStateChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_ComponentStateChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentStateChangeNotifyEventHandler.html"
---

# DAssemblyDocEvents_ComponentStateChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Obsolete. Superseded by [DAssemblyDocEvents_ComponentStateChangeNotify2EventHandler](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_ComponentStateChangeNotify2EventHandler.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_ComponentStateChangeNotifyEventHandler( _
   ByVal componentModel As System.Object, _
   ByVal oldCompState As System.Short, _
   ByVal newCompState As System.Short _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_ComponentStateChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_ComponentStateChangeNotifyEventHandler(
   System.object componentModel,
   System.short oldCompState,
   System.short newCompState
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_ComponentStateChangeNotifyEventHandler(
   System.Object^ componentModel,
   System.short oldCompState,
   System.short newCompState
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `componentModel`:
- `oldCompState`:
- `newCompState`:

### Return Value

## VBA Syntax

See [ComponentStateChangeNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~ComponentStateChangeNotify_EV.html).

## Availability
