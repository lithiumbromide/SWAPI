---
title: "DDrawingDocEvents_RenameItemNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DDrawingDocEvents_RenameItemNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_RenameItemNotifyEventHandler.html"
---

# DDrawingDocEvents_RenameItemNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Notifies the user program when an item is renamed in one of the SOLIDWORKS tree structures (for example, such as the FeatureManager design tree or the ConfigurationManager tree).

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DDrawingDocEvents_RenameItemNotifyEventHandler( _
   ByVal EntityType As System.Integer, _
   ByVal oldName As System.String, _
   ByVal NewName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DDrawingDocEvents_RenameItemNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DDrawingDocEvents_RenameItemNotifyEventHandler(
   System.int EntityType,
   System.string oldName,
   System.string NewName
)
```

### C++/CLI

```cpp
public delegate System.int DDrawingDocEvents_RenameItemNotifyEventHandler(
   System.int EntityType,
   System.String^ oldName,
   System.String^ NewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntityType`: Type of item renamed as defined in [swNotifyEntityType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNotifyEntityType_e.html)
- `oldName`: Previous item name
- `NewName`: New item name

## VBA Syntax

See [RenameItemNotify Event (DrawingDoc)](ms-its:sldworksapivb6.chm::/SldWorks~DrawingDoc~RenameItemNotify_EV.html).

## Remarks

This supports the renaming of configurations.

If developing a C++ application, use [swDrawingRenameItemNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
