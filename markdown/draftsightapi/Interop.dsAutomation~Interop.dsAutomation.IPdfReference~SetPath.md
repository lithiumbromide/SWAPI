---
title: "SetPath Method (IPdfReference)"
project: ""
interface: "IPdfReference"
member: "SetPath"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPdfReference~SetPath.html"
---

# SetPath Method (IPdfReference)

Sets the saved path of this PDF reference.

## Syntax

### Visual Basic

```vb
Sub SetPath( _
   ByVal PdfPath As System.String _
)
```

### C#

```csharp
void SetPath(
   System.string PdfPath
)
```

### JScript

```
function SetPath(
   PdfPath : System.String
);
```

### Managed Extensions for C++

```
void SetPath(
   System.string* PdfPath
)
```

### C++/CLI

```cpp
void SetPath(
   System.String^ PdfPath
)
```

### Parameters

- `PdfPath`: Saved path

## Remarks

This method sets the **Saved path** that is displayed in the File information section of the Attach Reference: PDF Underlay dialog that appears after you run the ATTACHPDF command in DraftSight.

## See Also

[IPdfReference Interface](Interop.dsAutomation~Interop.dsAutomation.IPdfReference.html)
[IPdfReference Members](Interop.dsAutomation~Interop.dsAutomation.IPdfReference_members.html)
[IPdfReference::GetPath Method ()](Interop.dsAutomation~Interop.dsAutomation.IPdfReference~GetPath.html)

## Availability

DraftSight 2020 SP0
