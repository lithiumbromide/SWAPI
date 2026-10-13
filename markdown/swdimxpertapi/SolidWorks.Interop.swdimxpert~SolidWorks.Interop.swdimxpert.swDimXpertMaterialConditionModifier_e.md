---
title: "swDimXpertMaterialConditionModifier_e Enumeration"
project: "SOLIDWORKS DimXpert API Help"
interface: "swDimXpertMaterialConditionModifier_e"
member: ""
kind: "enum"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.swDimXpertMaterialConditionModifier_e.html"
---

# swDimXpertMaterialConditionModifier_e Enumeration

DimXpert material condition modifiers.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swDimXpertMaterialConditionModifier_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swDimXpertMaterialConditionModifier_e
```

### C#

```csharp
public enum swDimXpertMaterialConditionModifier_e : System.Enum
```

### C++/CLI

```cpp
public enum class swDimXpertMaterialConditionModifier_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDimXpertMaterialConditionModifier_unknown | 0 |
| swDimXpertMCM_LMC | 1 = Least material condition |
| swDimXpertMCM_MMC | 2 = Maximum material condition |
| swDimXpertMCM_NoMCM | 3 = No material condition modifier |
| swDimXpertMCM_RFS | 4 = Regardless of feature size |

## Remarks

The material condition modifiers of this enumeration can be applied to the tolerance or datums of a [geometric tolerance](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertTolerance.html) to set the least, maximum, and RFS material conditions for a feature. MMC, LMC, and RFS can be applied only to features of size, such as holes. Material condition modifiers of geometric tolerances are set by clicking the Geometric Tolerances icon on the DimXpert tool bar and selecting MCM symbols that map to the members of this enumeration as follows:

| DimXpert MCM Symbol | Enumeration member |
| --- | --- |
| L | swDimXpertMCM_LMC |
| M | swDimXpertMCM_MMC |
| (blank) | swDimXpertMCM_NoMCM |
| S | swDimXpertMCM_RFS |

## See Also

[SolidWorks.Interop.swdimxpert Namespace](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert_namespace.html)
