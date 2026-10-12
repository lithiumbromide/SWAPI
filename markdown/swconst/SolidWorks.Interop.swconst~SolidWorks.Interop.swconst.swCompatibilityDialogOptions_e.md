---
title: "swCompatibilityDialogOptions_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swCompatibilityDialogOptions_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCompatibilityDialogOptions_e.html"
---

# swCompatibilityDialogOptions_e Enumeration

Options for displaying the previous file format version compatibility check results dialog.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCompatibilityDialogOptions_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swCompatibilityDialogOptions_e
```

### C#

```csharp
public enum swCompatibilityDialogOptions_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCompatibilityDialogOptions_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swCompatibilityDialogOptions_AlwaysShow | 0 = Always show the dialog regardless of the outcome of the compatibility check. |
| swCompatibilityDialogOptions_NeverShow | 2 = Never show the dialog regardless of the outcome of the compatibility check. |
| swCompatibilityDialogOptions_ShowOnIncompatible | 1 = Only show the dialog when incompatibilities are found. |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
