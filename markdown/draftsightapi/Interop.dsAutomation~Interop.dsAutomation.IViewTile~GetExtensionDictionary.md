---
title: "GetExtensionDictionary Method (IViewTile)"
project: ""
interface: "IViewTile"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewTile~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IViewTile)

Gets the dictionary for this ViewTile.

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

If the dictionary does not exist or it was erased by either [IViewTile::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IViewTile~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IViewTile Interface](Interop.dsAutomation~Interop.dsAutomation.IViewTile.html)
[IViewTile Members](Interop.dsAutomation~Interop.dsAutomation.IViewTile_members.html)
[IViewTile::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IViewTile~CreateExtensionDictionary.html)

## Availability

DraftSight V1R6.0
