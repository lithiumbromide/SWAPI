---
title: "swsGeneralSpringError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsGeneralSpringError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsGeneralSpringError_e.html"
---

# swsGeneralSpringError_e Enumeration

General spring status codes

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsGeneralSpringError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsGeneralSpringError_e
```

### C#

```csharp
public enum swsGeneralSpringError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsGeneralSpringError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsGeneralSpringErrorBodyExcludedFromAnalysis | 11 = Selected entity is on a body excluded from analysis |
| swsGeneralSpringErrorFaceDispNull | 12 = Selected face entity is null |
| swsGeneralSpringErrorFaceOnBeam | 13 = Selected face entity is on a beam body |
| swsGeneralSpringErrorFeatureNotLicensed | 19 |
| swsGeneralSpringErrorFeatureNotReady | 17 |
| swsGeneralSpringErrorFeatureNotSupported | 18 |
| swsGeneralSpringErrorHasRemoteMass | 10 = Selected entity has a remote mass |
| swsGeneralSpringErrorInvalidMesh | 1 |
| swsGeneralSpringErrorInvalidStudy | 2 |
| swsGeneralSpringErrorNegativePreloadForce | 15 = Preload force must be >= 0 |
| swsGeneralSpringErrorNegativeStiffness | 14 = Stiffness must be > 0 |
| swsGeneralSpringErrorNoObjectForSourceOrTarget | 8 |
| swsGeneralSpringErrorNumberFacesLessThanTwo | 7 = Number of selected faces must be >= 2 |
| swsGeneralSpringErrorSelectCoordSys | 4 = Select a coordinate system |
| swsGeneralSpringErrorSelectFace | 3 = Select a face |
| swsGeneralSpringErrorSelectionsOnSameComponent | 9 = Selected entities belong to the same component |
| swsGeneralSpringErrorSelectTwoFaces | 5 = Select two faces on two different bodies |
| swsGeneralSpringErrorSourceTargetEntitiesSame | 6 = Selected source and target entities are the same |
| swsGeneralSpringErrorStiffnessAllZero | 16 = Stiffnesses must be > 0 |
| swsGeneralSpringErrorSuccessful | 0 |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
