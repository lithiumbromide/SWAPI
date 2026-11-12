---
title: "SetActiveProfile Method (IProfileManager)"
project: ""
interface: "IProfileManager"
member: "SetActiveProfile"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IProfileManager~SetActiveProfile.html"
---

# SetActiveProfile Method (IProfileManager)

Sets the specified profile as active.

## Syntax

### Visual Basic

```vb
Function SetActiveProfile( _
   ByVal ProfileName As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool SetActiveProfile(
   System.string ProfileName
)
```

### JScript

```
function SetActiveProfile(
   ProfileName : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool SetActiveProfile(
   System.string* ProfileName
)
```

### C++/CLI

```cpp
System.bool SetActiveProfile(
   System.String^ ProfileName
)
```

### Parameters

- `ProfileName`: Name of profile to set active

### Return Value

True if active profile successfully set, false if not

## See Also

[IProfileManager Interface](Interop.dsAutomation~Interop.dsAutomation.IProfileManager.html)
[IProfileManager Members](Interop.dsAutomation~Interop.dsAutomation.IProfileManager_members.html)
[IProfileManager::GetActiveProfile Method ()](Interop.dsAutomation~Interop.dsAutomation.IProfileManager~GetActiveProfile.html)

## Availability

DraftSight 2024 SP0
