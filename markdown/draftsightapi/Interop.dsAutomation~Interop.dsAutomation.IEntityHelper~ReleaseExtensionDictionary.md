---
title: "ReleaseExtensionDictionary Method (IEntityHelper)"
project: ""
interface: "IEntityHelper"
member: "ReleaseExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~ReleaseExtensionDictionary.html"
---

# ReleaseExtensionDictionary Method (IEntityHelper)

Releases and erases the dictionary, if the dictionary exists and is empty, for the specified entity.

## Syntax

### Visual Basic

```vb
Function ReleaseExtensionDictionary( _
   ByVal Obj As System.Object _
) As System.Boolean
```

### C#

```csharp
System.bool ReleaseExtensionDictionary(
   System.object Obj
)
```

### JScript

```
function ReleaseExtensionDictionary(
   Obj : System.Object
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool ReleaseExtensionDictionary(
   System.Object* Obj
)
```

### C++/CLI

```cpp
System.bool ReleaseExtensionDictionary(
   System.Object^ Obj
)
```

### Parameters

- `Obj`: Entity for which to delete the dictionary

### Return Value

True if the dictionary is release and erased, false if not (see **Remarks**)

## Remarks

If the dictionary exists and is not empty, i.e., it contains one or more [XRecords](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html), then it is not released and erased. You must remove or erase all XRecords from the dictionary before you can release and erase the dictionary. See [IDictionary::RemoveEntry](Interop.dsAutomation~Interop.dsAutomation.IDictionary~RemoveEntry.html) and [IXRecord::Erased](Interop.dsAutomation~Interop.dsAutomation.IXRecord~Erased.html).

To restore a released and erased dictionary for the specified entity, call [IEntityHelper::CreateExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~CreateExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html). If you close the drawing before restoring the released and erased dictionary, then that dictionary is deleted from the drawing and cannot be restored.

This method also returns true if the dictionary does not exist.

## See Also

[IEntityHelper Interface](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper.html)
[IEntityHelper Members](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper_members.html)
[IEntityHelper::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~GetExtensionDictionary.html)

## Availability

DraftSight V1R5.0
