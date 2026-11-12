---
title: "IToolbarItem Interface"
project: ""
interface: "IToolbarItem"
member: ""
kind: "interface"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IToolbarItem.html"
---

# IToolbarItem Interface

Allows access to a toolbar item.

## Syntax

### Visual Basic

```vb
Public Interface IToolbarItem
```

### C#

```csharp
public interface IToolbarItem
```

### JScript

```
public interface IToolbarItem
```

### Managed Extensions for C++

```
public __gc __interface IToolbarItem
```

### C++/CLI

```cpp
public interface class IToolbarItem
```

## Examples

The following code snippets show how to add a toolbar button with a ToolTip to a toolbar:

- COM native C++ (from the DraftSight API [COM native C++ template file](GettingStarted-draftsightapi.html) **DsAddinConnection.cpp**)
- [C++](#CPP) ( from the DraftSight API [C++ template file](GettingStarted-draftsightapi.html) **dsAddinConnection.cpp**)

##### COM native C++

IToolbarPtr pToolbar = m_DsApp->AddToolbar( m_sApiUuid, dsUIState_Document, L"DsAddin Toolbar");

IToolbarItemPtr pToolbarItem;

pToolbarItem = pToolbar->InsertToolbarItem( m_sApiUuid, dsToolBarItemType_UserCommand, ++position, L"Open Notepad", pNotepad.GetUserCommandID() );

##### C++

dsToolbar_ptr pToolbar;

dsApp->AddToolbar( myApplication::appID, dsUIState_Document, ToolbarName, &pToolbar );

if

( NULL != pToolbar )

{

dsToolbarItem_ptr pToolbarItem;

dsString ButtonName = L

"Notepad"

;

dsString UserCmdID;

pMenu->GetID( &UserCmdID );

pToolbar->InsertToolbarItem( myApplication::appID, dsToolBarItemType_UserCommand, 1, ButtonName, UserCmdID, &pToolbarItem );

[Back to top](#exampleBookmark)

## Remarks

To display the list of available toolbars, right-click a toolbar in the DraftSight user interface and select **Toolbars** to open the Specify Toolbars dialog.

## Accessors

[IToolbar::GetToolBarItems](Interop.dsAutomation~Interop.dsAutomation.IToolbar~GetToolbarItems.html)

[IToolbar::InsertToolbarItem](Interop.dsAutomation~Interop.dsAutomation.IToolbar~InsertToolbarItem.html)

## Access Diagram

DSObjectModel.pdf#ToolbarItem

[ToolbarItem](DSObjectModel.pdf#ToolbarItem)

## See Also

[IToolbarItem Members](Interop.dsAutomation~Interop.dsAutomation.IToolbarItem_members.html)
[Interop.dsAutomation Namespace](Interop.dsAutomation~Interop.dsAutomation_namespace.html)
[IToolbar Interface](Interop.dsAutomation~Interop.dsAutomation.IToolbar.html)
