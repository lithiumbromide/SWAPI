---
title: "AddWorkspace Method (IApplication)"
project: ""
interface: "IApplication"
member: "AddWorkspace"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~AddWorkspace.html"
---

# AddWorkspace Method (IApplication)

Adds the specified workspace to the list of DraftSight user-interface workspaces.

## Syntax

### Visual Basic

```vb
Function AddWorkspace( _
   ByVal WorkspaceName As System.String _
) As WorkSpace
```

### C#

```csharp
WorkSpace AddWorkspace(
   System.string WorkspaceName
)
```

### JScript

```
function AddWorkspace(
   WorkspaceName : System.String
) : WorkSpace;
```

### Managed Extensions for C++

```
WorkSpace* AddWorkspace(
   System.string* WorkspaceName
)
```

### C++/CLI

```cpp
WorkSpace^ AddWorkspace(
   System.String^ WorkspaceName
)
```

### Parameters

- `WorkspaceName`: Name of the new workspace

### Return Value

[IWorkspace](Interop.dsAutomation~Interop.dsAutomation.IWorkspace.html)

## Examples

See the following ribbon-based add-in projects:

- `install_dir`**\APISDK\samples\C#\Simple\Ribbon**
- `install_dir`**\APISDK\samples\C++\Simple\Ribbon**
- `install_dir`**\APISDK\samples\COM\Simple\RibbonSample**
- `install_dir`**\APISDK\samples\JS\Simple\RibbonSample.html**

## Remarks

After calling this method, call [IWorkspace::Activate](Interop.dsAutomation~Interop.dsAutomation.IWorkspace~Activate.html) to reload all of the user-interface components for the new workspace.

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::GetActiveWorkspace Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetActiveWorkspace.html)
[IApplication::GetWorkspace Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetWorkspace.html)
[IApplication::GetWorkspaces Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetWorkspaces.html)

## Availability

DraftSight 2017 SP0
