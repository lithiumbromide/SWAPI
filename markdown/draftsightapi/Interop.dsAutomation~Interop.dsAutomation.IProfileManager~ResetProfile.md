---
title: "ResetProfile Method (IProfileManager)"
project: ""
interface: "IProfileManager"
member: "ResetProfile"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IProfileManager~ResetProfile.html"
---

# ResetProfile Method (IProfileManager)

Sets the values in the specified profile to the default settings.

## Syntax

### Visual Basic

```vb
Function ResetProfile( _
   ByVal ProfileName As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool ResetProfile(
   System.string ProfileName
)
```

### JScript

```
function ResetProfile(
   ProfileName : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool ResetProfile(
   System.string* ProfileName
)
```

### C++/CLI

```cpp
System.bool ResetProfile(
   System.String^ ProfileName
)
```

### Parameters

- `ProfileName`: Name of profile to reset

### Return Value

True if profile successfully reset, false if not

## See Also

[IProfileManager Interface](Interop.dsAutomation~Interop.dsAutomation.IProfileManager.html)
[IProfileManager Members](Interop.dsAutomation~Interop.dsAutomation.IProfileManager_members.html)

## Availability

DraftSight 2024 SP0
