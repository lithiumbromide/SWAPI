---
title: "FeatureManager::HoleWizard"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/FeatureManager/FeatureManager__HoleWizard.htm"
---

# FeatureManager::HoleWizard

This method is obsolete and has been superseded by [FeatureManager::HoleWizard2](sldworksAPI.chm::/FeatureManager/FeatureManager__HoleWizard2.htm).

Description

This method creates a hole using the hole wizard.

Syntax (OLE Automation)

retval = FeatureManager.HoleWizard ( genericHoleType, standardIndex, fastenerTypeIndex, sSize, endType, diameter, depth, value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12 )

| Input: | (long) genericHoleType | Hole type as defined in swWzdGeneralHoleTypes_e |
| --- | --- | --- |
| Input: | (long) standardIndex | Standard property as defined in swWzdHoleStandards_e |
| Input: | (long) fastenerTypeIndex | Screw type as defined in swWzdHoleStandardFastenerTypes_e |
| Input: | (BSTR) sSize | Size of the hole |
| Input: | (short) endType | End type as defined in swEndConditions_e |
| Input: | (double) diameter | Diameter of the hole in meters |
| Input: | (double) depth | Depth of the hole in meters |
| Input: | (double) value1 | Hole-related parameter |
| Input: | (double) value2 | Hole-related parameter |
| Input: | (double) value3 | Hole-related parameter |
| Input: | (double) value4 | Hole-related parameter |
| Input: | (double) value5 | Hole-related parameter |
| Input: | (double) value6 | Hole-related parameter |
| Input: | (double) value7 | Hole-related parameter |
| Input: | (double) value8 | Hole-related parameter |
| Input: | (double) value9 | Hole-related parameter |
| Input: | (double) value10 | Hole-related parameter |
| Input: | (double) value11 | Hole-related parameter |
| Input: | (double) value12 | Hole-related parameter |
| Output: | (LPFEATURE) retVal | Pointer to the Feature object |

Syntax (COM)

status = FeatureManager->HoleWizard ( genericHoleType, standardIndex, fastenerTypeIndex, sSize, endType, diameter, depth, value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, retval )

| Input: | (long) genericHoleType | Hole type as defined in swWzdGeneralHoleTypes_e |
| --- | --- | --- |
| Input: | (long) standardIndex | Standard property as defined in swWzdHoleStandards_e |
| Input: | (long) fastenerTypeIndex | Screw type as defined in swWzdHoleStandardFastenerTypes_e |
| Input: | (BSTR) sSize | Size of the hole |
| Input: | (short) endType | End type as defined in swEndConditions_e |
| Input: | (double) diameter | Diameter of the hole in meters |
| Input: | (double) depth | Depth of the hole in meters |
| Input: | (double) value1 | Hole-related parameter |
| Input: | (double) value2 | Hole-related parameter |
| Input: | (double) value3 | Hole-related parameter |
| Input: | (double) value4 | Hole-related parameter |
| Input: | (double) value5 | Hole-related parameter |
| Input: | (double) value6 | Hole-related parameter |
| Input: | (double) value7 | Hole-related parameter |
| Input: | (double) value8 | Hole-related parameter |
| Input: | (double) value9 | Hole-related parameter |
| Input: | (double) value10 | Hole-related parameter |
| Input: | (double) value11 | Hole-related parameter |
| Input: | (double) value12 | Hole-related parameter |
| Output: | (LPFEATURE) retVal | Pointer to the Feature object |
| Output: | (HRESULT) status | S_OK if successful |

Remarks

Screw Fit - As defined in swWzdHoleScrewClearanceTypes_e and only used if user does not specify a hole diameter; default value is NORMAL_FIT

Drill Angle - defaults to 118° if not specified

Input Metrics - Input angles in radians; input values in meters

Parameters for this method:

- The fastenerTypeIndex parameter has to match the standard and be valid for that hole type or an error occurs.
- The sSize parameter must be a valid size for fastener type or an error occurs.
- The value1 through value12 parameters are different for each type of hole. The possible values are as follows, organized by hole type. SolidWorks ignores parameters set to -1.

value1 through value12 for different types of holes:

#### Counterbore Holes

Head clearance – Added to either the input counterbore depth or the counterbore depth in the standard.

Parameters for all counterbore holes:

1. Hole Diameter
2. Hole Depth
3. CounterBore Diameter
4. CounterBore Depth
5. HeadClearance
6. Screw Fit
7. Drill Angle
8. Near Csink Diameter
9. Near Csink Angle
10. Bot Csink Diameter
11. Bot Csink Angle
12. Far Csink Diameter
13. Far Csink Angle
14. Offset

