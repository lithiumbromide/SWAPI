---
title: "GetPath Method (IPdfReference)"
project: ""
interface: "IPdfReference"
member: "GetPath"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPdfReference~GetPath.html"
---

# GetPath Method (IPdfReference)

Gets the saved path of this PDF reference.

## Syntax

### Visual Basic

```vb
Function GetPath() As System.String
```

### C#

```csharp
System.string GetPath()
```

### JScript

```
function GetPath() : System.String;
```

### Managed Extensions for C++

```
System.string* GetPath();
```

### C++/CLI

```cpp
System.String^ GetPath();
```

### Return Value

Saved path

## Remarks

This method returns the **Saved path** that is displayed in the File information section of the Attach Reference: PDF Underlay dialog that appears after you run the ATTACHPDF command in DraftSight.

## See Also

[IPdfReference Interface](Interop.dsAutomation~Interop.dsAutomation.IPdfReference.html)
[IPdfReference Members](Interop.dsAutomation~Interop.dsAutomation.IPdfReference_members.html)
[IPdfReference::GetFoundInPath Method ()](Interop.dsAutomation~Interop.dsAutomation.IPdfReference~GetFoundInPath.html)
[IPdfReference::SetPath Method ()](Interop.dsAutomation~Interop.dsAutomation.IPdfReference~SetPath.html)

## Availability

DraftSight 2020 SP0
