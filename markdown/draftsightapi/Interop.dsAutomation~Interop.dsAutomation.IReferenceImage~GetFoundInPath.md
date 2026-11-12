---
title: "GetFoundInPath Method (IReferenceImage)"
project: ""
interface: "IReferenceImage"
member: "GetFoundInPath"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~GetFoundInPath.html"
---

# GetFoundInPath Method (IReferenceImage)

Gets the path and file name where this Referenced image is copied.

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

Referenced image copy location

## Remarks

This method returns the **Found in path** that is displayed in the File information section of the Attach Reference: Image dialog that appears after you run the ATTACHIMAGE command in DraftSight.

## See Also

[IReferenceImage Interface](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage.html)
[IReferenceImage Members](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage_members.html)
[IReferenceImage::GetPath Method ()](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~GetPath.html)

## Availability

DraftSight 2019 SP0
