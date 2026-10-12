---
title: "fwAutomaticRecognitionOptions_e Enumeration"
project: "FeatureWorks API Help"
interface: "fwAutomaticRecognitionOptions_e"
member: ""
kind: "enum"
source: "fworksapi/SolidWorks.Interop.fworks~SolidWorks.Interop.fworks.fwAutomaticRecognitionOptions_e.html"
---

# fwAutomaticRecognitionOptions_e Enumeration

Automatic recognition options. [Bitmask](sldworksapiprogguide.chm::/overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum fwAutomaticRecognitionOptions_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As fwAutomaticRecognitionOptions_e
```

### C#

```csharp
public enum fwAutomaticRecognitionOptions_e : System.Enum
```

### C++/CLI

```cpp
public enum class fwAutomaticRecognitionOptions_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| fwAutoEdgeFlange | 0x100 = Recognize edge flange features automatically |
| fwAutoHemFlange | 0x200 = Recognize hem features automatically |
| fwBaseFlange | 0x40 = Recognize base flange features automatically |
| fwChamfils | 0x10 = Recognize fillets and chamfers automatically |
| fwExtrudeOption | 0x1 = Recognize extrude features automatically |
| fwHoles | 0x8 = Recognize hole features automatically |
| fwRevolve | 0x4 = Recognize revolve features automatically |
| fwRibs | 0x20 = Recognize rib features automatically |
| fwSketchedBend | 0x80 = Recognize sketched bend features automatically |
| fwVolume | 0x2 = Recognize volume features automatically |

## See Also

[SolidWorks.Interop.fworks Namespace](SolidWorks.Interop.fworks~SolidWorks.Interop.fworks_namespace.html)
