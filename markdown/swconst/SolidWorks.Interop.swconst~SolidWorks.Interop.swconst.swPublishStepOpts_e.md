---
title: "swPublishStepOpts_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swPublishStepOpts_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPublishStepOpts_e.html"
---

# swPublishStepOpts_e Enumeration

Options for publishing to Step 242.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swPublishStepOpts_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swPublishStepOpts_e
```

### C#

```csharp
public enum swPublishStepOpts_e : System.Enum
```

### C++/CLI

```cpp
public enum class swPublishStepOpts_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swPublishStepOpts_FaceEdgeSTEP242 | 2 = Export face/edge properties/IDs |
| swPublishStepOpts_None | 0 |
| swPublishStepOpts_SplitFacesSTEP242 | 1 = Split features with 360 degree faces (holes, cylinders, cones) into two |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
