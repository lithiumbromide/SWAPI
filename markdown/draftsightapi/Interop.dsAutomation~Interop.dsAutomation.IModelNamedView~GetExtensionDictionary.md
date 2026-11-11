---
title: "GetExtensionDictionary Method (IModelNamedView)"
project: ""
interface: "IModelNamedView"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IModelNamedView)

Gets the dictionary for the model named view.

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

If the dictionary does not exist or it was erased by either [IModelNamedView::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IModelNamedView Interface](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView.html)
[IModelNamedView Members](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView_members.html)
[IModelNamedView::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
