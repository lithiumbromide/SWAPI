---
title: "GetApiID Method (IToolbarItem)"
project: ""
interface: "IToolbarItem"
member: "GetApiID"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IToolbarItem~GetApiID.html"
---

# GetApiID Method (IToolbarItem)

Gets the UUID of the add-in or non add-in application for the toolbar item.

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

The return value is the string specified for [IToolbar::InsertToolbarItem's](Interop.dsAutomation~Interop.dsAutomation.IToolbar~InsertToolbarItem.html) ApiUuid parameter.

## See Also

[IToolbarItem Interface](Interop.dsAutomation~Interop.dsAutomation.IToolbarItem.html)
[IToolbarItem Members](Interop.dsAutomation~Interop.dsAutomation.IToolbarItem_members.html)

## Availability

DraftSight V1R1.2
