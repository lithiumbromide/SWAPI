---
title: "AddToolbar Method (IApplication)"
project: ""
interface: "IApplication"
member: "AddToolbar"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~AddToolbar.html"
---

# AddToolbar Method (IApplication)

Obsolete. Superseded by [IWorkspace::AddToolbar](Interop.dsAutomation~Interop.dsAutomation.IWorkspace~AddToolbar.html).

## Syntax

### Visual Basic

```vb
Function AddToolbar( _
   ByVal ApiUuid As System.String, _
   ByVal UIState As dsUIState_e, _
   ByVal ToolBarName As System.String _
) As Toolbar
```

### C#

```csharp
Toolbar AddToolbar(
   System.string ApiUuid,
   dsUIState_e UIState,
   System.string ToolBarName
)
```

### JScript

```
function AddToolbar(
   ApiUuid : System.String,
   UIState : dsUIState_e,
   ToolBarName : System.String
) : Toolbar;
```

### Managed Extensions for C++

```
Toolbar* AddToolbar(
   System.string* ApiUuid,
   dsUIState_e UIState,
   System.string* ToolBarName
)
```

### C++/CLI

```cpp
Toolbar^ AddToolbar(
   System.String^ ApiUuid,
   dsUIState_e UIState,
   System.String^ ToolBarName
)
```

### Parameters

- `ApiUuid`: UUID of the add-in or application
- `UIState`: Where to add the toolbar as defined in [dsUIState_e](Interop.dsAutomation~Interop.dsAutomation.dsUIState_e.html)
- `ToolBarName`: Name of the toolbar

### Return Value

[Toolbar](Interop.dsAutomation~Interop.dsAutomation.IToolbar.html)

## Examples

The following code snippets show how to add a toolbar to the Classic Default workspace:

- COM native C++(from the DraftSight API [COM native C++ template file](GettingStarted-draftsightapi.html) **DsAddinConnection.cpp**)
- C++ (from the DraftSight API [C++ template file](GettingStarted-draftsightapi.html) **dsAddinConnection.cpp**)

##### COM native C++

IToolbarPtr pToolbar = m_DsApp->AddToolbar( m_sApiUuid, dsUIState_Document, L"DsAddin Toolbar");

##### C++

dsString ToolbarName = L"QAddIn1_Toolbar";

dsToolbar_ptr pToolbar;

dsApp->AddToolbar( myApplication::appID, dsUIState_Document, ToolbarName, &pToolbar );

## Remarks

This method is valid only for the Classic Default workspace as of DraftSight 2017 SP0.

To display the list of available toolbars, right-click a toolbar in the DraftSight user interface and select **Toolbars** to open the Specify Toolbars dialog.

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::GetToolbars Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetToolbars.html)

## Availability

DraftSight V1R1
