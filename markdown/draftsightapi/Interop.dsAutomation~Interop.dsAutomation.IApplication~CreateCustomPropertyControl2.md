---
title: "CreateCustomPropertyControl2 Method (IApplication)"
project: ""
interface: "IApplication"
member: "CreateCustomPropertyControl2"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateCustomPropertyControl2.html"
---

# CreateCustomPropertyControl2 Method (IApplication)

Creates a custom tab.

## Syntax

### Visual Basic

```vb
Function CreateCustomPropertyControl2( _
   ByVal ControlName As System.String, _
   ByVal InitialArea As dsCustomPropertyControlArea_e, _
   ByVal AllowedAreas As System.Integer _
) As CustomPropertyControl
```

### C#

```csharp
CustomPropertyControl CreateCustomPropertyControl2(
   System.string ControlName,
   dsCustomPropertyControlArea_e InitialArea,
   System.int AllowedAreas
)
```

### JScript

```
function CreateCustomPropertyControl2(
   ControlName : System.String,
   InitialArea : dsCustomPropertyControlArea_e,
   AllowedAreas : System.int
) : CustomPropertyControl;
```

### Managed Extensions for C++

```
CustomPropertyControl* CreateCustomPropertyControl2(
   System.string* ControlName,
   dsCustomPropertyControlArea_e InitialArea,
   System.int AllowedAreas
)
```

### C++/CLI

```cpp
CustomPropertyControl^ CreateCustomPropertyControl2(
   System.String^ ControlName,
   dsCustomPropertyControlArea_e InitialArea,
   System.int AllowedAreas
)
```

### Parameters

- `ControlName`: Name of the application-defined tab
- `InitialArea`: Location where the application-defined tab is initially docked as defined in [dsCustomPropertyControlArea_e](Interop.dsAutomation~Interop.dsAutomation.dsCustomPropertyControlArea_e.html)
- `AllowedAreas`: Locations where a user is allowed to dock the application-defined tab as defined in [dsCustomPropertyControlArea_e](Interop.dsAutomation~Interop.dsAutomation.dsCustomPropertyControlArea_e.html)

### Return Value

[Custom tab](Interop.dsAutomation~Interop.dsAutomation.ICustomPropertyControl.html)

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)

## Availability

DraftSight V1R5.0
