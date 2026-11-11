---
title: "IWorkspace Interface"
project: ""
interface: "IWorkspace"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IWorkspace.html"
---

# IWorkspace Interface

Allows access to a workspace of the DraftSight user interface.

## Syntax

### Visual Basic

```vb
Public Interface IWorkspace
```

### C#

```csharp
public interface IWorkspace
```

### JScript

```
public interface IWorkspace
```

### Managed Extensions for C++

```
public __gc __interface IWorkspace
```

### C++/CLI

```cpp
public interface class IWorkspace
```

## Examples

See the following ribbon-based add-in projects:

- `install_dir`**\APISDK\samples\C#\Simple\Ribbon**
- `install_dir`**\APISDK\samples\C++\Simple\Ribbon**
- `install_dir`**\APISDK\samples\COM\Simple\RibbonSample**
- `install_dir`**\APISDK\samples\JS\Simple\RibbonSample.html**

## Remarks

A workspace is a data container that combines user-interface elements such as menus, toolbars, and ribbon components. When a workspace is activated, all of its components appear.

As of DraftSight 2017 SP0, two types of workspaces are supported:

- Classic Default, which provides the traditional [menu](Interop.dsAutomation~Interop.dsAutomation.IMenuItem.html) and [toolbar](Interop.dsAutomation~Interop.dsAutomation.IToolbar.html)s.
- Ribbon-based, which organizes groups of [command](Interop.dsAutomation~Interop.dsAutomation.IRibbonCommandButton.html)s into [tab](Interop.dsAutomation~Interop.dsAutomation.IRibbonTab.html)s, [panel](Interop.dsAutomation~Interop.dsAutomation.IRibbonPanel.html)s, [row](Interop.dsAutomation~Interop.dsAutomation.IRibbonRow.html)s, and [row panel](Interop.dsAutomation~Interop.dsAutomation.IRibbonRowPanel.html)s. Adding a new ribbon-based workspace automatically creates a [system menu](Interop.dsAutomation~Interop.dsAutomation.IRibbonSystemMenu.html) and a [quick access toolbar](Interop.dsAutomation~Interop.dsAutomation.IRibbonQuickAccessBar.html).

## Accessors

[IApplication::AddWorkspace](Interop.dsAutomation~Interop.dsAutomation.IApplication~AddWorkspace.html)

[IApplication::GetActiveWorkspace](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetActiveWorkspace.html)

[IApplication::GetWorkspace](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetWorkspace.html)

[IApplication::GetWorkspaces](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetWorkspaces.html)

## Access Diagram

DSObjectModel.pdf#Workspace

[Workspace](DSObjectModel.pdf#Workspace)

## See Also

[IWorkspace Members](Interop.dsAutomation~Interop.dsAutomation.IWorkspace_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
