---
title: "AdvancedHole Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "AdvancedHole"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AdvancedHole.html"
---

# AdvancedHole Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::AdvancedHole2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AdvancedHole2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AdvancedHole( _
   ByVal AdvancedHoleNearElementArray As System.Object, _
   ByVal AdvancedHoleFarElementArray As System.Object, _
   ByVal UseBaselineDimensions As System.Boolean, _
   ByVal IsCustomCallout As System.Boolean, _
   ByRef ResultArray As System.Object _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim AdvancedHoleNearElementArray As System.Object
Dim AdvancedHoleFarElementArray As System.Object
Dim UseBaselineDimensions As System.Boolean
Dim IsCustomCallout As System.Boolean
Dim ResultArray As System.Object
Dim value As Feature

value = instance.AdvancedHole(AdvancedHoleNearElementArray, AdvancedHoleFarElementArray, UseBaselineDimensions, IsCustomCallout, ResultArray)
```

### C#

```csharp
Feature AdvancedHole(
   System.object AdvancedHoleNearElementArray,
   System.object AdvancedHoleFarElementArray,
   System.bool UseBaselineDimensions,
   System.bool IsCustomCallout,
   out System.object ResultArray
)
```

### C++/CLI

```cpp
Feature^ AdvancedHole(
   System.Object^ AdvancedHoleNearElementArray,
   System.Object^ AdvancedHoleFarElementArray,
   System.bool UseBaselineDimensions,
   System.bool IsCustomCallout,
   [Out] System.Object^ ResultArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AdvancedHoleNearElementArray`: Array of near side hole data objects (see **Remarks**)
- `AdvancedHoleFarElementArray`: Array of far side hole data objects (see **Remarks**)
- `UseBaselineDimensions`: True to use baseline dimensions, false to not (see **Remarks**)
- `IsCustomCallout`: True to customize the hole callout, false to use a default hole callout (see **Remarks**)
- `ResultArray`: Array of result codes as defined in [swAdvancedHoleResults_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAdvancedHoleResults_e.html) (see **Remarks**)

### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html); Nothing or null if this method results in an invalid geometry condition (see **Remarks**)

## VBA Syntax

See [FeatureManager::AdvancedHole](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~AdvancedHole.html).

## Remarks

The Advanced Hole feature:

- is separate from the Hole Wizard functionality (see [FeatureManager::HoleWizard5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~HoleWizard5.html)).
- consists of several hole elements, e.g., counterbore, countersink, straight, and tapered tap, that are stacked from the near and far side faces inward. The near and far side stacks, combined, form the Advanced Hole.
- can be added only to parts at this time.

AdvancedHoleNearElementArray and AdvancedHoleFarElementArray each contain one or more hole type-specific objects in order as they stack from the near and far side faces:

- [ICounterboreElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICounterboreElementData.html)
- [ICountersinkElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData.html)
- [IStraightElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData.html)
- [IStraightTapElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData.html)
- [ITaperedTapElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData.html)

The hole type-specific interfaces above extend the parent interface, [IAdvancedHoleElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.html), which you use to set general Advanced Hole properties.

UseBaseLineDimensions controls which hole type-specific properties are valid. See [IAdvancedHoleFeatureData::UseBaselineDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~UseBaselineDimensions.html).

IsCustomCallout set to true allows you to set a custom callout string for individual hole elements using [IAdvancedHoleElementData::CalloutString](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~CalloutString.html).

ResultArray contains a return code for each element in AdvancedHoleNearElementArray and AdvancedHoleFarElementArray. It is possible for this method to fail to create an advanced hole, even though ResultArray contains all success result codes. If the individual hole elements all combine to produce invalid geometry (e.g., a disjoint body or a self-intersecting face) or if incorrect near or far side faces are selected, then this method returns Nothing or null.

To create an Advanced Hole feature, follow the examples which do the following:

1. Call [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.html) to select the near side (Mark = 256) and far side (Mark = 512) faces of the Advanced Hole. You must select these faces by location, so do not use [IEntity::Select4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~Select4.html).
2. Call [IModelDocExtension::CreateAdvancedHoleElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateAdvancedHoleElementData.html) to create an AdvancedHoleElementData object.
3. Set the general Advanced Hole properties using the AdvancedHoleElementData object.
4. Cast the AdvancedHoleElementData object using one of the hole type-specific interfaces.
5. Set the specific Advanced Hole properties using the hole type-specific object.
6. Repeat steps 2 - 5 for each hole element you want to add to the near and far side stacks of the Advanced Hole.
7. Create near and far side arrays of the hole type-specific objects in stacking order from each face inward. The innermost elements of each stack should match to create a contiguous hole that extends from near side face to far side face.
8. Pass the near and far side arrays to IFeatureManager::AdvancedHole to create the Advanced Hole.
9. Delete the defining Advanced Hole sketch point and call [ISketchManager::CreatePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreatePoint.html) one or more times to insert the Advanced Hole in multiple locations.

To edit an Advanced Hole feature, call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html) to access [IAdvancedHoleFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData.html). See [Accessing Selections that Define Features](sldworksapiprogguide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
