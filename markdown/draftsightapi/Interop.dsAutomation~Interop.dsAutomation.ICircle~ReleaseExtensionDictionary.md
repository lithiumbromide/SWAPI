---
title: "ReleaseExtensionDictionary Method (ICircle)"
project: ""
interface: "ICircle"
member: "ReleaseExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICircle~ReleaseExtensionDictionary.html"
---

# ReleaseExtensionDictionary Method (ICircle)

Releases and erases the [dictionary](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html) for the Circle, if the dictionary exists and is empty.

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

## Examples

[Create and Remove Dictionaries (C#)](Create_and_Remove_Dictionaries_Example_CSharp.htm)
[Create and Remove Dictionaries (VB.NET)](Create_and_Remove_Dictionaries_Example_VBNET.htm)
[Create and Remove Dictionaries (VBA)](Create_and_Remove_Dictionaries_Example_VBA.htm)
[Create and Remove Dictionary (JavaScript)](Create_and_Remove_Dictionary_Example_JS.htm)

## Remarks

If the dictionary exists and is not empty, i.e., it contains one or more [XRecords](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html), then it is not released and erased. You must remove or erase all XRecords from the dictionary before you can release and erase the dictionary. See [IDictionary::RemoveEntry](Interop.dsAutomation~Interop.dsAutomation.IDictionary~RemoveEntry.html) and [IXRecord::Erased](Interop.dsAutomation~Interop.dsAutomation.IXRecord~Erased.html).

To restore a released and erased dictionary for this Circle, call [ICircle::CreateExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.ICircle~CreateExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html). If you close the drawing before restoring the released and erased dictionary, then that dictionary is deleted from the drawing and cannot be restored.

This method also returns true if the dictionary does not exist.

## See Also

[ICircle Interface](Interop.dsAutomation~Interop.dsAutomation.ICircle.html)
[ICircle Members](Interop.dsAutomation~Interop.dsAutomation.ICircle_members.html)
[ICircle::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.ICircle~GetExtensionDictionary.html)

## Availability

DraftSight V1R4.0
