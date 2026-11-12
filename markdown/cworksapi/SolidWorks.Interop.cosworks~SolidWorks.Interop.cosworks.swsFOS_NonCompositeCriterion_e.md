---
title: "swsFOS_NonCompositeCriterion_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsFOS_NonCompositeCriterion_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsFOS_NonCompositeCriterion_e.html"
---

# swsFOS_NonCompositeCriterion_e Enumeration

Factor of safety criteria for non-composite shells

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsFOS_NonCompositeCriterion_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsFOS_NonCompositeCriterion_e
```

### C#

```csharp
public enum swsFOS_NonCompositeCriterion_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsFOS_NonCompositeCriterion_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsFOSNonCompositeCriterion_Automatic | 4 = See Remarks |
| swsFOSNonCompositeCriterion_Coulomb | 3 = Max Normal Stress |
| swsFOSNonCompositeCriterion_MohrCoulomb | 2 = Mohr-Coulomb Stress |
| swsFOSNonCompositeCriterion_Tresca | 1 = Maximum Shear Stress |
| swsFOSNonCompositeCriterion_VonMisesHencky | 0 = Maximum von Mises Stress |

## Remarks

If you set swsFOSNonCompositeCriterion_Automatic, SOLIDWORKS Simulation selects the most appropriate failure criterion across all element types by applying the following conditions:

- The default Failure Criterion assigned in the Material dialog box for each material.
- If you have not assigned a default failure criterion in the Material dialog box, the software assigns the Mohr-Coulomb stress criterion.
- If you selected Max von Mises or Max shear (Tresca) criterion for a beam material, the software uses the yield strength as allowable stress.
- If you selected Max normal or Mohr-Coulomb criterion for a beam material, the software uses the tensile strength as the allowable stress.
- For composite shells, the Tsai-Hill failure criterion is applied.
- Failure indices for the composite shells failure criteria (Tsai-Hill, Tsai-Wu, and Maximum Stress) are calculated from nodal stresses.
- For beams, the factor of safety is calculated from: Upper bound axial and bending stress / Yield Strength.
- For assemblies, the factor of safety is calculated from the un-averaged values of stress components.

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
