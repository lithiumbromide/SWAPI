---
title: "HoleWizard2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "HoleWizard2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~HoleWizard2.html"
---

# HoleWizard2 Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::HoleWizard3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~HoleWizard3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function HoleWizard2( _
   ByVal GenericHoleType As System.Integer, _
   ByVal StandardIndex As System.Integer, _
   ByVal FastenerTypeIndex As System.Integer, _
   ByVal SSize As System.String, _
   ByVal EndType As System.Short, _
   ByVal Diameter As System.Double, _
   ByVal Depth As System.Double, _
   ByVal Value1 As System.Double, _
   ByVal Value2 As System.Double, _
   ByVal Value3 As System.Double, _
   ByVal Value4 As System.Double, _
   ByVal Value5 As System.Double, _
   ByVal Value6 As System.Double, _
   ByVal Value7 As System.Double, _
   ByVal Value8 As System.Double, _
   ByVal Value9 As System.Double, _
   ByVal Value10 As System.Double, _
   ByVal Value11 As System.Double, _
   ByVal Value12 As System.Double, _
   ByVal ThreadClass As System.String, _
   ByVal RevDir As System.Boolean, _
   ByVal UseFeatScope As System.Boolean, _
   ByVal UseAutoSelect As System.Boolean, _
   ByVal AssemblyFeatureScope As System.Boolean, _
   ByVal AutoSelectComponents As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim GenericHoleType As System.Integer
Dim StandardIndex As System.Integer
Dim FastenerTypeIndex As System.Integer
Dim SSize As System.String
Dim EndType As System.Short
Dim Diameter As System.Double
Dim Depth As System.Double
Dim Value1 As System.Double
Dim Value2 As System.Double
Dim Value3 As System.Double
Dim Value4 As System.Double
Dim Value5 As System.Double
Dim Value6 As System.Double
Dim Value7 As System.Double
Dim Value8 As System.Double
Dim Value9 As System.Double
Dim Value10 As System.Double
Dim Value11 As System.Double
Dim Value12 As System.Double
Dim ThreadClass As System.String
Dim RevDir As System.Boolean
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim AssemblyFeatureScope As System.Boolean
Dim AutoSelectComponents As System.Boolean
Dim value As Feature

value = instance.HoleWizard2(GenericHoleType, StandardIndex, FastenerTypeIndex, SSize, EndType, Diameter, Depth, Value1, Value2, Value3, Value4, Value5, Value6, Value7, Value8, Value9, Value10, Value11, Value12, ThreadClass, RevDir, UseFeatScope, UseAutoSelect, AssemblyFeatureScope, AutoSelectComponents)
```

### C#

```csharp
Feature HoleWizard2(
   System.int GenericHoleType,
   System.int StandardIndex,
   System.int FastenerTypeIndex,
   System.string SSize,
   System.short EndType,
   System.double Diameter,
   System.double Depth,
   System.double Value1,
   System.double Value2,
   System.double Value3,
   System.double Value4,
   System.double Value5,
   System.double Value6,
   System.double Value7,
   System.double Value8,
   System.double Value9,
   System.double Value10,
   System.double Value11,
   System.double Value12,
   System.string ThreadClass,
   System.bool RevDir,
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.bool AssemblyFeatureScope,
   System.bool AutoSelectComponents
)
```

### C++/CLI

```cpp
Feature^ HoleWizard2(
   System.int GenericHoleType,
   System.int StandardIndex,
   System.int FastenerTypeIndex,
   System.String^ SSize,
   System.short EndType,
   System.double Diameter,
   System.double Depth,
   System.double Value1,
   System.double Value2,
   System.double Value3,
   System.double Value4,
   System.double Value5,
   System.double Value6,
   System.double Value7,
   System.double Value8,
   System.double Value9,
   System.double Value10,
   System.double Value11,
   System.double Value12,
   System.String^ ThreadClass,
   System.bool RevDir,
   System.bool UseFeatScope,
   System.bool UseAutoSelect,
   System.bool AssemblyFeatureScope,
   System.bool AutoSelectComponents
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `GenericHoleType`: Hole type as defined in [swWzdGeneralHoleTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdGeneralHoleTypes_e.html)
- `StandardIndex`: Standard property as defined in [swWzdHoleStandards_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleStandards_e.html)
- `FastenerTypeIndex`: Screw type as defined in [swWzdHoleStandardFastenerTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleStandardFastenerTypes_e.html)
- `SSize`: Size of the hole
- `EndType`: End type as defined in [swEndConditions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html)
- `Diameter`: Diameter of the hole in meters
- `Depth`: Depth of the hole in meters
- `Value1`: Hole-related parameter
- `Value2`: Hole-related parameter
- `Value3`: Hole-related parameter
- `Value4`: Hole-related parameter
- `Value5`: Hole-related parameter
- `Value6`: Hole-related parameter
- `Value7`: Hole-related parameter
- `Value8`: Hole-related parameter
- `Value9`: Hole-related parameter
- `Value10`: Hole-related parameter
- `Value11`: Hole-related parameter
- `Value12`: Hole-related parameter
- `ThreadClass`: One of the following thread classes:

  - 1B
  - 2B
  - 3B

  Applies to ANSI inch standard only
- `RevDir`: True to reverse the direction of the hole, false to not
- `UseFeatScope`: True if the feature only affects selected bodies, false if the feature affects all bodies
- `UseAutoSelect`: True to automatically select all bodies and have the feature affect those bodies, false to select the bodies the feature affects
- `AssemblyFeatureScope`: True if the assembly feature only affects selected bodies in the assembly, false if the assembly feature affects all bodies in the assembly
- `AutoSelectComponents`: True to auto-select all affected components, false to only use the selected components

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::HoleWizard2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~HoleWizard2.html).

