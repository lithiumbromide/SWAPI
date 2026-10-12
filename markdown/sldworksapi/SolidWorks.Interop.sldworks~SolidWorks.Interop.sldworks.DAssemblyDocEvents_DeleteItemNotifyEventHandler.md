---
title: "DAssemblyDocEvents_DeleteItemNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_DeleteItemNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_DeleteItemNotifyEventHandler.html"
---

# DAssemblyDocEvents_DeleteItemNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies the user program when an item is deleted from one of the SOLIDWORKS Design tree structures (for example, the FeatureManager design tree or the ConfigurationManager tree).

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_DeleteItemNotifyEventHandler( _
   ByVal EntityType As System.Integer, _
   ByVal itemName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_DeleteItemNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_DeleteItemNotifyEventHandler(
   System.int EntityType,
   System.string itemName
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_DeleteItemNotifyEventHandler(
   System.int EntityType,
   System.String^ itemName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntityType`: Type of entity deleted as defined in [swNotifyEntityType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNotifyEntityType_e.html)
- `itemName`: Name of entity deleted

## VBA Syntax

See [DeleteItemNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~DeleteItemNotify_EV.html).

## Remarks

If developing a C++ application, use [swAssemblyDeleteItemNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

No explicit notification is available for a component reorder operation. However, component reordering generates [DeleteItemNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_DeleteItemNotifyEventHandler.html) and [AddItemNotify](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.DAssemblyDocEvents_AddItemNotifyEventHandler.html) events.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
