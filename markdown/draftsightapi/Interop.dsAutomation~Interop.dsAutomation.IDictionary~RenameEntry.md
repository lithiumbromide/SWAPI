---
title: "RenameEntry Method (IDictionary)"
project: ""
interface: "IDictionary"
member: "RenameEntry"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDictionary~RenameEntry.html"
---

# RenameEntry Method (IDictionary)

Changes the name of the specified entity in the dictionary.

## Syntax

### Visual Basic

```vb
Function RenameEntry( _
   ByVal OldName As System.String, _
   ByVal NewName As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool RenameEntry(
   System.string OldName,
   System.string NewName
)
```

### JScript

```
function RenameEntry(
   OldName : System.String,
   NewName : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool RenameEntry(
   System.string* OldName,
   System.string* NewName
)
```

### C++/CLI

```cpp
System.bool RenameEntry(
   System.String^ OldName,
   System.String^ NewName
)
```

### Parameters

- `OldName`: Name of the entity to change
- `NewName`: Name to which to change OldName

### Return Value

True if OldName is changed to NewName, false if not

## See Also

[IDictionary Interface](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)
[IDictionary Members](Interop.dsAutomation~Interop.dsAutomation.IDictionary_members.html)
[IDictionary::GetEntries Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetEntries.html)
[IDictionary::GetEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetEntry.html)
[IDictionary::GetNameOf Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetNameOf.html)
[IDictionary::HasEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~HasEntry.html)
[IDictionary::RemoveEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~RemoveEntry.html)
[IDictionary::SetEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~SetEntry.html)

## Availability

DraftSight V1R4.0
