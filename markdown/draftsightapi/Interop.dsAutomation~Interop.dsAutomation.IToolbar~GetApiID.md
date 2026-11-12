---
title: "GetApiID Method (IToolbar)"
project: ""
interface: "IToolbar"
member: "GetApiID"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IToolbar~GetApiID.html"
---

# GetApiID Method (IToolbar)

Gets the UUID of the add-in or non add-in application for the toolbar.

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

The return value is the string specified for [IApplication::AddToolbar's](Interop.dsAutomation~Interop.dsAutomation.IApplication~AddToolbar.html) ApiUuid parameter.

## See Also

[IToolbar Interface](Interop.dsAutomation~Interop.dsAutomation.IToolbar.html)
[IToolbar Members](Interop.dsAutomation~Interop.dsAutomation.IToolbar_members.html)

## Availability

DraftSight V1R1.2
