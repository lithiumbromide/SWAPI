---
title: "DAssemblyDocEvents_ComponentDisplayModeChangePreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_ComponentDisplayModeChangePreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentDisplayModeChangePreNotifyEventHandler.html"
---

# DAssemblyDocEvents_ComponentDisplayModeChangePreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired before a reference component's display mode is changed in an assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_ComponentDisplayModeChangePreNotifyEventHandler( _
   ByVal Component As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_ComponentDisplayModeChangePreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_ComponentDisplayModeChangePreNotifyEventHandler(
   System.object Component
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_ComponentDisplayModeChangePreNotifyEventHandler(
   System.Object^ Component
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Component`: [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [ComponentDisplayModeChangePreNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~ComponentDisplayModeChangePreNotify_EV.html).

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
