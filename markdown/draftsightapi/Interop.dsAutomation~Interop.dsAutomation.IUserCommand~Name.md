---
title: "Name Property (IUserCommand)"
project: ""
interface: "IUserCommand"
member: "Name"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IUserCommand~Name.html"
---

# Name Property (IUserCommand)

Gets or sets the user command's name.

## Syntax

### Visual Basic

```vb
Property Name As System.String
```

### C#

```csharp
System.string Name {get; set;}
```

### JScript

```
function get,set Name : System.String
```

### Managed Extensions for C++

```
__property System.string* get_Name();
__property void set_Name(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ Name {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

User command's name

## Remarks

The return value is the string specified for [IMenuItem::InsertMenuItem's](Interop.dsAutomation~Interop.dsAutomation.IMenuItem~InsertMenuItem.html) or [IToolBar::InsertToolBarItem's](Interop.dsAutomation~Interop.dsAutomation.IToolbar~InsertToolbarItem.html) ItemName parameter or the string set by this property.

## See Also

[IUserCommand Interface](Interop.dsAutomation~Interop.dsAutomation.IUserCommand.html)
[IUserCommand Members](Interop.dsAutomation~Interop.dsAutomation.IUserCommand_members.html)

## Availability

DraftSight V1R1
