---
title: "GetExtensionDictionary Method (IEntityHelper)"
project: ""
interface: "IEntityHelper"
member: "GetExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~GetExtensionDictionary.html"
---

# GetExtensionDictionary Method (IEntityHelper)

Gets the dictionary for the specified entity.

## Syntax

### Visual Basic

```vb
Function GetExtensionDictionary( _
   ByVal Obj As System.Object _
) As Dictionary
```

### C#

```csharp
Dictionary GetExtensionDictionary(
   System.object Obj
)
```

### JScript

```
function GetExtensionDictionary(
   Obj : System.Object
) : Dictionary;
```

### Managed Extensions for C++

```
Dictionary* GetExtensionDictionary(
   System.Object* Obj
)
```

### C++/CLI

```cpp
Dictionary^ GetExtensionDictionary(
   System.Object^ Obj
)
```

### Parameters

- `Obj`: Entity for which to get its dictionary

### Return Value

[Dictionary](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)

## Remarks

If the dictionary does not exist or it was erased by either [IEntityHelper::ReleaseExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~ReleaseExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html), then null or Nothing is returned.

## See Also

[IEntityHelper Interface](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper.html)
[IEntityHelper Members](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper_members.html)
[IEntityHelper::CreateExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~CreateExtensionDictionary.html)

## Availability

DraftSight V1R5.0
