---
title: "SwDmAnnotationFileOpenError Enumeration"
project: "SOLIDWORKS Document Manager API Help"
interface: "SwDmAnnotationFileOpenError"
member: ""
kind: "enum"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmAnnotationFileOpenError.html"
---

# SwDmAnnotationFileOpenError Enumeration

Result codes when opening the preview bitmap of an annotation file.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum SwDmAnnotationFileOpenError
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As SwDmAnnotationFileOpenError
```

### C#

```csharp
public enum SwDmAnnotationFileOpenError : System.Enum
```

### C++/CLI

```cpp
public enum class SwDmAnnotationFileOpenError : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDmAnnotationFileOpenErrorFail | 1 |
| swDmAnnotationFileOpenErrorFileNotFound | 2 |
| swDmAnnotationFileOpenErrorNonAnnotationFile | 3 |
| swDmAnnotationFileOpenErrorNone | 0 |

## See Also

[SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.html)
