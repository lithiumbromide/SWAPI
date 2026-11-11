---
title: "GetFoundInPath Method (IPdfReference)"
project: ""
interface: "IPdfReference"
member: "GetFoundInPath"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPdfReference~GetFoundInPath.html"
---

# GetFoundInPath Method (IPdfReference)

Gets the found in path for this PDF reference.

## Syntax

### Visual Basic

```vb
Function GetFoundInPath() As System.String
```

### C#

```csharp
System.string GetFoundInPath()
```

### JScript

```
function GetFoundInPath() : System.String;
```

### Managed Extensions for C++

```
System.string* GetFoundInPath();
```

### C++/CLI

```cpp
System.String^ GetFoundInPath();
```

### Return Value

Found in path

## Remarks

This method returns the **Found in path** that is displayed in the File information section of the Attach Reference: PDF Underlay dialog that appears after you run the ATTACHPDF command in DraftSight.

## See Also

[IPdfReference Interface](Interop.dsAutomation~Interop.dsAutomation.IPdfReference.html)
[IPdfReference Members](Interop.dsAutomation~Interop.dsAutomation.IPdfReference_members.html)
[IPdfReference::GetPath Method ()](Interop.dsAutomation~Interop.dsAutomation.IPdfReference~GetPath.html)

## Availability

DraftSight 2020 SP0
