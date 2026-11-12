---
title: "GetWorkspace Method (IApplication)"
project: ""
interface: "IApplication"
member: "GetWorkspace"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~GetWorkspace.html"
---

# GetWorkspace Method (IApplication)

Gets the specified workspace for the DraftSight user interface.

## Syntax

### Visual Basic

```vb
Function GetWorkspace( _
   ByVal Name As System.String _
) As WorkSpace
```

### C#

```csharp
WorkSpace GetWorkspace(
   System.string Name
)
```

### JScript

```
function GetWorkspace(
   Name : System.String
) : WorkSpace;
```

### Managed Extensions for C++

```
WorkSpace* GetWorkspace(
   System.string* Name
)
```

### C++/CLI

```cpp
WorkSpace^ GetWorkspace(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of workspace

### Return Value

[IWorkspace](Interop.dsAutomation~Interop.dsAutomation.IWorkspace.html)

## Examples

See the following ribbon-based add-in projects:

- `install_dir`**\APISDK\samples\C#\Simple\Ribbon**
- `install_dir`**\APISDK\samples\C++\Simple\Ribbon**
- `install_dir`**\APISDK\samples\COM\Simple\RibbonSample**
- `install_dir`**\APISDK\samples\JS\Simple\RibbonSample.html**

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::AddWorkspace Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~AddWorkspace.html)
[IApplication::GetActiveWorkspace Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetActiveWorkspace.html)
[IApplication::GetWorkspaces Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetWorkspaces.html)

## Availability

DraftSight 2017 SP0
