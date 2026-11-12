---
title: "InsertCoordinateSystem Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertCoordinateSystem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCoordinateSystem.html"
---

# InsertCoordinateSystem Method (IFeatureManager)

Inserts a coordinate system feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertCoordinateSystem( _
   ByVal XFlippedIn As System.Boolean, _
   ByVal YFlippedIn As System.Boolean, _
   ByVal ZFlippedIn As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim XFlippedIn As System.Boolean
Dim YFlippedIn As System.Boolean
Dim ZFlippedIn As System.Boolean
Dim value As Feature

value = instance.InsertCoordinateSystem(XFlippedIn, YFlippedIn, ZFlippedIn)
```

### C#

```csharp
Feature InsertCoordinateSystem(
   System.bool XFlippedIn,
   System.bool YFlippedIn,
   System.bool ZFlippedIn
)
```

### C++/CLI

```cpp
Feature^ InsertCoordinateSystem(
   System.bool XFlippedIn,
   System.bool YFlippedIn,
   System.bool ZFlippedIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XFlippedIn`: True to flip the x axis direction, false to not
- `YFlippedIn`: True to flip the y axis direction, false to not
- `ZFlippedIn`: True to flip the z axis direction, false to not

### Return Value

[Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertCoordinateSystem](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertCoordinateSystem.html).

## Examples

[Insert Coordinate System Feature at Center of Mass (VBA)](Insert_Coordinate_System_Feature_at_Center_of_Mass_Example_VB.htm)

## Remarks

Make the selections using [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) with a mark of:

- 1 - Origin
- 2 - X axis
- 4 - Y axis
- 8 - Z axis

This method:

- does not require all three axis to be selected. The behavior is the same as interactively creating a coordinate system. See the SOLIDWORKS Help for more information.
- works in section-view mode, but not if temporary geometry that only exists in section-view mode is selected.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)
[IFeatureManager::CreateCoordinateSystem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateCoordinateSystem.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
