---
title: "GetID Method (IUserCommand)"
project: ""
interface: "IUserCommand"
member: "GetID"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IUserCommand~GetID.html"
---

# GetID Method (IUserCommand)

Gets the user command's ID.

## Syntax

### Visual Basic

```vb
Function GetID() As System.String
```

### C#

```csharp
System.string GetID()
```

### JScript

```
function GetID() : System.String;
```

### Managed Extensions for C++

```
System.string* GetID();
```

### C++/CLI

```cpp
System.String^ GetID();
```

### Return Value

User command's ID (see **Remarks**)

## Examples

This code snippet shows how to get the user command's ID (from the DraftSight API [COM native C++ template files](GettingStarted-draftsightapi.html) **DsAddinUserCommand.h** and **DsAddinUserCommand.cpp**).

##### COM native C++

**DsAddinUserCommand.h**

bstr_t GetUserCommandID();

**DsAddinUserCommand.cpp**

bstr_t DsAddinUserCommand::GetUserCommandID()
{
return m_DsUserCommand->GetID();
}

## Examples

[Create Context-sensitive Menu Items (C#)](Create_Context-sensitive_Menu_Items_Example_CSharp.htm)
[Create Context-sensitive Menu Items (VB.NET)](Create_Context-sensitive_Menu_Items_Example_VBNET.htm)
[Create Context-sensitive Menu Items (VBA)](Create_Context-sensitive_Menu_Items_Example_VBA.htm)

## Remarks

The return value is the string specified for [IMenuItem::InsertMenuItem's](Interop.dsAutomation~Interop.dsAutomation.IMenuItem~InsertMenuItem.html) or [IToolBar::InsertToolBarItem's](Interop.dsAutomation~Interop.dsAutomation.IToolbar~InsertToolbarItem.html) UserCmdID parameter.

## See Also

[IUserCommand Interface](Interop.dsAutomation~Interop.dsAutomation.IUserCommand.html)
[IUserCommand Members](Interop.dsAutomation~Interop.dsAutomation.IUserCommand_members.html)
[IUserCommand::SetID Method ()](Interop.dsAutomation~Interop.dsAutomation.IUserCommand~SetID.html)

## Availability

DraftSight V1R1
