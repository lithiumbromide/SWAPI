---
title: "GetApiID Method (IMenuItem)"
project: ""
interface: "IMenuItem"
member: "GetApiID"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMenuItem~GetApiID.html"
---

# GetApiID Method (IMenuItem)

Gets the UUID of the add-in or non add-in application for the menu item.

## Syntax

### Visual Basic

```vb
Function GetApiID() As System.String
```

### C#

```csharp
System.string GetApiID()
```

### JScript

```
function GetApiID() : System.String;
```

### Managed Extensions for C++

```
System.string* GetApiID();
```

### C++/CLI

```cpp
System.String^ GetApiID();
```

### Return Value

UUID of the add-in or non add-in application

## Remarks

The return value is the string specified for [IMenuItem::InsertMenuItem's](Interop.dsAutomation~Interop.dsAutomation.IMenuItem~InsertMenuItem.html) ApiUuid parameter.

## See Also

[IMenuItem Interface](Interop.dsAutomation~Interop.dsAutomation.IMenuItem.html)
[IMenuItem Members](Interop.dsAutomation~Interop.dsAutomation.IMenuItem_members.html)

## Availability

DraftSight V1R1.2
