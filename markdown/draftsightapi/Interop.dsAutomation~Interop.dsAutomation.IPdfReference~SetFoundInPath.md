---
title: "SetFoundInPath Method (IPdfReference)"
project: ""
interface: "IPdfReference"
member: "SetFoundInPath"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPdfReference~SetFoundInPath.html"
---

# SetFoundInPath Method (IPdfReference)

Sets the found in path for this PDF reference.

## Syntax

### Visual Basic

```vb
Sub SetFoundInPath( _
   ByVal FoundInPath As System.String _
)
```

### C#

```csharp
void SetFoundInPath(
   System.string FoundInPath
)
```

### JScript

```
function SetFoundInPath(
   FoundInPath : System.String
);
```

### Managed Extensions for C++

```
void SetFoundInPath(
   System.string* FoundInPath
)
```

### C++/CLI

```cpp
void SetFoundInPath(
   System.String^ FoundInPath
)
```

### Parameters

- `FoundInPath`: Found in path

## Remarks

This method sets the **Found in path** that is displayed in the File information section of the Attach Reference: PDF Underlay dialog that appears after you run the ATTACHPDF command in DraftSight.

## See Also

[IPdfReference Interface](Interop.dsAutomation~Interop.dsAutomation.IPdfReference.html)
[IPdfReference Members](Interop.dsAutomation~Interop.dsAutomation.IPdfReference_members.html)

## Availability

DraftSight 2020 SP1
