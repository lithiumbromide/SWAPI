---
title: "CreateProfile Method (IProfileManager)"
project: ""
interface: "IProfileManager"
member: "CreateProfile"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IProfileManager~CreateProfile.html"
---

# CreateProfile Method (IProfileManager)

Creates the specified settings profile.

## Syntax

### Visual Basic

```vb
Function CreateProfile( _
   ByVal NewProfileName As System.String, _
   ByVal CopyFromProfileName As System.String, _
   ByVal NewProfileDesc As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool CreateProfile(
   System.string NewProfileName,
   System.string CopyFromProfileName,
   System.string NewProfileDesc
)
```

### JScript

```
function CreateProfile(
   NewProfileName : System.String,
   CopyFromProfileName : System.String,
   NewProfileDesc : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool CreateProfile(
   System.string* NewProfileName,
   System.string* CopyFromProfileName,
   System.string* NewProfileDesc
)
```

### C++/CLI

```cpp
System.bool CreateProfile(
   System.String^ NewProfileName,
   System.String^ CopyFromProfileName,
   System.String^ NewProfileDesc
)
```

### Parameters

- `NewProfileName`: Name of new profile
- `CopyFromProfileName`: Name of profile to copy into new profile
- `NewProfileDesc`: Description of new profile

### Return Value

True if profile successfully created, false if not

## See Also

[IProfileManager Interface](Interop.dsAutomation~Interop.dsAutomation.IProfileManager.html)
[IProfileManager Members](Interop.dsAutomation~Interop.dsAutomation.IProfileManager_members.html)

## Availability

DraftSight 2024 SP0
