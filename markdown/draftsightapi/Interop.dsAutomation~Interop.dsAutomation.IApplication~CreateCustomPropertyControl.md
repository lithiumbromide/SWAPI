---
title: "CreateCustomPropertyControl Method (IApplication)"
project: ""
interface: "IApplication"
member: "CreateCustomPropertyControl"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateCustomPropertyControl.html"
---

# CreateCustomPropertyControl Method (IApplication)

Obsolete. Superseded by [IApplication::CreateCustomPropertyControl2](Interop.dsAutomation~Interop.dsAutomation.IApplication~CreateCustomPropertyControl2.html).

## Syntax

### Visual Basic

```vb
Function CreateCustomPropertyControl( _
   ByVal ControlName As System.String _
) As CustomPropertyControl
```

### C#

```csharp
CustomPropertyControl CreateCustomPropertyControl(
   System.string ControlName
)
```

### JScript

```
function CreateCustomPropertyControl(
   ControlName : System.String
) : CustomPropertyControl;
```

### Managed Extensions for C++

```
CustomPropertyControl* CreateCustomPropertyControl(
   System.string* ControlName
)
```

### C++/CLI

```cpp
CustomPropertyControl^ CreateCustomPropertyControl(
   System.String^ ControlName
)
```

### Parameters

- `ControlName`: Name of the application-defined tab

### Return Value

[Custom tab](Interop.dsAutomation~Interop.dsAutomation.ICustomPropertyControl.html)

## Remarks

The application-defined tab docks on the right side of the window.

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)

## Availability

DraftSight V1R1.3
