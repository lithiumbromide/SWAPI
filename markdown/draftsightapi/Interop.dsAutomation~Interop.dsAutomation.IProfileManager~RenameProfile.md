---
title: "RenameProfile Method (IProfileManager)"
project: ""
interface: "IProfileManager"
member: "RenameProfile"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IProfileManager~RenameProfile.html"
---

# RenameProfile Method (IProfileManager)

Renames the specified profile.

## Syntax

### Visual Basic

```vb
Function RenameProfile( _
   ByVal NewProfileName As System.String, _
   ByVal OldProfileName As System.String, _
   ByVal NewProfileDesc As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool RenameProfile(
   System.string NewProfileName,
   System.string OldProfileName,
   System.string NewProfileDesc
)
```

### JScript

```
function RenameProfile(
   NewProfileName : System.String,
   OldProfileName : System.String,
   NewProfileDesc : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool RenameProfile(
   System.string* NewProfileName,
   System.string* OldProfileName,
   System.string* NewProfileDesc
)
```

### C++/CLI

```cpp
System.bool RenameProfile(
   System.String^ NewProfileName,
   System.String^ OldProfileName,
   System.String^ NewProfileDesc
)
```

### Parameters

- `NewProfileName`: New name of profile
- `OldProfileName`: Old name of profile
- `NewProfileDesc`: Description of new profile

### Return Value

True if profile successfully renamed, false if not

## See Also

[IProfileManager Interface](Interop.dsAutomation~Interop.dsAutomation.IProfileManager.html)
[IProfileManager Members](Interop.dsAutomation~Interop.dsAutomation.IProfileManager_members.html)

## Availability

DraftSight 2024 SP0
