---
title: "CreateExtensionDictionary Method (IEntityHelper)"
project: ""
interface: "IEntityHelper"
member: "CreateExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~CreateExtensionDictionary.html"
---

# CreateExtensionDictionary Method (IEntityHelper)

Creates a dictionary for the specified entity.

## Syntax

### Visual Basic

```vb
Function CreateExtensionDictionary( _
   ByVal Obj As System.Object _
) As Dictionary
```

### C#

```csharp
Dictionary CreateExtensionDictionary(
   System.object Obj
)
```

### JScript

```
function CreateExtensionDictionary(
   Obj : System.Object
) : Dictionary;
```

### Managed Extensions for C++

```
Dictionary* CreateExtensionDictionary(
   System.Object* Obj
)
```

### C++/CLI

```cpp
Dictionary^ CreateExtensionDictionary(
   System.Object^ Obj
)
```

### Parameters

- `Obj`: Entity

### Return Value

[Dictionary](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)

## Remarks

| If the dictionary... | Then the dictionary is... |
| --- | --- |
| Already exists for the entity | Not overwritten; instead, the existing dictionary is returned. |
| Was erased by either IEntityHelper::ReleaseExtensionDictionary or IDictionary::Erased | Restored. NOTE : If the drawing is closed with the dictionary erased, then the dictionary is deleted from the drawing and cannot be restored. |

## See Also

[IEntityHelper Interface](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper.html)
[IEntityHelper Members](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper_members.html)
[IEntityHelper::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~GetExtensionDictionary.html)

## Availability

DraftSight V1R5.0
