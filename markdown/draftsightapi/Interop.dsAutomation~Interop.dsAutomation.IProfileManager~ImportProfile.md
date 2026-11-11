---
title: "ImportProfile Method (IProfileManager)"
project: ""
interface: "IProfileManager"
member: "ImportProfile"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IProfileManager~ImportProfile.html"
---

# ImportProfile Method (IProfileManager)

Reads the specified profile that was created by an export.

## Syntax

### Visual Basic

```vb
Function ImportProfile( _
   ByVal ProfileName As System.String, _
   ByVal ImportFileName As System.String, _
   ByVal ProfileDesc As System.String, _
   ByVal IsImportPathInfo As System.Boolean _
) As System.Boolean
```

### C#

```csharp
System.bool ImportProfile(
   System.string ProfileName,
   System.string ImportFileName,
   System.string ProfileDesc,
   System.bool IsImportPathInfo
)
```

### JScript

```
function ImportProfile(
   ProfileName : System.String,
   ImportFileName : System.String,
   ProfileDesc : System.String,
   IsImportPathInfo : System.boolean
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool ImportProfile(
   System.string* ProfileName,
   System.string* ImportFileName,
   System.string* ProfileDesc,
   System.bool IsImportPathInfo
)
```

### C++/CLI

```cpp
System.bool ImportProfile(
   System.String^ ProfileName,
   System.String^ ImportFileName,
   System.String^ ProfileDesc,
   System.bool IsImportPathInfo
)
```

### Parameters

- `ProfileName`: Name of profile to create
- `ImportFileName`: Pathname of XML profile to read
- `ProfileDesc`: Description of profile
- `IsImportPathInfo`: True to remember import path information, false to not

### Return Value

True if profile successfully imported, false if not

## See Also

[IProfileManager Interface](Interop.dsAutomation~Interop.dsAutomation.IProfileManager.html)
[IProfileManager Members](Interop.dsAutomation~Interop.dsAutomation.IProfileManager_members.html)
[IProfileManager::ExportProfile Method ()](Interop.dsAutomation~Interop.dsAutomation.IProfileManager~ExportProfile.html)

## Availability

DraftSight 2024 SP0
