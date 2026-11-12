---
title: "GetSystemFiles Method (IApplication)"
project: ""
interface: "IApplication"
member: "GetSystemFiles"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~GetSystemFiles.html"
---

# GetSystemFiles Method (IApplication)

Gets access to the DraftSight options that get and set these system files: dictionary, font, Help, log, and support.

## Syntax

### Visual Basic

```vb
Function GetSystemFiles() As SystemFiles
```

### C#

```csharp
SystemFiles GetSystemFiles()
```

### JScript

```
function GetSystemFiles() : SystemFiles;
```

### Managed Extensions for C++

```
SystemFiles* GetSystemFiles();
```

### C++/CLI

```cpp
SystemFiles^ GetSystemFiles();
```

### Return Value

[ISystemFiles](Interop.dsAutomation~Interop.dsAutomation.ISystemFiles.html)

## Examples

[Set and Get System Files (C#)](Set_and_Get_System_Files_Example_CSharp.htm)
[Set and Get System Files (VB.NET)](Set_and_Get_System_Files_Example_VBNET.htm)
[Set and Get System Files (VBA)](Set_and_Get_System_Files_Example_VBA.htm)
[Get System Files (JavaScript)](Get_System_Files_Example_JS.htm)

## Remarks

The ISystemFiles interface corresponds to clicking **Tools > Options > File Locations > System** in the user interface.

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)

## Availability

DraftSight V1R3.0
