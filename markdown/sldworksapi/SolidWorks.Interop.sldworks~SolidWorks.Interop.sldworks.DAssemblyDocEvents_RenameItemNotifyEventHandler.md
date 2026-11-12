---
title: "DAssemblyDocEvents_RenameItemNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_RenameItemNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RenameItemNotifyEventHandler.html"
---

# DAssemblyDocEvents_RenameItemNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when an item is renamed in one of the SOLIDWORKS Design tree structures, such as the FeatureManager design tree or the ConfigurationManager tree.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_RenameItemNotifyEventHandler( _
   ByVal EntityType As System.Integer, _
   ByVal oldName As System.String, _
   ByVal NewName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_RenameItemNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_RenameItemNotifyEventHandler(
   System.int EntityType,
   System.string oldName,
   System.string NewName
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_RenameItemNotifyEventHandler(
   System.int EntityType,
   System.String^ oldName,
   System.String^ NewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntityType`: Type of item to rename as defined in [swNotifyEntityType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNotifyEntityType_e.html)
- `oldName`: Current item name
- `NewName`: New item name

## VBA Syntax

See [RenameItemNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~RenameItemNotify_EV.html).

## Examples

[Add Component and Mate (VBA)](Add_Component_and_Mate_Example_VB.htm)
[Add Component and Mate (VB.NET)](Add_Component_and_Mate_Example_VBNET.htm)
[Add Component and Mate (C#)](Add_Component_and_Mate_Example_CSharp.htm)
[Fire Notifications When Renaming Components (C#)](Fire_Notifications_When_Renaming_Components_Example_CSharp.htm)
[Fire Notifications When Renaming Components (VB.NET)](Fire_Notifications_When_Renaming_Components_Example_VBNET.htm)
[Fire Notifications When Renaming Components (VBA)](Fire_Notifications_When_Renaming_Components_Example_VB.htm)

## Remarks

This event is also fired when [IComponent2::MakeVirtual](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~MakeVirtual.html) is called.

If developing a C++ application, use [swAssemblyRenameItemNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
