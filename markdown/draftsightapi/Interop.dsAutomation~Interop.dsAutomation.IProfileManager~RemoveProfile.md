---
title: "RemoveProfile Method (IProfileManager)"
project: ""
interface: "IProfileManager"
member: "RemoveProfile"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IProfileManager~RemoveProfile.html"
---

# RemoveProfile Method (IProfileManager)

Deletes the specified profile.

## Syntax

### Visual Basic

```vb
Function RemoveProfile( _
   ByVal ProfileName As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool RemoveProfile(
   System.string ProfileName
)
```

### JScript

```
function RemoveProfile(
   ProfileName : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool RemoveProfile(
   System.string* ProfileName
)
```

### C++/CLI

```cpp
System.bool RemoveProfile(
   System.String^ ProfileName
)
```

### Parameters

- `ProfileName`: Name of profile to delete (see **Remarks**)

### Return Value

True if profile successfully removed, false if not

## Remarks

You cannot delete the active profile.

## See Also

[IProfileManager Interface](Interop.dsAutomation~Interop.dsAutomation.IProfileManager.html)
[IProfileManager Members](Interop.dsAutomation~Interop.dsAutomation.IProfileManager_members.html)

## Availability

DraftSight 2024 SP0
