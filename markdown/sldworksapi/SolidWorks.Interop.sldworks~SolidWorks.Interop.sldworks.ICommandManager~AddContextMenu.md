---
title: "AddContextMenu Method (ICommandManager)"
project: "SOLIDWORKS API Help"
interface: "ICommandManager"
member: "AddContextMenu"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~AddContextMenu.html"
---

# AddContextMenu Method (ICommandManager)

Adds a new context-sensitive menu to the CommandManager.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddContextMenu( _
   ByVal UserID As System.Integer, _
   ByVal Title As System.String _
) As CommandGroup
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandManager
Dim UserID As System.Integer
Dim Title As System.String
Dim value As CommandGroup

value = instance.AddContextMenu(UserID, Title)
```

### C#

```csharp
CommandGroup AddContextMenu(
   System.int UserID,
   System.string Title
)
```

### C++/CLI

```cpp
CommandGroup^ AddContextMenu(
   System.int UserID,
   System.String^ Title
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserID`: User-defined ID for this context-sensitive menu
- `Title`: Name of the context-sensitive menu to add to the CommandManager

### Return Value

Pointer to [ICommandGroup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup.html) object

## VBA Syntax

See [CommandManager::AddContextMenu](ms-its:sldworksapivb6.chm::/sldworks~CommandManager~AddContextMenu.html).

## Remarks

A context-sensitive menu is a pop-up menu that is displayed when a user right-clicks a selectable object type defined by [ICommandGroup::SelectType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~SelectType.html) and, if the object type is a custom feature, [ICommandGroup::CustomNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~CustomNames.html).

You can turn off all menus or all toolbars for a CommandGroup. See [ICommandGroup::HasMenu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~HasMenu.html) and [ICommandGroup::HasToolbar](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~HasToolbar.html) for details.

## See Also

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html)
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.html)
[ICommandGroup::Name Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~Name.html)
[ICommandGroup::SelectType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~SelectType.html)
[ICommandManager::RemoveCommandGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveCommandGroup.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