#### Countersink Holes

Head clearance type - Value from swWzdHoleCounterSinkHeadClearanceTypes_e, which represents how to add the head clearance values to the hole.

Parameters for all countersink holes:

1. Hole Diameter
2. Hole Depth
3. Near Csink Diameter
4. Near Csink Angle
5. Head Clearance
6. Screw Fit
7. Drill Angle
8. Far Csink Diameter
9. Far Csink Angle
10. Offset
11. Head Clearance Type

#### Regular Holes

Parameters for all holes:

1. Hole Diameter
2. Hole Depth
3. Screw Fit
4. Drill Angle
5. Near Csink Diameter
6. Near Csink Angle
7. Far Csink Diameter
8. Far Csink Angle
9. Offset

#### Pipe Tapped Holes

Tap Drill Depth – Depth can be setup as a ratio from the standard thread depth or the input thread depth. If the user does specify a tap drill depth, the calculation from the thread depth is replaced with the specified depth.

Cosmetic Thread Type - Defaults to swCosmeticThreadTypeNone from swWzdHoleCosmeticThreadTypes_e.

Near countersink angle - Can be calculated from standard data as a default.

Parameters for all ptap holes:

1. Tap drill diameter
2. Tap drill depth
3. Thread Depth
4. Near Csink Diameter
5. Near Csink Angle
6. Far Csink Diameter
7. Far Csink Angle
8. Drill Angle
9. Cosmetic Thread Type
10. Offset

#### Tap Holes

Tap Drill Depth - If the user specifies a tap drill depth, SolidWorks always uses this depth. Tap drill depths can be calculated:

1. For helicoil holes: Tap drill depth is calculated based on a constant * tap drill diameter + allowance for tap type (bottoming or plug).
2. For tapped holes: Tap drill depth is calculated from the thread length + advance + allowance for tap type (bottoming or plug).

Thread Depth – If the user specifies thread depth, SolidWorks always uses this depth. Tap drill depths can be calculated:

1. For helicoil holes: Thread depth is calculated based on a constant (determined by hole type i.e. Insert = 1.0 * Dia) + thread depth from the standard * thread major diameter.
2. For tapped holes: based on 2 * thread diameter

Cosmetic Thread Type - Specified as defined in swWzdHoleCosmeticThreadTypes_e

Hcoil Tap Type - Defaults to swTapTypePlug as defined in swWzdHoleHcoilTapTypes_e. Used only for the helicoil standard holes.

Thread end condition - Defaults to swThreadEndConditionBLIND as defined in swWzdHoleThreadEndCondition_e.

Parameters for all ptap holes:

1. Tap drill diameter
2. Tap drill depth
3. Thread Depth
4. Near Csink Diameter
5. Near Csink Angle
6. Far Csink Diameter
7. Far Csink Angle
8. Drill Angle
9. Cosmetic Thread Type
10. Thread End Condition
11. Helicoil Tap Type
12. Offset

#### Legacy Holes

For legacy types of holes standardIndex, fastenerTypeIndex, sSize are not relevant and SolidWorks ignores them.

The sequence of parameters 6 to 19 for different types of legacy holes is as follows:

Simple

1. Diameter
2. Depth
3. Sketch ID

Tapered

1. Minor Diameter
2. Depth
3. Sketch ID
4. Major Diameter

Counterbored

1. Diameter
2. Depth
3. Sketch ID
4. C-Bore Diameter
5. C-Bore Depth

Countersunk

1. Diameter
2. Depth
3. Sketch ID
4. C-Sink Angle
5. C-Sink Diameter

Counterdrilled

1. Diameter
2. Depth
3. Sketch ID
4. C-Drill Diameter
5. C-Drill Depth
6. C-Drill Angle

Simple Drilled

1. Diameter
2. Depth
3. Sketch ID
4. Drill Angle

Tapered Drilled

1. Minor Diameter
2. Depth
3. Sketch ID
4. Major Diameter
5. Drill Angle

C-Bored Drilled

1. Diameter
2. Depth
3. Sketch ID
4. C-Bore Diameter
5. C-Bore Depth
6. Drill Angle

C-Sunk Drilled

1. Diameter
2. Depth
3. Sketch ID
4. C-Sink Diameter
5. C-Sink Angle
6. Drill Angle

C-Drilled Drilled

1. Diameter
2. Depth
3. Sketch ID
4. C-Drill Diameter
5. C-Drill Depth
6. Drill Angle
7. C-Drill Angle
