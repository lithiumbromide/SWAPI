---
title: "HasEntry Method (IDictionary)"
project: ""
interface: "IDictionary"
member: "HasEntry"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDictionary~HasEntry.html"
---

# HasEntry Method (IDictionary)

Gets whether the dictionary contains an entity with the specified name.

## Syntax

### Visual Basic

```vb
Function HasEntry( _
   ByVal Name As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool HasEntry(
   System.string Name
)
```

### JScript

```
function HasEntry(
   Name : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool HasEntry(
   System.string* Name
)
```

### C++/CLI

```cpp
System.bool HasEntry(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of specified entity

### Return Value

True if the dictionary contains an entity with the specified name, false if not

## Examples

[Create and Remove Dictionaries (C#)](Create_and_Remove_Dictionaries_Example_CSharp.htm)
[Create and Remove Dictionaries (VB.NET)](Create_and_Remove_Dictionaries_Example_VBNET.htm)
[Create and Remove Dictionaries (VBA)](Create_and_Remove_Dictionaries_Example_VBA.htm)

## See Also

[IDictionary Interface](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)
[IDictionary Members](Interop.dsAutomation~Interop.dsAutomation.IDictionary_members.html)
[IDictionary::GetEntries Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetEntries.html)
[IDictionary::GetEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetEntry.html)
[IDictionary::GetNameOf Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetNameOf.html)
[IDictionary::RemoveEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~RemoveEntry.html)
[IDictionary::RenameEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~RenameEntry.html)
[IDictionary::SetEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~SetEntry.html)

## Availability

DraftSight V1R4.0
