---
title: "GetExtensionDictionary Method (ITable)"
project: ""
interface: "ITable"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (ITable)

Gets the dictionary for the Table.

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

If the dictionary does not exist or it was erased by either [ITable::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.ITable~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
