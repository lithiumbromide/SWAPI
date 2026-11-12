---
title: "CreateCommandGroup Method (ICommandManager)"
project: "SOLIDWORKS API Help"
interface: "ICommandManager"
member: "CreateCommandGroup"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CreateCommandGroup.html"
---

# CreateCommandGroup Method (ICommandManager)

Obsolete. Superseded by [ICommandManager::CreateCommandGroup2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~CreateCommandGroup2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateCommandGroup( _
   ByVal UserID As System.Integer, _
   ByVal Title As System.String, _
   ByVal ToolTip As System.String, _
   ByVal Hint As System.String, _
   ByVal Position As System.Integer _
) As CommandGroup
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandManager
Dim UserID As System.Integer
Dim Title As System.String
Dim ToolTip As System.String
Dim Hint As System.String
Dim Position As System.Integer
Dim value As CommandGroup

value = instance.CreateCommandGroup(UserID, Title, ToolTip, Hint, Position)
```

### C#

```csharp
CommandGroup CreateCommandGroup(
   System.int UserID,
   System.string Title,
   System.string ToolTip,
   System.string Hint,
   System.int Position
)
```

### C++/CLI

```cpp
CommandGroup^ CreateCommandGroup(
   System.int UserID,
   System.String^ Title,
   System.String^ ToolTip,
   System.String^ Hint,
   System.int Position
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserID`: Unique user-defined ID for this CommandGroup
- `Title`: Name of the CommandGroup to create (see **Remarks**)
- `ToolTip`: ToolTip for this CommandGroup
- `Hint`: Text displayed in SOLIDWORKS status bar when a user's mouse pointer is over this CommandGroup
- `Position`: Position of the CommandGroup in the CommandManager for all document templates (see **Remarks**)

  NOTE: Specify 0 to add the CommandGroup to the beginning of the CommandMananger, or specify -1 to add it to the end of the CommandManager.

### Return Value

Pointer to [ICommandGroup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup.html) object

## VBA Syntax

See [CommandManager::CreateCommandGroup](ms-its:sldworksapivb6.chm::/sldworks~CommandManager~CreateCommandGroup.html).

## Remarks

You can also use [ICommandGroup::MenuPosition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~HasMenu.html) to control the position of the CommandGroup in specific document templates.

If you change the definition of an existing CommandGroup (i.e., add or remove toolbar buttons), you must assign a new unique user-defined UserID to that CommandGroup. You must perform this action to avoid conflicts with any previously existing CommandGroupa and to allow for backward and forward compatibility of the CommandGroups in your application.

To add a CommandGroup to an existing SOLIDWORKS menu, specify the name of a parent menu in Title. For example, to add a CommandGroup to the Help menu, specify:

Visual Basic: "&Help/MyApp Help"
Visual C++ or C#: "&Help\\MyApp Help"

**NOTE**: If you do not specify the name of a parent menu in Title, then the menu item appears on the Tools menu below the **Xpress Products** menu item.

You can turn off all menus or all toolbars for a CommandGroup . See [ICommandGroup::HasMenu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~HasMenu.html) and [ICommandGroup::HasToolbar](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup~HasToolbar.html) for details.

## See Also

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html)
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.html)
[ICommandManager::RemoveCommandGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveCommandGroup.html)
[ICommandManager::GetCommandGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetCommandGroup.html)
[ICommandManager::GetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetGroups.html)
[ICommandManager::IGetGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetGroups.html)
[ICommandManager::NumberOfGroups Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~NumberOfGroups.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
