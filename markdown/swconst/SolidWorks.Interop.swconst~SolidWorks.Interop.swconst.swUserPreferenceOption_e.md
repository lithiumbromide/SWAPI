---
title: "swUserPreferenceOption_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swUserPreferenceOption_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceOption_e.html"
---

# swUserPreferenceOption_e Enumeration

User-preference enumerators for customizing document-level annotation, dimension, table, and view-label drafting standards.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swUserPreferenceOption_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swUserPreferenceOption_e
```

### C#

```csharp
public enum swUserPreferenceOption_e : System.Enum
```

### C++/CLI

```cpp
public enum class swUserPreferenceOption_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swDetailingAngleDimension | See System Options and Document Properties. |
| swDetailingAngularRunningDimension | See System Options and Document Properties. |
| swDetailingAnnotation | See System Options and Document Properties. |
| swDetailingArcLengthDimension | See System Options and Document Properties. |
| swDetailingAuxiliaryView | See System Options and Document Properties. |
| swDetailingBalloon | See System Options and Document Properties. |
| swDetailingBendTable | See System Options and Document Properties. |
| swDetailingBillOfMaterial | See System Options and Document Properties. |
| swDetailingChamferDimension | See System Options and Document Properties. |
| swDetailingDatum | See System Options and Document Properties. |
| swDetailingDetailView | See System Options and Document Properties. |
| swDetailingDiameterDimension | See System Options and Document Properties. |
| swDetailingDimension | See System Options and Document Properties. |
| swDetailingDrawingView | See System Options and Document Properties. |
| swDetailingFamilyTable | See System Options and Document Properties. |
| swDetailingGeneralTable | See System Options and Document Properties. |
| swDetailingGeometricTolerance | See System Options and Document Properties. |
| swDetailingHoleDimension | See System Options and Document Properties. |
| swDetailingHoleTable | See System Options and Document Properties. |
| swDetailingLinearDimension | See System Options and Document Properties. |
| swDetailingLocationLabel | See System Options and Document Properties. |
| swDetailingMiscView | See System Options and Document Properties. |
| swDetailingNoOptionSpecified | See System Options and Document Properties. |
| swDetailingNote | See System Options and Document Properties. |
| swDetailingOrdinateDimension | See System Options and Document Properties. |
| swDetailingOrthoView | See System Options and Document Properties. |
| swDetailingPunchTable | See System Options and Document Properties. |
| swDetailingRadiusDimension | See System Options and Document Properties. |
| swDetailingRevisionCloud | See System Options and Document Properties. |
| swDetailingRevisionTable | See System Options and Document Properties. |
| swDetailingSectionView | See System Options and Document Properties. |
| swDetailingSurfaceFinishSymbol | See System Options and Document Properties. |
| swDetailingTableAnnotation | See System Options and Document Properties. |
| swDetailingWeldSymbol | See System Options and Document Properties. |
| swDetailingWeldTable | See System Options and Document Properties. |

## Remarks

Use with:

- [IModelDocExtension::GetUserPreferenceDouble](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceDouble.html) and [IModelDocExtension::SetUserPreferenceDouble](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SetUserPreferenceDouble.html)
- [IModelDocExtension::GetUserPreferenceInteger](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceInteger.html) and [IModelDocExtension::SetUserPreferenceInteger](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SetUserPreferenceInteger.html)
- [IModelDocExtension::GetUserPreferenceString](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceString.html) and [IModelDocExtension::SetUserPreferenceString](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SetUserPreferenceString.html)
- [IModelDocExtension::GetUserPreferenceTextFormat](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceTextFormat.html) and [IModelDocExtension::SetUserPreferenceTextFormat](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SetUserPreferenceTextFormat.html)
- [IModelDocExtension::GetUserPreferenceToggle](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceToggle.html) and [IModelDocExtension::SetUserPreferenceToggle](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SetUserPreferenceToggle.html)

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
