---
title: "swsProbePostResultNodeElementSelectionWarning_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsProbePostResultNodeElementSelectionWarning_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsProbePostResultNodeElementSelectionWarning_e.html"
---

# swsProbePostResultNodeElementSelectionWarning_e Enumeration

Results probe selection warnings. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsProbePostResultNodeElementSelectionWarning_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsProbePostResultNodeElementSelectionWarning_e
```

### C#

```csharp
public enum swsProbePostResultNodeElementSelectionWarning_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsProbePostResultNodeElementSelectionWarning_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsProbePostResultNodeElemSelectionWarning_FewElemsLieOnBeamGaps | 0x1 = Elements lie on beam gaps |
| swsProbePostResultNodeElemSelectionWarning_FewNodeElemsLieOnNonRenderedBody | 0x8 = Nodes or elements are on a non-rendered body |
| swsProbePostResultNodeElemSelectionWarning_FewNodeElemsNotOnSectionPlane | 0x2 = Nodes or elements are not on the section plane |
| swsProbePostResultNodeElemSelectionWarning_FewNodeElemsOutOfRange | 0x4 = Nodes or elements are out of range for the given model |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
