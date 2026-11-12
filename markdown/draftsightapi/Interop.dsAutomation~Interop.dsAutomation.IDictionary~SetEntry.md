---
title: "SetEntry Method (IDictionary)"
project: ""
interface: "IDictionary"
member: "SetEntry"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDictionary~SetEntry.html"
---

# SetEntry Method (IDictionary)

Sets the name for the specified entity in the dictionary.

## Syntax

### Visual Basic

```vb
Sub SetEntry( _
   ByVal Name As System.String, _
   ByVal Obj As System.Object _
)
```

### C#

```csharp
void SetEntry(
   System.string Name,
   System.object Obj
)
```

### JScript

```
function SetEntry(
   Name : System.String,
   Obj : System.Object
);
```

### Managed Extensions for C++

```
void SetEntry(
   System.string* Name,
   System.Object* Obj
)
```

### C++/CLI

```cpp
void SetEntry(
   System.String^ Name,
   System.Object^ Obj
)
```

### Parameters

- `Name`: Name for Obj
- `Obj`: Entity

## Remarks

| If the specified name... | Then... |
| --- | --- |
| Exists | The existing name and entity association is replaced with the name and entity association specified in this method. |
| Does not exist | The specified name and entity association is created. |

## See Also

[IDictionary Interface](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)
[IDictionary Members](Interop.dsAutomation~Interop.dsAutomation.IDictionary_members.html)
[IDictionary::GetEntries Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetEntries.html)
[IDictionary::GetEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetEntry.html)
[IDictionary::GetNameOf Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetNameOf.html)
[IDictionary::HasEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~HasEntry.html)
[IDictionary::RemoveEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~RemoveEntry.html)
[IDictionary::RenameEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~RenameEntry.html)

## Availability

DraftSight V1R4.0
