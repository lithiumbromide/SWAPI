---
title: "ICommandManager Interface"
project: "SOLIDWORKS API Help"
interface: "ICommandManager"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager.html"
---

# ICommandManager Interface

Allows add-in applications to add and remove [CommandGroups](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandGroup.html) (menus and toolbars) to the CommandManager.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICommandManager
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandManager
```

### C#

```csharp
public interface ICommandManager
```

### C++/CLI

```cpp
public interface class ICommandManager
```

## VBA Syntax

See [CommandManager](ms-its:sldworksapivb6.chm::/sldworks~CommandManager.html).

## Examples

[Create Flyouts in the CommandManager (C#)](Create_Flyouts_in_the_CommandManager_Example_CSharp.htm)
[Create Flyouts in the CommandManager (VB.NET)](Create_Flyouts_in_the_CommandManager_Example_VBNET.htm)
[Create Submenus in the CommandManager (C#)](Create_Submenus_in_the_CommandManager_Example_CSharp.htm)

## Remarks

Only one CommandManager can exist in an add-in application.

See [CommandManager and CommandGroups](sldworksAPIProgGuide.chm::/OVERVIEW/CommandManager_and_CommandGroups.htm) to learn how to create a CommandManager and add and remove CommandGroups.

## Accessors

[ISldWorks::GetCommandManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetCommandManager.html)

## Access Diagram

[CommandManager](SWObjectModel.pdf#CommandManager)

## See Also

[ICommandManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
