---
title: "ReleaseExtensionDictionary Method (IModelNamedView)"
project: ""
interface: "IModelNamedView"
member: "ReleaseExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~ReleaseExtensionDictionary.html"
---

# ReleaseExtensionDictionary Method (IModelNamedView)

Releases and erases the [dictionary](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html) for the model named view, if the dictionary exists and is empty.

## Syntax

### Visual Basic

```vb
Function ReleaseExtensionDictionary() As System.Boolean
```

### C#

```csharp
System.bool ReleaseExtensionDictionary()
```

### JScript

```
function ReleaseExtensionDictionary() : System.boolean;
```

### Managed Extensions for C++

```
System.bool ReleaseExtensionDictionary();
```

### C++/CLI

```cpp
System.bool ReleaseExtensionDictionary();
```

### Return Value

True if the dictionary is released and erased, false if not (see **Remarks**)

## Remarks

If the dictionary exists and is not empty, i.e., it contains one or more [XRecords](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html), then it is not released and erased. You must remove or erase all XRecords from the dictionary before you can release and erase the dictionary. See [IDictionary::RemoveEntry](Interop.dsAutomation~Interop.dsAutomation.IDictionary~RemoveEntry.html) and [IXRecord::Erased](Interop.dsAutomation~Interop.dsAutomation.IXRecord~Erased.html).

To restore a released and erased dictionary for this model named view, call [IModelNamedView::CreateExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~CreateExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html). If you close the drawing before restoring the released and erased dictionary, then that dictionary is deleted from the drawing and cannot be restored.

This method also returns true if the dictionary does not exist.

## See Also

[IModelNamedView Interface](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView.html)
[IModelNamedView Members](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView_members.html)
[IModelNamedView::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IModelNamedView~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
