---
title: "DDrawingDocEvents_DeleteItemNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_DeleteItemNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_DeleteItemNotifyEventHandler.html"
---

# DDrawingDocEvents_DeleteItemNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies the user program when an item is deleted from one of the SOLIDWORKS tree structures (for example, the FeatureManager design tree or the ConfigurationManager tree).

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_DeleteItemNotifyEventHandler( _
   ByVal EntityType As System.Integer, _
   ByVal itemName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_DeleteItemNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_DeleteItemNotifyEventHandler(
   System.int EntityType,
   System.string itemName
)
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_DeleteItemNotifyEventHandler(
   System.int EntityType,
   System.String^ itemName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntityType`: Type of the item deleted as defined in [swNotifyEntityType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNotifyEntityType_e.html)
- `itemName`: Name of the deleted item

## VBA Syntax

See [DeleteItemNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~DeleteItemNotify_EV.html).

## Remarks

If developing a C++ application, use [swDrawingDeleteItemNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
