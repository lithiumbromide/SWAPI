---
title: "DAssemblyDocEvents_ComponentReferredDisplayStateChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_ComponentReferredDisplayStateChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentReferredDisplayStateChangeNotifyEventHandler.html"
---

# DAssemblyDocEvents_ComponentReferredDisplayStateChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when a component's referenced display state changes.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_ComponentReferredDisplayStateChangeNotifyEventHandler( _
   ByVal componentModel As System.Object, _
   ByVal CompName As System.String, _
   ByVal oldDSId As System.Integer, _
   ByVal oldDSName As System.String, _
   ByVal newDSId As System.Integer, _
   ByVal newDSName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_ComponentReferredDisplayStateChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_ComponentReferredDisplayStateChangeNotifyEventHandler(
   System.object componentModel,
   System.string CompName,
   System.int oldDSId,
   System.string oldDSName,
   System.int newDSId,
   System.string newDSName
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_ComponentReferredDisplayStateChangeNotifyEventHandler(
   System.Object^ componentModel,
   System.String^ CompName,
   System.int oldDSId,
   System.String^ oldDSName,
   System.int newDSId,
   System.String^ newDSName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `componentModel`: [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) whose referenced display state is changing
- `CompName`: Name of component
- `oldDSId`: Original referenced display state ID of the component
- `oldDSName`: Original referenced display state name for the component
- `newDSId`: New referenced display state ID of the component
- `newDSName`: New referenced display state name for the component

## VBA Syntax

See [ComponentReferredDisplayStateChangeNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~ComponentReferredDisplayStateChangeNotify_EV.html).

## Examples

[Fire Notification When Component Referenced Display State Changes (C#)](Fire_Notification_When_Component_Referenced_Display_State_Changes_Example_CSharp.htm)
[Fire Notification When Component Referenced Display State Changes (VB.NET)](Fire_Notification_When_Component_Referenced_Display_State_Changes_Example_VBNET.htm)
[Fire Notification When Component Referenced Display State Changes (VBA)](Fire_Notification_When_Component_Referenced_Display_State_Changed_Example_VB.htm)

## Remarks

If developing a C++ application, use [ComponentReferredDisplayStateChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
