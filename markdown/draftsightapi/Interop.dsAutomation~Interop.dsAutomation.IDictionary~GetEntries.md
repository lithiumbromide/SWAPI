---
title: "GetEntries Method (IDictionary)"
project: ""
interface: "IDictionary"
member: "GetEntries"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetEntries.html"
---

# GetEntries Method (IDictionary)

Gets the entities and their entity types in the dictionary.

## Syntax

### Visual Basic

```vb
Function GetEntries( _
   ByRef EntityTypeLongArray As System.Object _
) As System.Object
```

### C#

```csharp
System.object GetEntries(
   out System.object EntityTypeLongArray
)
```

### JScript

```
function GetEntries(
   EntityTypeLongArray : System.Object
) : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetEntries(
   [PARAMFLAG::Out] System.Object* EntityTypeLongArray
)
```

### C++/CLI

```cpp
System.Object^ GetEntries(
   [Out] System.Object^ EntityTypeLongArray
)
```

### Parameters

- `EntityTypeLongArray`: Array of entity types as defined in [dsObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsObjectType_e.html)

### Return Value

Array of entities

## Examples

[Create and Remove Dictionaries (C#)](Create_and_Remove_Dictionaries_Example_CSharp.htm)
[Create and Remove Dictionaries (VB.NET)](Create_and_Remove_Dictionaries_Example_VBNET.htm)
[Create and Remove Dictionaries (VBA)](Create_and_Remove_Dictionaries_Example_VBA.htm)

## See Also

[IDictionary Interface](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)
[IDictionary Members](Interop.dsAutomation~Interop.dsAutomation.IDictionary_members.html)
[IDictionary::GetEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetEntry.html)
[IDictionary::GetNameOf Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetNameOf.html)
[IDictionary::HasEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~HasEntry.html)
[IDictionary::RemoveEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~RemoveEntry.html)
[IDictionary::RenameEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~RenameEntry.html)
[IDictionary::SetEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~SetEntry.html)

## Availability

DraftSight V1R4.0
