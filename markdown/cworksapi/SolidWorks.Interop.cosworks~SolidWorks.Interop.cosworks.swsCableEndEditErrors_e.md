---
title: "swsCableEndEditErrors_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsCableEndEditErrors_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCableEndEditErrors_e.html"
---

# swsCableEndEditErrors_e Enumeration

Cable editing errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsCableEndEditErrors_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsCableEndEditErrors_e
```

### C#

```csharp
public enum swsCableEndEditErrors_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsCableEndEditErrors_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsCableErrCode_InadequateEntitiesSelection | 24 = Insufficient number of entities selected for valid linkage rod definition |
| swsCableErrCode_InvalidCoAxialSelection | 6 = Selected concentric cylindrical faces or edges (for shells or surface bodies) at both ends must not be coaxial |
| swsCableErrCode_InvalidLibraryMaterialDetails | 19 = Setting the material library failed due to invalid library path/name or non-available material name |
| swsCableErrCode_InvalidMaterialSourceType | 16 = Material source type must be cjhosen from swsMaterialSourceType_e |
| swsCableErrCode_InvalidNonCoAxialSelection | 5 = Selected concentric cylindrical faces or edges (for shells or surface bodies) at one end must be coaxial |
| swsCableErrCode_InvalidNonConcentricSelection | 7 = Select concentric cylindrical edges from shell or surface body |
| swsCableErrCode_InvalidSelection | 4 = Select cylindrical face(s) or a single vertex for solid bodies or edge(s) for shells or surface bodies |
| swsCableErrCode_InvalidUnitType | 15 = Unit type must be chosen from swsUnit_e |
| swsCableErrCode_NoActiveDoc | 1 = Active document not found |
| swsCableErrCode_NoActiveStudy | 2 = Active study not found |
| swsCableErrCode_OffsetOptionNotAvailable | 9 = Offset direction and values are not available for vertex selection |
| swsCableErrCode_OutOfRangeAxialStrengthValue | 25 = 0 <= valid value of Axial Strength < 1e+36 |
| swsCableErrCode_OutOfRangeDensity | 23 = 0 < valid value of Density < 1e+36 |
| swsCableErrCode_OutOfRangePreLoadForceValue | 26 = 0 <= valid value of Pre Load Force < 1e+36 |
| swsCableErrCode_OutOfRangeShearModulus | 21 = 0 < valid value of Shear Modulus < 1e+36 |
| swsCableErrCode_OutOfRangeThermalCoefficient | 22 = 0 < valid value of Thermal Coefficient < 1e+36 |
| swsCableErrCode_OutOfRangeYoungsModulus | 20 = 0 < valid value of Young's Modulus < 1e+36 |
| swsCableErrCode_SetLibraryMaterialNA | 18 = Setting the material library is allowed when Material Source Type = swsMaterial_Library |
| swsCableErrCode_SetMaterialPropertyNA | 17 = Setting the material property is allowed when Material Source Type = swsMaterial_Custom |
| swsCableErrCode_SetOperationNotSupported | 3 = You must call BeginEdit to start editing |
| swsCableErrCode_Successful | 0 |
| swsCableErrCode_ZeroDiameterValue | 14 |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
