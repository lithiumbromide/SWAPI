---
title: "CreateFlyoutGroup Method (ICommandManager)"
project: "SOLIDWORKS API Help"
interface: "ICommandManager"
member: "CreateFlyoutGroup"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CreateFlyoutGroup.html"
---

# CreateFlyoutGroup Method (ICommandManager)

Obsolete. Superseded by [ICommandManager::CreateFlyoutGroup2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CreateFlyoutGroup2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateFlyoutGroup( _
   ByVal UserID As System.Integer, _
   ByVal Title As System.String, _
   ByVal ToolTip As System.String, _
   ByVal Hint As System.String, _
   ByVal SmallIcon As System.String, _
   ByVal LargeIcon As System.String, _
   ByVal SmallImageList As System.String, _
   ByVal LargeImageList As System.String, _
   ByVal CallbackFunction As System.String, _
   ByVal UpdateCallbackFunction As System.String _
) As FlyoutGroup
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandManager
Dim UserID As System.Integer
Dim Title As System.String
Dim ToolTip As System.String
Dim Hint As System.String
Dim SmallIcon As System.String
Dim LargeIcon As System.String
Dim SmallImageList As System.String
Dim LargeImageList As System.String
Dim CallbackFunction As System.String
Dim UpdateCallbackFunction As System.String
Dim value As FlyoutGroup

value = instance.CreateFlyoutGroup(UserID, Title, ToolTip, Hint, SmallIcon, LargeIcon, SmallImageList, LargeImageList, CallbackFunction, UpdateCallbackFunction)
```

### C#

```csharp
FlyoutGroup CreateFlyoutGroup(
   System.int UserID,
   System.string Title,
   System.string ToolTip,
   System.string Hint,
   System.string SmallIcon,
   System.string LargeIcon,
   System.string SmallImageList,
   System.string LargeImageList,
   System.string CallbackFunction,
   System.string UpdateCallbackFunction
)
```

### C++/CLI

```cpp
FlyoutGroup^ CreateFlyoutGroup(
   System.int UserID,
   System.String^ Title,
   System.String^ ToolTip,
   System.String^ Hint,
   System.String^ SmallIcon,
   System.String^ LargeIcon,
   System.String^ SmallImageList,
   System.String^ LargeImageList,
   System.String^ CallbackFunction,
   System.String^ UpdateCallbackFunction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UserID`: Unique, user-defined ID for the new flyout
- `Title`: Name of the flyout to create
- `ToolTip`: ToolTip for the new flyout
- `Hint`: Text displayed in SOLIDWORKS Design status bar when a user's mouse pointer is over the flyout
- `SmallIcon`: Path to the small bitmap or PNG used in the flyout
- `LargeIcon`: Path to the large bitmap or PNG used in the flyout
- `SmallImageList`: Path to the bitmap or PNG containing all of the small button and separator images for this flyout
- `LargeImageList`: Path to the bitmap or PNG containing all of the large button and separator images for this flyout
- `CallbackFunction`: Function to call when the flyout is selected
- `UpdateCallbackFunction`: Optional update function that controls the state of the item; if specified, then SOLIDWORKS Design calls this function before displaying the item (see **Remarks**)

  | If this update function returns... | Then the SOLIDWORKS Design... |
  | --- | --- |
  | 0 | Disables the item |
  | 1 | Enables the item; this is the default state if no update function is specified |

### Return Value

[IFlyoutGroup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFlyoutGroup.html)

## VBA Syntax

See [CommandManager::CreateFlyoutGroup](ms-its:sldworksapivb6.chm::/sldworks~CommandManager~CreateFlyoutGroup.html).

## Remarks

After creating the flyout, display it on a CommandManager tab by calling [ICommandTabBox::AddCommands](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandTabBox~AddCommands.html). Call [IFlyoutGroup::AddContextMenuFlyout](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFlyoutGroup~AddContextMenuFlyout.html) to add it to context menus. Call [IFlyoutGroup::AddCommandItem](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFlyoutGroup~AddCommandItem.html) to add menu items to the flyout group.

If any flyout menu items are enabled, then the flyout button cannot be disabled by the flyout group's UpdateCallbackFunction. The sensitivity of the top-level flyout button is always determined by its enabled menu items. Disabled flyout menu items do not appear in the flyout menu. If there are no flyout menu items, then control of the top-level flyout button is returned to the flyout group's UpdateCallbackFunction.

## See Also

[ICommandManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html)
[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.html)
[ICommandManager::GetFlyoutGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetFlyoutGroup.html)
[ICommandManager::GetFlyoutGroups Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetFlyoutGroups.html)
[ICommandManager::RemoveFlyoutGroup Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~RemoveFlyoutGroup.html)
[ICommandManager::NumberOfFlyoutGroups Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~NumberOfFlyoutGroups.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
