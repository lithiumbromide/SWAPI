---
title: "ExportProfile Method (IProfileManager)"
project: ""
interface: "IProfileManager"
member: "ExportProfile"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IProfileManager~ExportProfile.html"
---

# ExportProfile Method (IProfileManager)

Writes the specified profile as an XML file.

## Syntax

### Visual Basic

```vb
Function ExportProfile( _
   ByVal ProfileName As System.String, _
   ByVal ExportFileName As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool ExportProfile(
   System.string ProfileName,
   System.string ExportFileName
)
```

### JScript

```
function ExportProfile(
   ProfileName : System.String,
   ExportFileName : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool ExportProfile(
   System.string* ProfileName,
   System.string* ExportFileName
)
```

### C++/CLI

```cpp
System.bool ExportProfile(
   System.String^ ProfileName,
   System.String^ ExportFileName
)
```

### Parameters

- `ProfileName`: Name of profile to export
- `ExportFileName`: Pathname of XML file to create

### Return Value

True if profile successfully exported, false if not

## See Also

[IProfileManager Interface](Interop.dsAutomation~Interop.dsAutomation.IProfileManager.html)
[IProfileManager Members](Interop.dsAutomation~Interop.dsAutomation.IProfileManager_members.html)
[IProfileManager::ImportProfile Method ()](Interop.dsAutomation~Interop.dsAutomation.IProfileManager~ImportProfile.html)

## Availability

DraftSight 2024 SP0
