---
title: "gtpslFeatureType_e Enumeration"
project: "SOLIDWORKS Utilities API Help"
interface: "gtpslFeatureType_e"
member: ""
kind: "enum"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtpslFeatureType_e.html"
---

# gtpslFeatureType_e Enumeration

Feature type IDs for [IPowerSelect](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IPowerSelect.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum gtpslFeatureType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As gtpslFeatureType_e
```

### C#

```csharp
public enum gtpslFeatureType_e : System.Enum
```

### C++/CLI

```cpp
public enum class gtpslFeatureType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| gtPslFeat_All | 1001 = Feature groups 1001 through 1100 |
| gtPslFeat_AllBoss | 1002 |
| gtPslFeat_AllCut | 1003 |
| gtPslFeat_AllFeatures | 1004 |
| gtPslFeat_AllPatterns | 1005 |
| gtPslFeat_AllReferenceGeometry | 1007 |
| gtPslFeat_AllSheetMetal | 1006 |
| gtPslFeat_AllSurfaceFeats | 1009 |
| gtPslFeat_AllWeldMents | 1008 |
| gtPslFeat_AreaFillPattern | 307 |
| gtPslFeat_Axis | 402 |
| gtPslFeat_BaseBend | 502 |
| gtPslFeat_BaseFlangeTab | 501 = Sheet metal features 501 through 600 |
| gtPslFeat_BasePart | 701 = Other features 701 to 800 |
| gtPslFeat_BossBaseExtrude | 1 = Base boss features 1 through 100 |
| gtPslFeat_BossBaseLoft | 4 |
| gtPslFeat_BossBaseNet | 5 |
| gtPslFeat_BossBaseRevolve | 2 |
| gtPslFeat_BossBaseSweep | 3 |
| gtPslFeat_BossBaseThicken | 6 |
| gtPslFeat_BreakCorner | 514 |
| gtPslFeat_Cavity | 224 |
| gtPslFeat_Chamfer | 202 |
| gtPslFeat_CircularPattern | 302 |
| gtPslFeat_ClosedCorner | 513 |
| gtPslFeat_Combine | 212 |
| gtPslFeat_CoordinateSystem | 403 |
| gtPslFeat_CornerTrim | 527 |
| gtPslFeat_CurveDrivenPattern | 306 |
| gtPslFeat_CutExtrude | 101 = Cut features 101 through 200 |
| gtPslFeat_CutLoft | 104 |
| gtPslFeat_CutNet | 105 |
| gtPslFeat_CutRevolve | 102 |
| gtPslFeat_CutSweep | 103 |
| gtPslFeat_CutThicken | 106 |
| gtPslFeat_CutWithSurface | 107 |
| gtPslFeat_Deform | 211 |
| gtPslFeat_DeleteBody | 217 |
| gtPslFeat_Dome | 209 |
| gtPslFeat_Draft | 205 |
| gtPslFeat_EdgeBend | 504 |
| gtPslFeat_EdgeFlange | 503 |
| gtPslFeat_FlatBends | 524 |
| gtPslFeat_FlatPattern | 525 |
| gtPslFeat_FlattenBends | 520 |
| gtPslFeat_Flex | 223 |
| gtPslFeat_Fold | 516 |
| gtPslFeat_FreeformBend | 518 |
| gtPslFeat_Hem | 507 |
| gtPslFeat_HemBends | 508 |
| gtPslFeat_Imported | 219 |
| gtPslFeat_Indent | 222 |
| gtPslFeat_Jog | 509 |
| gtPslFeat_JogBends | 510 |
| gtPslFeat_Join | 214 |
| gtPslFeat_LibraryFeature | 218 |
| gtPslFeat_LinearPattern | 301 = Patterns/mirror |
| gtPslFeat_LoftedBend | 517 |
| gtPslFeat_MateReference | 405 |
| gtPslFeat_MirrorPart | 702 |
| gtPslFeat_MirrorPattern | 303 |
| gtPslFeat_MiterBend | 506 |
| gtPslFeat_MiterFlange | 505 |
| gtPslFeat_MoveCopy | 216 |
| gtPslFeat_Plane | 401 = Reference features 401 through 500 |
| gtPslFeat_ProcessBends | 523 |
| gtPslFeat_RefPoint | 404 |
| gtPslFeat_Rib | 207 |
| gtPslFeat_Rip | 519 |
| gtPslFeat_RoundBends | 522 |
| gtPslFeat_Scale | 208 |
| gtPslFeat_Shape | 210 |
| gtPslFeat_SharpBends | 521 |
| gtPslFeat_Shell | 206 |
| gtPslFeat_SimpleFillet | 201 = Features 201 through 300 |
| gtPslFeat_SimpleHole | 203 |
| gtPslFeat_SketchBends | 512 |
| gtPslFeat_SketchDrivenPattern | 305 |
| gtPslFeat_SketchedBend | 511 |
| gtPslFeat_Split | 215 |
| gtPslFeat_StockPart | 221 |
| gtPslFeat_SurfceExtend | 814 |
| gtPslFeat_SurfceExtrude | 801 = Surface features 801 through 900 |
| gtPslFeat_SurfceFill | 811 |
| gtPslFeat_SurfceKnit | 817 |
| gtPslFeat_SurfceLoft | 804 |
| gtPslFeat_SurfceMidSurface | 812 |
| gtPslFeat_SurfceMoveCopy | 818 |
| gtPslFeat_SurfceNet | 819 |
| gtPslFeat_SurfceOffset | 808 |
| gtPslFeat_SurfcePartingSurface | 813 |
| gtPslFeat_SurfcePlanar | 805 |
| gtPslFeat_SurfceRadiate | 809 |
| gtPslFeat_SurfceRevolve | 802 |
| gtPslFeat_SurfceRuledSurface | 810 |
| gtPslFeat_SurfceSimpleFillet | 806 |
| gtPslFeat_SurfceSweep | 803 |
| gtPslFeat_SurfceTrim | 815 |
| gtPslFeat_SurfceUnTrim | 816 |
| gtPslFeat_SurfceVariableFillet | 807 |
| gtPslFeat_TableDrivenPattern | 304 |
| gtPslFeat_UiBend | 526 |
| gtPslFeat_Unfold | 515 |
| gtPslFeat_VariableFillet | 220 |
| gtPslFeat_WeldEndCap | 603 |
| gtPslFeat_WeldFilletBead | 604 |
| gtPslFeat_WeldGusset | 602 |
| gtPslFeat_WeldStructuralMember | 605 |
| gtPslFeat_WeldTrimExtend | 601 = Weld features 601 through 700 |
| gtPslFeat_WeldWeldment | 606 |
| gtPslFeat_WizardHole | 204 |
| gtPslFeat_Wrap | 213 |

## See Also

[SolidWorks.Interop.gtswutilities Namespace](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities_namespace.html)
