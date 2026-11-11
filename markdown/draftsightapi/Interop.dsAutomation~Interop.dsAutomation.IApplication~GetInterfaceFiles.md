---
title: "GetInterfaceFiles Method (IApplication)"
project: ""
interface: "IApplication"
member: "GetInterfaceFiles"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~GetInterfaceFiles.html"
---

# GetInterfaceFiles Method (IApplication)

Gets access to the DraftSight options that get and set default paths for these user-interface files: alias, custom icon, main customization, and custom menu.

## Syntax

### Visual Basic

```vb
Function GetInterfaceFiles() As InterfaceFiles
```

### C#

```csharp
InterfaceFiles GetInterfaceFiles()
```

### JScript

```
function GetInterfaceFiles() : InterfaceFiles;
```

### Managed Extensions for C++

```
InterfaceFiles* GetInterfaceFiles();
```

### C++/CLI

```cpp
InterfaceFiles^ GetInterfaceFiles();
```

### Return Value

[IInterfaceFiles](Interop.dsAutomation~Interop.dsAutomation.IInterfaceFiles.html)

## Examples

[Set and Get Paths of Interface Files (C#)](Set_and_Get_Paths_of_Interface_Files_Example_CSharp.htm)
[Set and Get Paths of Interface Files (VB.NET)](Set_and_Get_Paths_of_Interface_Files_Example_VBNET.htm)
[Set and Get Paths of Interface Files (VBA)](Set_and_Get_Paths_of_Interface_Files_Example_VBA.htm)

## Remarks

The IInterfaceFiles interface corresponds to clicking **Tools > Options > File Locations > Interface** in the user interface.

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)

## Availability

DraftSight V1R5.0
