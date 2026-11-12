---
title: "GetExtensionDictionary Method (ISheetNamedView)"
project: ""
interface: "ISheetNamedView"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISheetNamedView~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (ISheetNamedView)

Gets the dictionary for the sheet named view.

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

If the dictionary does not exist or it was erased by either [ISheetNamedView::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.ISheetNamedView~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[ISheetNamedView Interface](Interop.dsAutomation~Interop.dsAutomation.ISheetNamedView.html)
[ISheetNamedView Members](Interop.dsAutomation~Interop.dsAutomation.ISheetNamedView_members.html)
[ISheetNamedView::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ISheetNamedView~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
