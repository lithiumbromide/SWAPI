---
title: "GetPath Method (IReferenceImage)"
project: ""
interface: "IReferenceImage"
member: "GetPath"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~GetPath.html"
---

# GetPath Method (IReferenceImage)

Gets the original path and file name of the Referenced image.

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

Path and file name of the saved Referenced image

## Remarks

This method returns the **Saved path** that is displayed in the File information section of the Attach Reference: Image dialog that appears after you run the ATTACHIMAGE command in DraftSight.

## See Also

[IReferenceImage Interface](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage.html)
[IReferenceImage Members](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage_members.html)
[IReferenceImage::SetPath Method](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~SetPath.html)
[IReferenceImage::GetFoundInPath Method ()](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~GetFoundInPath.html)

## Availability

DraftSight V1R1.4
