---
title: "ReleaseExtensionDictionary Method (IExtrudedSurface)"
project: ""
interface: "IExtrudedSurface"
member: "ReleaseExtensionDictionary"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExtrudedSurface~ReleaseExtensionDictionary.html"
---

# ReleaseExtensionDictionary Method (IExtrudedSurface)

Releases and erases the [dictionary](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html), if it exists and is empty, for this extruded surface.

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

## Remarks

If the dictionary exists and is not empty, i.e., it contains one or more [XRecords](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html), then it is not released and erased. You must remove or erase all XRecords from the dictionary before you can release and erase the dictionary. See [IDictionary::RemoveEntry](Interop.dsAutomation~Interop.dsAutomation.IDictionary~RemoveEntry.html) and [IXRecord::Erased](Interop.dsAutomation~Interop.dsAutomation.IXRecord~Erased.html).

To restore a released and erased dictionary for this extruded surface, call [IExtrudedSurface::CreateExtensionDictionary](Interop.dsAutomation~Interop.dsAutomation.IExtrudedSurface~CreateExtensionDictionary.html) or [IDictionary::Erased](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html). If you close the drawing before restoring the released and erased dictionary, then that dictionary is deleted from the drawing and cannot be restored.

This method also returns true if the dictionary does not exist.

## See Also

[IExtrudedSurface Interface](Interop.dsAutomation~Interop.dsAutomation.IExtrudedSurface.html)
[IExtrudedSurface Members](Interop.dsAutomation~Interop.dsAutomation.IExtrudedSurface_members.html)
[IExtrudedSurface::GetExtensionDictionary Method ()](Interop.dsAutomation~Interop.dsAutomation.IExtrudedSurface~GetExtensionDictionary.html)

## Availability

DraftSight 2020 SP0
