---
title: "CreateExtensionDictionary Method (ICircle)"
project: ""
interface: "ICircle"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICircle~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (ICircle)

Creates a dictionary for the Circle.

## Syntax

### Visual Basic

```vb
Function CreateExtensionDictionary() As Dictionary
```

### C#

```csharp
Dictionary CreateExtensionDictionary()
```

### JScript

```
function CreateExtensionDictionary() : Dictionary;
```

### Managed Extensions for C++

```
Dictionary* CreateExtensionDictionary();
```

### C++/CLI

```cpp
Dictionary^ CreateExtensionDictionary();
```

### Return Value

[Dictionary](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)

## Examples

[Create and Remove Dictionaries (C#)](Create_and_Remove_Dictionaries_Example_CSharp.htm)
[Create and Remove Dictionaries (VB.NET)](Create_and_Remove_Dictionaries_Example_VBNET.htm)
[Create and Remove Dictionaries (VBA)](Create_and_Remove_Dictionaries_Example_VBA.htm)
[Create and Remove Dictionary (JavaScript)](Create_and_Remove_Dictionary_Example_JS.htm)

## Remarks

| If the dictionary... | Then the dictionary is... |
| --- | --- |
| Already exists for the Circle | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either ICircle::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[ICircle Interface](Interop.dsAutomation~Interop.dsAutomation.ICircle.html)
[ICircle Members](Interop.dsAutomation~Interop.dsAutomation.ICircle_members.html)
[ICircle::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ICircle~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
