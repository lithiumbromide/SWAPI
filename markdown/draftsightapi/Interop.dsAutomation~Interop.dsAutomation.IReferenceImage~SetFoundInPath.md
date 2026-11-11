---
title: "SetFoundInPath Method (IReferenceImage)"
project: ""
interface: "IReferenceImage"
member: "SetFoundInPath"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~SetFoundInPath.html"
---

# SetFoundInPath Method (IReferenceImage)

Sets the path and file name where this Referenced image is copied.

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

- `FoundInPath`: Referenced image copy location

## Remarks

This method sets the **Found in path** that is displayed in the File information section of the Attach Reference: Image dialog that appears after you run the ATTACHIMAGE command in DraftSight.

## See Also

[IReferenceImage Interface](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage.html)
[IReferenceImage Members](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage_members.html)

## Availability

DraftSight 2020 SP1
