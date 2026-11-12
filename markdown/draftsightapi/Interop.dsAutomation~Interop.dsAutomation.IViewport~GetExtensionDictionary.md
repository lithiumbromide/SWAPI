---
title: "GetExtensionDictionary Method (IViewport)"
project: ""
interface: "IViewport"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewport~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IViewport)

Gets the dictionary for the Viewport.

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

If the dictionary does not exist or it was erased by either [IViewport::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IViewport~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IViewport Interface](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)
[IViewport Members](Interop.dsAutomation~Interop.dsAutomation.IViewport_members.html)
[IViewport::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IViewport~CreateExtensionDictionary.html)

## Availability

DraftSight V1R4.0
