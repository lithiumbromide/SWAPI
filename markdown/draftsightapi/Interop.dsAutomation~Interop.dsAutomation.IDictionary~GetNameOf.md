---
title: "GetNameOf Method (IDictionary)"
project: ""
interface: "IDictionary"
member: "GetNameOf"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetNameOf.html"
---

# GetNameOf Method (IDictionary)

Gets the name of the specified entity in the dictionary.

## Syntax

### Visual Basic

```vb
Function GetNameOf( _
   ByVal Entity As System.Object _
) As System.String
```

### C#

```csharp
System.string GetNameOf(
   System.object Entity
)
```

### JScript

```
function GetNameOf(
   Entity : System.Object
) : System.String;
```

### Managed Extensions for C++

```
System.string* GetNameOf(
   System.Object* Entity
)
```

### C++/CLI

```cpp
System.String^ GetNameOf(
   System.Object^ Entity
)
```

### Parameters

- `Entity`: Entity whose name to get in the dictionary

### Return Value

Name of the specified entity (see **Remarks**)

## Examples

[Create and Remove Dictionaries (C#)](Create_and_Remove_Dictionaries_Example_CSharp.htm)
[Create and Remove Dictionaries (VB.NET)](Create_and_Remove_Dictionaries_Example_VBNET.htm)
[Create and Remove Dictionaries (VBA)](Create_and_Remove_Dictionaries_Example_VBA.htm)

## Remarks

If an empty string is returned, then the specified entity is not in the dictionary.

## See Also

[IDictionary Interface](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)
[IDictionary Members](Interop.dsAutomation~Interop.dsAutomation.IDictionary_members.html)
[IDictionary::GetEntries Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetEntries.html)
[IDictionary::GetEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetEntry.html)
[IDictionary::HasEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~HasEntry.html)
[IDictionary::RemoveEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~RemoveEntry.html)
[IDictionary::RenameEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~RenameEntry.html)
[IDictionary::SetEntry Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~SetEntry.html)

## Availability

DraftSight V1R4.0
