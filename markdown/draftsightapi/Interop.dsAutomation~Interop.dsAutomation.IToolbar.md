---
title: "IToolbar Interface"
project: ""
interface: "IToolbar"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IToolbar.html"
---

# IToolbar Interface

Allows access to a toolbar.

## Syntax

### Visual Basic

```vb
Public Interface IToolbar
```

### C#

```csharp
public interface IToolbar
```

### JScript

```
public interface IToolbar
```

### Managed Extensions for C++

```
public __gc __interface IToolbar
```

### C++/CLI

```cpp
public interface class IToolbar
```

## Examples

The following code snippets show how to add a toolbar to the list of available toolbars:

- COM native C++(from the DraftSight API [COM native C++ template file](GettingStarted-draftsightapi.html) **DsAddinConnection.cpp**)
- C++ (from the DraftSight API [C++ template file](GettingStarted-draftsightapi.html) **dsAddinConnection.cpp**)

##### COM native C++

IToolbarPtr pToolbar = m_DsApp->AddToolbar( m_sApiUuid, dsUIState_Document, L"DsAddin Toolbar");

##### C++

dsString ToolbarName = L

"QAddIn1_Toolbar"

;

dsToolbar_ptr pToolbar;

dsApp->AddToolbar( myApplication::appID, dsUIState_Document, ToolbarName, &pToolbar );

## Remarks

To display the list of available toolbars, right-click a toolbar in the DraftSight user interface and select **Toolbars** to open the Specify Toolbars dialog.

## Accessors

[IApplication::AddToolbar](Interop.dsAutomation~Interop.dsAutomation.IApplication~AddToolbar.html)

[IApplication::GetToolbars](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetToolbars.html)

[IWorkspace::AddToolbar](Interop.dsAutomation~Interop.dsAutomation.IWorkspace~AddToolbar.html)

[IWorkspace::GetToolbars](Interop.dsAutomation~Interop.dsAutomation.IWorkspace~GetToolbars.html)

## Access Diagram

DSObjectModel.pdf#Toolbar

[Toolbar](DSObjectModel.pdf#Toolbar)

## See Also

[IToolbar Members](Interop.dsAutomation~Interop.dsAutomation.IToolbar_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IToolbarItem Interface](Interop.dsAutomation~Interop.dsAutomation.IToolbarItem.html)
