---
title: "DDrawingDocEvents_DeleteItemPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_DeleteItemPreNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_DeleteItemPreNotifyEventHandler.html"
---

# DDrawingDocEvents_DeleteItemPreNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies the user program when an item is about to be deleted from one of the SOLIDWORKS tree structures (for example, the FeatureManager design tree or the ConfigurationManager tree).

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_DeleteItemPreNotifyEventHandler( _
   ByVal EntityType As System.Integer, _
   ByVal itemName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_DeleteItemPreNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_DeleteItemPreNotifyEventHandler(
   System.int EntityType,
   System.string itemName
)
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_DeleteItemPreNotifyEventHandler(
   System.int EntityType,
   System.String^ itemName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntityType`: Type of the item deleted as defined in [swNotifyEntityType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNotifyEntityType_e.html)
- `itemName`: Name of the deleted item

## VBA Syntax

See [DeleteItemPreNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~DeleteItemPreNotify_EV.html).

## Remarks

Use [IDrawingDoc::FeatureByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc.html)[FeatureByName Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~FeatureByName.html) or [IDrawingDoc::IFeatureByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~IFeatureByName.html) to get the object being deleted.

If developing a C++ application, use [swDrawingDeleteItemPreNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
