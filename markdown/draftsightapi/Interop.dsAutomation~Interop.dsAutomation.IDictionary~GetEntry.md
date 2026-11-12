---
title: "GetEntry Method (IDictionary)"
project: ""
interface: "IDictionary"
member: "GetEntry"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetEntry.html"
---

# GetEntry Method (IDictionary)

Gets the specified entity and its entity type in the dictionary.

## Syntax

### Visual Basic

```vb
Function GetEntry( _
   ByVal Name As System.String, _
   ByRef ObjType As dsObjectType_e _
) As System.Object
```

### C#

```csharp
System.object GetEntry(
   System.string Name,
   out dsObjectType_e ObjType
)
```

### JScript

```
function GetEntry(
   Name : System.String,
   ObjType : dsObjectType_e
) : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetEntry(
   System.string* Name,
   [PARAMFLAG::Out] dsObjectType_e ObjType
)
```

### C++/CLI

```cpp
System.Object^ GetEntry(
   System.String^ Name,
   [Out] dsObjectType_e ObjType
)
```

### Parameters

- `Name`: Name of entity to get
- `ObjType`: Type of entity as defined in [dsObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsObjectType_e.html)

### Return Value

Entity (see **Remarks**)

## Examples

[Create and Remove Dictionaries (C#)](Create_and_Remove_Dictionaries_Example_CSharp.htm)
[Create and Remove Dictionaries (VB.NET)](Create_and_Remove_Dictionaries_Example_VBNET.htm)
[Create and Remove Dictionaries (VBA)](Create_and_Remove_Dictionaries_Example_VBA.htm)

## Remarks

If the entity is not supported, null or Nothing might be returned.

## See Also

[IDictionary Interface](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)
[IDictionary Members](Interop.dsAutomation~Interop.dsAutomation.IDictionary_members.html)
[IDictionary::GetEntries Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetEntries.html)
[IDictionary::GetNameOf Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetNameOf.html)
[IDictionary::HasEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~HasEntry.html)
[IDictionary::RemoveEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~RemoveEntry.html)
[IDictionary::RenameEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~RenameEntry.html)
[IDictionary::SetEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~SetEntry.html)

## Availability

DraftSight V1R4.0
