---
title: "ReleaseExtensionDictionary Method (IDictionary)"
project: ""
interface: "IDictionary"
member: "ReleaseExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDictionary~ReleaseExtensionDictionary.html"
---

# ReleaseExtensionDictionary Method (IDictionary)

Releases and erases the [extension dictionary](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html) of the dictionary, if the extension dictionary exists and is empty.

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

True if the extension dictionary is released and erased, false if not (see **Remarks**)

## Remarks

If the extension dictionary exists and is not empty, i.e., it contains one or more [XRecords](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html), then it is not released and erased. You must either remove or erase all XRecords from the extension dictionary before you can release and erase the extension dictionary from the dictionary. See [IDictionary::RemoveEntry](Interop.dsAutomation~Interop.dsAutomation.IDictionary~RemoveEntry.html) and [IXRecord::Erased](Interop.dsAutomation~Interop.dsAutomation.IXRecord~Erased.html).

To restore the released and erased extension dictionary to this dictionary, call either [IDictionary::CreateExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IDictionary~CreateExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html) before closing the drawing. If you close the drawing before restoring the released and erased extension dictionary, then that extension dictionary is deleted from the drawing and cannot be restored.

This method also returns true if the extension dictionary does not exist.

## See Also

[IDictionary Interface](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)
[IDictionary Members](Interop.dsAutomation~Interop.dsAutomation.IDictionary_members.html)
[IDictionary::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
