---
title: "AbortRunningCommand Method (IApplication)"
project: ""
interface: "IApplication"
member: "AbortRunningCommand"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~AbortRunningCommand.html"
---

# AbortRunningCommand Method (IApplication)

Aborts the command that is executing.

## Syntax

### Visual Basic

```vb
Sub AbortRunningCommand()
```

### C#

```csharp
void AbortRunningCommand()
```

### JScript

```
function AbortRunningCommand();
```

### Managed Extensions for C++

```
void AbortRunningCommand();
```

### C++/CLI

```cpp
void AbortRunningCommand();
```

## Examples

[Transform Circle to Region (C#)](Transform_Circle_to_Region_Example_CSharp.htm)
[Transform Circle to Region (VB.NET)](Transform_Circle_to_Region_Example_VBNET.htm)
[Transform Circle to Region (VBA)](Transform_Circle_to_Region_Example_VBA.htm)

## Remarks

Only use this method in standalone applications or outside a command; otherwise, calling this command breaks the current command flow.

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::GetRunningCommand Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetRunningCommand.html)
[IApplication::RunCommand Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~RunCommand.html)
[IApplication::CreateCommand Method](Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateCommand.html)
[ICommand Interface](Interop.dsAutomation~Interop.dsAutomation.ICommand.html)

## Availability

DraftSight V1R1
