---
title: "DPartDocEvents_PreRenameItemNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_PreRenameItemNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_PreRenameItemNotifyEventHandler.html"
---

# DPartDocEvents_PreRenameItemNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when a part document referenced by other documents is about to be renamed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_PreRenameItemNotifyEventHandler( _
   ByVal EntityType As System.Integer, _
   ByVal oldName As System.String, _
   ByVal NewName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_PreRenameItemNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_PreRenameItemNotifyEventHandler(
   System.int EntityType,
   System.string oldName,
   System.string NewName
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_PreRenameItemNotifyEventHandler(
   System.int EntityType,
   System.String^ oldName,
   System.String^ NewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntityType`: Type of item to rename as defined in [swNotifyEntityType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swNotifyEntityType_e.html)
- `oldName`: - Current name of the part document
- `NewName`: New name of the part document

## VBA Syntax

See [PreRenameItemNotify Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~PreRenameItemNotify_EV.html).

## Examples

[Fire Notifications When Renaming Part Document Belonging to Assembly (C#)](Fire_Notifications_When_Renaming_Part_Document_Belonging_to_Assembly_Example_CSharp.htm)
[Fire Notifications When Renaming Part Document Belonging to Assembly (VB.NET)](Fire_Notifications_When_Renaming_Part_Document_Belonging_to_Assembly_Example_VBNET.htm)
[Fire Notifications When Renaming Part Document Belonging to Assembly (VBA)](Fire_Notifications_When_Renaming_Part_Document_Belonging_to_Assembly_Example_VB.htm)

## Remarks

If developing a C++ application, use [swPartPreRenameItemNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
