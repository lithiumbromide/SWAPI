---
title: "CreateDictionary Method (IDictionary)"
project: ""
interface: "IDictionary"
member: "CreateDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDictionary~CreateDictionary.html"
---

# CreateDictionary Method (IDictionary)

Creates the specified dictionary in the dictionary.

## Syntax

### Visual Basic

```vb
Function CreateDictionary( _
   ByVal Name As System.String _
) As Dictionary
```

### C#

```csharp
Dictionary CreateDictionary(
   System.string Name
)
```

### JScript

```
function CreateDictionary(
   Name : System.String
) : Dictionary;
```

### Managed Extensions for C++

```
Dictionary* CreateDictionary(
   System.string* Name
)
```

### C++/CLI

```cpp
Dictionary^ CreateDictionary(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of the dictionary to create in the dictionary

### Return Value

[Dictionary](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html) (see **Remarks**)

## Examples

[Create and Remove Dictionaries (C#)](Create_and_Remove_Dictionaries_Example_CSharp.htm)
[Create and Remove Dictionaries (VB.NET)](Create_and_Remove_Dictionaries_Example_VBNET.htm)
[Create and Remove Dictionaries (VBA)](Create_and_Remove_Dictionaries_Example_VBA.htm)

## Remarks

If the specified dictionary already exists in the dictionary, then it is not overwritten.

## See Also

[IDictionary Interface](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)
[IDictionary Members](Interop.dsAutomation~Interop.dsAutomation.IDictionary_members.html)
[IDictionary::Erased Property ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html)
[IDictionary::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~CreateExtensionDictionary.html)
[IDictionary::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
