---
title: "DAssemblyDocEvents_ComponentStateChangeNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_ComponentStateChangeNotify2EventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentStateChangeNotify2EventHandler.html"
---

# DAssemblyDocEvents_ComponentStateChangeNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)

Obsolete. Superseded by [DAssemblyDocEvents_ComponentStateChangeNotify3EventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentStateChangeNotify3EventHandler.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_ComponentStateChangeNotify2EventHandler( _
   ByVal componentModel As System.Object, _
   ByVal CompName As System.String, _
   ByVal oldCompState As System.Short, _
   ByVal newCompState As System.Short _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_ComponentStateChangeNotify2EventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_ComponentStateChangeNotify2EventHandler(
   System.object componentModel,
   System.string CompName,
   System.short oldCompState,
   System.short newCompState
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_ComponentStateChangeNotify2EventHandler(
   System.Object^ componentModel,
   System.String^ CompName,
   System.short oldCompState,
   System.short newCompState
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `componentModel`: [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)
- `CompName`: Name of the component
- `oldCompState`: Previous state of the component as defined in [swComponentSuppressionState_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSuppressionState_e.html)
- `newCompState`: New state of the component as defined in [swComponentSuppressionState_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSuppressionState_e.html)

## VBA Syntax

See [ComponentStateChangeNotify2 Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~ComponentStateChangeNotify2_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyComponentStateChangeNotify2](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

SOLIDWORKS sends this notification:

- even if the assembly is not the active document.
- when a component gets suppressed due to an internal ID mismatch.
- not at all if a part is explicitly opened by the user or opened programmatically. In that case, SOLIDWORKS resolves the component part in any open assembly that references it. Your application must watch for the SOLIDWORKS event [FileOpenNotify2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DSldWorksEvents_FileOpenNotify2EventHandler.html).

When a component is resolved or unsuppressed, its model document becomes available to your application. Within this notification, you can get this object and register for other events. This might be useful for project data management (PDM) applications that want to ask the user to check out the assembly component if the user tries to make changes.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
