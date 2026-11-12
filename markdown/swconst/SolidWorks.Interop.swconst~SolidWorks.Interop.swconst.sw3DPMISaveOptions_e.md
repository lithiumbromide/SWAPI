---
title: "sw3DPMISaveOptions_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "sw3DPMISaveOptions_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.sw3DPMISaveOptions_e.html"
---

# sw3DPMISaveOptions_e Enumeration

3D PMI (Product and Manufacturing Information) save options when comparing two different versions of the same model. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum sw3DPMISaveOptions_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As sw3DPMISaveOptions_e
```

### C#

```csharp
public enum sw3DPMISaveOptions_e : System.Enum
```

### C++/CLI

```cpp
public enum class sw3DPMISaveOptions_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAddReportToDesignBinder | 1 or 0x1 |
| swDimXpertData | 4 or 0x4 |
| swReferenceData | 8 or 0x8 |
| swViewReportOnSave | 2 or 0x2 |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
