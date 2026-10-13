---
title: "DPartDocEvents_AddItemNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_AddItemNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_AddItemNotifyEventHandler.html"
---

# DPartDocEvents_AddItemNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when an item is added to one of the SOLIDWORKS tree structures such as the FeatureManager design tree and the ConfigurationManager.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_AddItemNotifyEventHandler( _
   ByVal EntityType As System.Integer, _
   ByVal itemName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_AddItemNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_AddItemNotifyEventHandler(
   System.int EntityType,
   System.string itemName
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_AddItemNotifyEventHandler(
   System.int EntityType,
   System.String^ itemName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntityType`: Type of new item as defined in [swNotifyEntityType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNotifyEntityType_e.html)
- `itemName`: Name of new item

## VBA Syntax

See [AddItemNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~AddItemNotify_EV.html).

## Remarks

If developing a C++ application, use [swPartAddItemNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
