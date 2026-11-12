---
title: "DAssemblyDocEvents_PreRenameItemNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_PreRenameItemNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_PreRenameItemNotifyEventHandler.html"
---

# DAssemblyDocEvents_PreRenameItemNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when a component document in an assembly is about to be renamed.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_PreRenameItemNotifyEventHandler( _
   ByVal EntityType As System.Integer, _
   ByVal oldName As System.String, _
   ByVal NewName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_PreRenameItemNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_PreRenameItemNotifyEventHandler(
   System.int EntityType,
   System.string oldName,
   System.string NewName
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_PreRenameItemNotifyEventHandler(
   System.int EntityType,
   System.String^ oldName,
   System.String^ NewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntityType`: Type of item to rename as defined in [swNotifyEntityType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swNotifyEntityType_e.html)
- `oldName`: Current name of the component document
- `NewName`: New name of the component document

## VBA Syntax

See [PreRenameItemNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~PreRenameItemNotify_EV.html).

## Examples

[Fire Notifications When Renaming Components (C#)](Fire_Notifications_When_Renaming_Components_Example_CSharp.htm)
[Fire Notifications When Renaming Components (VB.NET)](Fire_Notifications_When_Renaming_Components_Example_VBNET.htm)
[Fire Notifications When Renaming Components (VBA)](Fire_Notifications_When_Renaming_Components_Example_VB.htm)

## Remarks

This event is also fired when [IComponent2::MakeVirtual](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~MakeVirtual.html) is called.

If developing a C++ application, use [swAssemblyPreRenameItemNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