## Remarks

To add a hole at multiple locations, preselect the sketch points and do not specify any selection marks.

Screw Fit - As defined in [swWzdHoleScrewClearanceTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleScrewClearanceTypes_e.html) and only used if user does not specify a hole diameter; default value is NORMAL_FIT

Drill Angle - defaults to 118 degrees if not specified

Input Metrics - Input angles in radians; input values in meters

Parameters for this method:

- The FastenerTypeIndex parameter has to match the standard and be valid for that hole type or an error occurs.
- The SSize parameter must be a valid size for fastener type or an error occurs.
- The Value1 through Value12 parameters are different for each type of hole. The possible values are as follows, organized by hole type. SOLIDWORKS ignores parameters set to -1.

Value1 through Value12 for different types of holes:

##### Counterbore Holes

Head clearance - Added to either the input counterbore depth or the counterbore depth in the standard.

Parameters for all counterbore holes:

##### Countersink Holes

Head clearance type - Value from [swWzdHoleCounterSinkHeadClearanceTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleCounterSinkHeadClearanceTypes_e.html), which represents how to add the head clearance values to the hole.

Parameters for all countersink holes:

##### Regular Holes

Parameters for all holes:

##### Pipe Tapped Holes

Tap Drill Depth - Depth can be set up as a ratio from the standard thread depth or the input thread depth. If the user does specify a tap drill depth, then the calculation from the thread depth is replaced with the specified depth.

Cosmetic Thread Type - Defaults to swCosmeticThreadNone from [swWzdHoleCosmeticThreadTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleCosmeticThreadTypes_e.html).

Near countersink angle - Can be calculated from standard data as a default.

Parameters for all ptap holes:

##### Tap Holes

Tap Drill Depth - If the user specifies a tap drill depth, then SOLIDWORKS always uses this depth. Tap drill depths can be calculated:

Thread Depth - If the user specifies thread depth, then SOLIDWORKS always uses this depth. Tap drill depths can be calculated:

Cosmetic Thread Type - Specified as defined in swWzdHoleCosmeticThreadTypes_e.

Hcoil Tap Type - Defaults to swTapTypePlug as defined in [swWzdHoleHcoilTapTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleHcoilTapTypes_e.html); used only for the helicoil standard holes.

Thread end condition - Defaults to swEndThreadTypeBLIND as defined in [swWzdHoleThreadEndCondition_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleThreadEndCondition_e.html).

Parameters for all ptap holes:

##### Legacy Holes

For legacy types of holes StandardIndex, FastenerTypeIndex, and SSize are not relevant, and SOLIDWORKS ignores them.

The sequence of parameters 6 to 19 for different types of legacy holes is as follows:

Simple

Tapered

Counterbored

Countersunk

Counterdrilled

Simple Drilled

Tapered Drilled

C-Bored Drilled

C-Sunk Drilled

C-Drilled Drilled

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
