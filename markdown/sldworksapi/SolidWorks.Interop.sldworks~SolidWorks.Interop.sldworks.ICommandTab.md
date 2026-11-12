---
title: "ICommandTab Interface"
project: "SOLIDWORKS API Help"
interface: "ICommandTab"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab.html"
---

# ICommandTab Interface

Allows add-in applications to create tabs and add them to the [CommandManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager.html). The add-in application must create and clean up its own tabs.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICommandTab
```

### Visual Basic (Usage)

```vb
Dim instance As ICommandTab
```

### C#

```csharp
public interface ICommandTab
```

### C++/CLI

```cpp
public interface class ICommandTab
```

## VBA Syntax

See [CommandTab](ms-its:sldworksapivb6.chm::/sldworks~CommandTab.html).

## Examples

[Create CommandManager Tab and Tab Boxes (VB.NET)](Create_CommandManager_Tab_and_Tab_Boxes_Example_VB.NET.htm)

## Remarks

Your add-in must check to see if the tab already exists. If the tab already exists, then you should use that tab instead of creating a new tab. If your add-in does not check for an existing tab, then SOLIDWORKS will create a new tab each time it starts up.

Users can add buttons to and remove buttons from your CommandManager tab. However, if your add-in removes the CommandManager tab upon exiting SOLIDWORKS, then any customizations made by users will be lost.

## Accessors

[ICommandManager::AddCommandTab](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~AddCommandTab.html)

[ICommandManager::CommandTabs](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~CommandTabs.html)

[ICommandManager::GetCommandTab](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~GetCommandTab.html)

[ICommandManager::IGetCommandTabs](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommandManager~IGetCommandTabs.html)

[IModelDocExtension::GetCommandTabs](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetCommandTabs.html)

## Access Diagram

[CommandTab](SWObjectModel.pdf#CommandTab)

## See Also

[ICommandTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ICommandTabBox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox.html)
