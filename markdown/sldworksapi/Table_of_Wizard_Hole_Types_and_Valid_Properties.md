---
title: "Hole Wizard Feature Types and Their Valid Properties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapi/Table_of_Wizard_Hole_Types_and_Valid_Properties.htm"
---

# Hole Wizard Feature Types and Their Valid Properties

The properties that are valid for a specific instance of an [IWizardHoleFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html) object depend on the type of Wizard Hole feature. To determine the type of Wizard Hole feature, use [IWizardHoleFeatureData2::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~Type.html). The return value is one of the valid Hole Wizard feature's types as defined in swWzdHoleTypes_e.

The valid IWizardHoleFeatureData2 properties for each Wizard Hole type are:

| Hole and Slot Types | Valid IWizardHoleFeatureData2 Properties |
| --- | --- |
| swSimple | Diameter |
|  | Depth |
|  | Length (slot only) |
|  |  |
| swTapered | MinorDiameter |
|  | Depth |
|  | MajorDiameter |
|  |  |
| swCounterBored | Diameter |
|  | Depth |
|  | CounterBoreDiameter |
|  | CounterBoreDepth |
|  | Length (slot only) |
|  |  |
| swCounterSunk | Diameter |
|  | Depth |
|  | CounterSinkAngle |
|  | CounterSinkDiameter |
|  | Length (slot only) |
|  |  |
| swCounterDrilled | Diameter |
|  | Depth |
|  | CounterDrillDiameter |
|  | CounterDrillDepth |
|  | CounterDrillAngle |
|  |  |
| swSimpleDrilled | Diameter |
|  | Depth |
|  | DrillAngle |
|  |  |
| swTaperedDrilled | MinorDiameter |
|  | Depth |
|  | MajorDiameter |
|  | DrillAngle |
|  |  |
| swCounterBoredDrilled | Diameter |
|  | Depth |
|  | CounterBoreDiameter |
|  | CounterBoreDepth |
|  | DrillAngle |
|  |  |
| swCounterSunkDrilled | Diameter |
|  | Depth |
|  | CounterSinkDiameter |
|  | CounterSinkAngle |
|  | DrillAngle |
|  |  |
| swCounterDrilledDrilled | Diameter |
|  | Depth |
|  | CounterDrillDiameter |
|  | CounterDrillDepth |
|  | DrillAngle |
|  | CounterDrillAngle |
|  |  |
| swCounterBoreBlind | HoleDiameter |
|  | HoleDepth |
|  | CounterBoreDiameter |
|  | CounterBoreDepth |
|  | DrillAngle |
|  | Length (slot only) |
|  |  |
| swCounterBoreBlindCounterSinkMiddle | HoleDiameter |
|  | HoleDepth |
|  | CounterBoreDiameter |
|  | CounterBoreDepth |
|  | MidCounterSinkDiameter |
|  | MidCounterSinkAngle |
|  | DrillAngle |
|  | Length (slot only) |
|  |  |
| swCounterBoreBlindCounterSinkTop | HoleDiameter |
|  | HoleDepth |
|  | CounterBoreDiameter |
|  | CounterBoreDepth |
|  | NearCounterSinkDiameter |
|  | NearCounterSinkAngle |
|  | DrillAngle |
|  | Length (slot only) |
|  |  |
| swCounterBoreBlindCounterSinkTopmiddle | HoleDiameter |
|  | HoleDepth |
|  | CounterBoreDiameter |
|  | CounterBoreDepth |
|  | NearCounterSinkDiameter |
|  | NearCounterSinkAngle |
|  | MidCounterSinkDiameter |
|  | MidCounterSinkAngle |
|  | DrillAngle |
|  | Length (slot only) |
|  |  |
| swCounterBoreThru | ThruHoleDiameter |
|  | ThruHoleDepth |
|  | CounterBoreDiameter |
|  | CounterBoreDepth |
|  | Length (slot only) |
|  |  |
| swCounterBoreThruCounterSinkBottom | ThruHoleDiameter |
|  | ThruHoleDepth |
|  | CounterBoreDiameter |
|  | CounterBoreDepth |
|  | FarCounterSinkDiameter |
|  | FarCounterSinkAngle |
|  | Length (slot only) |
|  |  |
| swCounterBoreThruCounterSinkMiddle | ThruHoleDiameter |
|  | ThruHoleDepth |
|  | CounterBoreDiameter |
|  | CounterBoreDepth |
|  | MidCounterSinkDiameter |
|  | MidCounterSinkAngle |
|  | Length (slot only) |
|  |  |
| swCounterBoreThruCounterSinkMiddleBottom | ThruHoleDiameter |
|  | ThruHoleDepth |
|  | CounterBoreDiameter |
|  | CounterBoreDepth |
|  | MidCounterSinkDiameter |
|  | MidCounterSinkAngle |
|  | FarCounterSinkDiameter |
|  | FarCounterSinkAngle |
|  | Length (slot only) |
|  |  |
| swCounterBoreThruCounterSinkTop | ThruHoleDiameter |
|  | ThruHoleDepth |
|  | CounterBoreDiameter |
|  | CounterBoreDepth |
|  | NearCounterSinkDiameter |
|  | NearCounterSinkAngle |
|  | Length (slot only) |
|  |  |
| swCounterBoreThruCounterSinkTopBottom | ThruHoleDiameter |
|  | ThruHoleDepth |
|  | CounterBoreDiameter |
|  | CounterBoreDepth |
|  | NearCounterSinkDiameter |
|  | NearCounterSinkAngle |
|  | FarCounterSinkDiameter |
|  | FarCounterSinkAngle |
|  | Length (slot only) |
|  |  |
| swCounterBoreThruCounterSinkTopMiddle | ThruHoleDiameter |
|  | ThruHoleDepth |
|  | CounterBoreDiameter |
|  | CounterBoreDepth |
|  | NearCounterSinkDiameter |
|  | NearCounterSinkAngle |
|  | MidCounterSinkDiameter |
|  | MidCounterSinkAngle |
|  | Length (slot only) |
|  |  |
| swCounterBoreThruCounterSinkTopMiddleBottom | ThruHoleDiameter |
|  | ThruHoleDepth |
|  | CounterBoreDiameter |
|  | CounterBoreDepth |
|  | NearCounterSinkDiameter |
|  | NearCounterSinkAngle |
|  | MidCounterSinkDiameter |
|  | MidCounterSinkAngle |
|  | FarCounterSinkDiameter |
|  | FarCounterSinkAngle |
|  | Length (slot only) |
|  |  |
| swHoleBlind | HoleDiameter |
|  | HoleDepth |
|  | DrillAngle |
|  | Length (slot only) |
|  |  |
| swHoleBlindCounterSinkTop | HoleDiameter |
|  | HoleDepth |
|  | NearCounterSinkDiameter |
|  | NearCounterSinkAngle |
|  | DrillAngle |
|  | Length (slot only) |
|  |  |
| swCounterSinkBlind | HoleDiameter |
|  | HoleDepth |
|  | CounterSinkDiameter |
|  | CounterSinkAngle |
|  | DrillAngle |
|  | HeadClearance |
|  | Length (slot only) |
|  |  |
| swHoleThru | ThruHoleDiameter |
|  | ThruHoleDepth |
|  | Length (slot only) |
|  |  |
| swHoleThruCounterSinkBottom | ThruHoleDiameter |
|  | ThruHoleDepth |
|  | FarCounterSinkDiameter |
|  | FarCounterSinkAngle |
|  | Length (slot only) |
|  |  |
| swHoleThruCounterSinkTop | ThruHoleDiameter |
|  | ThruHoleDepth |
|  | NearCounterSinkDiameter |
|  | NearCounterSinkAngle |
|  | Length (slot only) |
|  |  |
| swHoleThruCounterSinkTopBottom | ThruHoleDiameter |
|  | ThruHoleDepth |
|  | NearCounterSinkDiameter |
|  | NearCounterSinkAngle |
|  | FarCounterSinkDiameter |
|  | FarCounterSinkAngle |
|  | Length (slot only) |
|  |  |
| swCounterSinkThru | ThruHoleDiameter |
|  | ThruHoleDepth |
|  | CounterSinkDiameter |
|  | CounterSinkAngle |
|  | HeadClearance |
|  | Length (slot only) |
|  |  |
| swCounterSinkThruCounterSinkBottom | ThruHoleDiameter |
|  | ThruHoleDepth |
|  | CounterSinkDiameter |
|  | CounterSinkAngle |
|  | FarCounterSinkDiameter |
|  | FarCounterSinkAngle |
|  | HeadClearance |
|  | Length (slot only) |
|  |  |
| swTapBlind | TapDrillDiameter |
|  | TapDrillDepth |
|  | ThreadDiameter |
|  | ThreadDepth |
|  | DrillAngle |
|  |  |
| swTapBlindCounterSinkTop | TapDrillDiameter |
|  | TapDrillDepth |
|  | ThreadDiameter |
|  | ThreadDepth |
|  | NearCounterSinkDiameter |
|  | NearCounterSinkAngle |
|  | DrillAngle |
|  |  |
| swTapThru | ThruTapDrillDiameter |
|  | ThruTapDrillDepth |
|  | ThreadDiameter |
|  | ThreadDepth |
|  |  |
| swTapThruCounterSinkBottom | ThruTapDrillDiameter |
|  | ThruTapDrillDepth |
|  | ThreadDiameter |
|  | ThreadDepth |
|  | FarCounterSinkDiameter |
|  | FarCounterSinkAngle |
|  |  |
| swTapThruCounterSinkTop | ThruTapDrillDiameter |
|  | ThruTapDrillDepth |
|  | ThreadDiameter |
|  | ThreadDepth |
|  | NearCounterSinkDiameter |
|  | NearCounterSinkAngle |
|  |  |
| swTapThruCounterSinkTopBottom | ThruTapDrillDiameter |
|  | ThruTapDrillDepth |
|  | ThreadDiameter |
|  | ThreadDepth |
|  | NearCounterSinkDiameter |
|  | NearCounterSinkAngle |
|  | FarCounterSinkDiameter |
|  | FarCounterSinkAngle |
|  |  |
| swPipeTapBlind | TapDrillDiameter |
|  | TapDrillDepth |
|  | ThreadDiameter |
|  | ThreadAngle |
|  | ThreadDepth |
|  | DrillAngle |
|  |  |
| swPipeTapBlindCounterSinkTop | TapDrillDiameter |
|  | TapDrillDepth |
|  | ThreadDiameter |
|  | ThreadAngle |
|  | ThreadDepth |
|  | CounterSinkDiameter |
|  | CounterSinkAngle |
|  | DrillAngle |
|  |  |
| swPipeTapThru | ThruTapDrillDiameter |
|  | ThruTapDrillDepth |
|  | ThreadDiameter |
|  | ThreadAngle |
|  | ThreadDepth |
|  |  |
| swPipeTapThruCounterSinkBottom | ThruTapDrillDiameter |
|  | ThruTapDrillDepth |
|  | ThreadDiameter |
|  | ThreadAngle |
|  | ThreadDepth |
|  | FarCounterSinkDiameter |
|  | FarCounterSinkAngle |
|  |  |
| swPipeTapThruCounterSinkTop | ThruTapDrillDiameter |
|  | ThruTapDrillDepth |
|  | ThreadDiameter |
|  | ThreadAngle |
|  | ThreadDepth |
|  | NearCounterSinkDiameter |
|  | NearCounterSinkAngle |
|  |  |
| swPipeTapThruCounterSinkTopBottom | ThruTapDrillDiameter |
|  | ThruTapDrillDepth |
|  | ThreadDiameter |
|  | ThreadAngle |
|  | ThreadDepth |
|  | NearCounterSinkDiameter |
|  | NearCounterSinkAngle |
|  | FarCounterSinkDiameter |
|  | FarCounterSinkAngle |
|  |  |
| swCounterSinkBlindWithoutHeadClearance | HoleDiameter |
|  | HoleDepth |
|  | CounterSinkDiameter |
|  | CounterSinkAngle |
|  | DrillAngle |
|  | Length (slot only) |
|  |  |
| swCounterSinkThruWithoutHeadClearance | T hruHoleDiameter |
|  | ThruHoleDepth |
|  | CounterSinkDiameter |
|  | CounterSinkAngle |
|  | Length (slot only) |
|  |  |
| swCounterSinkThruCounterSinkBottomWithoutHeadClearance | ThruHoleDiameter |
|  | ThruHoleDepth |
|  | CounterSinkDiameter |
|  | CounterSinkAngle |
|  | FarCounterSinkDiameter |
|  | FarCounterSinkAngle |
|  | HeadClearance |
|  | Length (slot only) |
|  |  |
| swTapBlindCosmeticThread | TapDrillDiameter |
|  | TapDrillDepth |
|  | ThreadDiameter |
|  | ThreadDepth |
|  | DrillAngle |
|  |  |
| swTapBlindCosmeticThreadCounterSinkTop | TapDrillDiameter |
|  | TapDrillDepth |
|  | ThreadDiameter |
|  | ThreadDepth |
|  | DrillAngle |
|  | NearCounterSinkDiameter |
|  | NearCounterSinkAngle |
|  |  |
| swTapThruCosmeticThread | ThruTapDrillDiameter |
|  | ThruTapDrillDepth |
|  | ThreadDiameter |
|  | ThreadDepth |
|  | DrillAngle |
|  |  |
| swTapThruCosmeticThreadCounterSinkTop | ThruTapDrillDiameter |
|  | ThruTapDrillDepth |
|  | ThreadDiameter |
|  | ThreadDepth |
|  | DrillAngle |
|  | NearCounterSinkDiameter |
|  | NearCounterSinkAngle |
|  |  |
| swTapThruCosmeticThreadCounterSinkBottom | ThruTapDrillDiameter |
|  | ThruTapDrillDepth |
|  | ThreadDiameter |
|  | ThreadDepth |
|  | DrillAngle |
|  | FarCounterSinkDiameter |
|  | FarCounterSinkAngle |
|  |  |
| swTapThruCosmeticThreadCounterSinkTopBottom | ThruTapDrillDiameter |
|  | ThruTapDrillDepth |
|  | ThreadDiameter |
|  | ThreadDepth |
|  | DrillAngle |
|  | FarCounterSinkDiameter |
|  | FarCounterSinkAngle |
|  | NearCounterSinkDiameter |
|  | NearCounterSinkAngle |
|  |  |
| swTapThruThreadThru | ThruTapDrillDiameter |
|  | ThruTapDrillDepth |
|  | ThruHoleDepth |
|  | ThruHoleDiameter |
|  | ThreadDiameter |
|  | ThreadDepth |
|  | ThreadEndCondition |
|  |  |
| swTapThruThreadThruCounterSinkTop | ThruTapDrillDiameter |
|  | ThruTapDrillDepth |
|  | ThruHoleDepth |
|  | ThruHoleDiameter |
|  | ThreadDiameter |
|  | ThreadDepth |
|  | ThreadEndCondition |
|  | NearCounterSinkDiameter |
|  | NearCounterSinkAngle |
|  |  |
| swTapThruThreadThruCounterSinkBottom | ThruTapDrillDiameter |
|  | ThruTapDrillDepth |
|  | ThruHoleDepth |
|  | ThruHoleDiameter |
|  | ThreadDiameter |
|  | ThreadDepth |
|  | ThreadEndCondition |
|  | FarCounterSinkDiameter |
|  | FarCounterSinkAngle |
|  |  |
| swTapThruThreadThruCountersinkTopBottom | ThruTapDrillDiameter |
|  | ThruTapDrillDepth |
|  | ThruHoleDepth |
|  | ThruHoleDiameter |
|  | ThreadDiameter |
|  | ThreadDepth |
|  | ThreadEndCondition |
|  | FarCounterSinkDiameter |
|  | FarCounterSinkAngle |
|  | NearCounterSinkDiameter |
|  | NearCounterSinkAngle |
|  |  |
| swTapBlindRemoveThread | TapDrillDiameter |
|  | TapDrillDepth |
