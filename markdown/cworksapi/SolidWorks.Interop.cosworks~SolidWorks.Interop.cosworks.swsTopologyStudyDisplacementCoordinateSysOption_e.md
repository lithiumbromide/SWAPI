---
title: "swsTopologyStudyDisplacementCoordinateSysOption_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsTopologyStudyDisplacementCoordinateSysOption_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyDisplacementCoordinateSysOption_e.html"
---

# swsTopologyStudyDisplacementCoordinateSysOption_e Enumeration

Coordinate system options for topology study constraints

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsTopologyStudyDisplacementCoordinateSysOption_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsTopologyStudyDisplacementCoordinateSysOption_e
```

### C#

```csharp
public enum swsTopologyStudyDisplacementCoordinateSysOption_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsTopologyStudyDisplacementCoordinateSysOption_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsTopologyDisplacementCoordinateSysOption_Global | 0 = Use the global coordinate system |
| swsTopologyDisplacementCoordinateSysOption_UserDefine | 1 = Select a coordinate system |

## Remarks

These options are valid for all displacement components as defined in [swsTopologyStudyDisplacementComponentType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyDisplacementComponentType_e.html) except swsTopologyDisplacementCompType_URES (URES::Resultant displacement (Absolute)).

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
