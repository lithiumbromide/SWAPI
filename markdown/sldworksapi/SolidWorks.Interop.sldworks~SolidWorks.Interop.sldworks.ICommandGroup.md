---
title: "ICommandGroup Interface"
project: "SOLIDWORKS API Help"
interface: "ICommandGroup"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.html"
---

# ICommandGroup Interface

Allows add-in applications to create toolbars and menu items, including flyout toolbars and submenus, and add them to the [ICommandManager.](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager.html)

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICommandGroup
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandGroup
```

### C#

```csharp
public interface ICommandGroup
```

### C++/CLI

```cpp
public interface class ICommandGroup
```

## VBA Syntax

See [CommandGroup](ms-its:sldworksapivb6.chm::/sldworks~CommandGroup.html).

## Examples

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)
[Create Submenus in the CommandManager (C#)](Create_Submenus_in_the_CommandManager_Example_CSharp.htm)

## Remarks

See [CommandManager and CommandGroups](sldworksAPIProgGuide.chm::/OVERVIEW/CommandManager_and_CommandGroups.htm) to learn how to add and remove CommandGroups.

## Accessors

[ICommandManager::GetCommandGroup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~GetCommandGroup.html)

[ICommandManager::GetGroups](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~GetGroups.html) and [ICommandManager::IGetGroups](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~IGetGroups.html)

[ICommandManager::CreateCommandGroup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~CreateCommandGroup.html)

[ICommandManager::AddContextMenu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~AddContextMenu.html)

## Access Diagram

[CommandGroup](SWObjectModel.pdf#CommandGroup)

## See Also

[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
