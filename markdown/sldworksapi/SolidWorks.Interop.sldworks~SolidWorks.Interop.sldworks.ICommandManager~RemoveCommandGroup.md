---
title: "RemoveCommandGroup Method (ICommandManager)"
project: "SOLIDWORKS API Help"
interface: "ICommandManager"
member: "RemoveCommandGroup"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveCommandGroup.html"
---

# RemoveCommandGroup Method (ICommandManager)

Obsolete. Superseded by [ICommandManager::RemoveCommandGroup2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~RemoveCommandGroup2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveCommandGroup( _
   ByVal UserID As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandManager
Dim UserID As System.Integer
Dim value As System.Boolean

value = instance.RemoveCommandGroup(UserID)
```

### C#

```csharp
System.bool RemoveCommandGroup(
   System.int UserID
)
```

### C++/CLI

```cpp
System.bool RemoveCommandGroup(
   System.int UserID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserID`: User-defined ID for this CommandGroup

### Return Value

True if the CommandGroup is removed, false if not

## VBA Syntax

See [CommandManager::RemoveCommandGroup](ms-its:sldworksapivb6.chm::/sldworks~CommandManager~RemoveCommandGroup.html).

## Remarks

This method removes CommandGroups created using [ICommandManager::AddContextMenu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~AddContextMenu.html) and [ICommandManager::CreateCommandGroup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~CreateCommandGroup.html).

## See Also

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html)
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.html)
[ICommandManager::GetCommandGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandGroup.html)
[ICommandManager::GetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetGroups.html)
[ICommandManager::IGetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetGroups.html)
[ICommandManager::NumberOfGroups Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~NumberOfGroups.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
