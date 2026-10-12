---
title: "DPartDocEvents_DeleteItemPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_DeleteItemPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_DeleteItemPreNotifyEventHandler.html"
---

# DPartDocEvents_DeleteItemPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies the user program when an item is about to be deleted from one of the SOLIDWORKS tree structures, such as the FeatureManager design tree and the ConfigurationManager.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_DeleteItemPreNotifyEventHandler( _
   ByVal EntityType As System.Integer, _
   ByVal itemName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_DeleteItemPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_DeleteItemPreNotifyEventHandler(
   System.int EntityType,
   System.string itemName
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_DeleteItemPreNotifyEventHandler(
   System.int EntityType,
   System.String^ itemName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntityType`: Type of item deleted as defined in [swNotifyEntityType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNotifyEntityType_e.html)
- `itemName`: Name of the item to be deleted

## VBA Syntax

See [DeleteItemPreNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~DeleteItemPreNotify_EV.html).

## Remarks

Use [IPartDoc::FeatureByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~FeatureByName.html) or [IPartDoc::IFeatureByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~IFeatureByName.html) to get the object to be deleted.

If developing a C++ application, use [swPartDeleteItemPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
