---
title: "GetExtensionDictionary Method (IModel)"
project: ""
interface: "IModel"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IModel~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IModel)

Gets the dictionary for the model.

## Syntax

### Visual Basic

```vb
Function GetExtensionDictionary() As Dictionary
```

### C#

```csharp
Dictionary GetExtensionDictionary()
```

### JScript

```
function GetExtensionDictionary() : Dictionary;
```

### Managed Extensions for C++

```
Dictionary* GetExtensionDictionary();
```

### C++/CLI

```cpp
Dictionary^ GetExtensionDictionary();
```

### Return Value

[Dictionary](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)

## Remarks

If the dictionary does not exist or it was erased by either [IModel::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IModel~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IModel Interface](Interop.dsAutomation~Interop.dsAutomation.IModel.html)
[IModel Members](Interop.dsAutomation~Interop.dsAutomation.IModel_members.html)
[IModel::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IModel~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
