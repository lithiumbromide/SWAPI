---
title: "InsertTableDrivenPattern Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertTableDrivenPattern"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertTableDrivenPattern.html"
---

# InsertTableDrivenPattern Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertTableDrivenPattern2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertTableDrivenPattern2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertTableDrivenPattern( _
   ByVal FileName As System.String, _
   ByVal PointVar As System.Object, _
   ByVal UseCentrod As System.Boolean, _
   ByVal GeomPatt As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim FileName As System.String
Dim PointVar As System.Object
Dim UseCentrod As System.Boolean
Dim GeomPatt As System.Boolean
Dim value As Feature

value = instance.InsertTableDrivenPattern(FileName, PointVar, UseCentrod, GeomPatt)
```

### C#

```csharp
Feature InsertTableDrivenPattern(
   System.string FileName,
   System.object PointVar,
   System.bool UseCentrod,
   System.bool GeomPatt
)
```

### C++/CLI

```cpp
Feature^ InsertTableDrivenPattern(
   System.String^ FileName,
   System.Object^ PointVar,
   System.bool UseCentrod,
   System.bool GeomPatt
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of the file that has the coordinates information; can be an empty string (see **Remarks**)
- `PointVar`: Array of x, y coordinates of the points (see **Remarks**)
- `UseCentrod`: True to use the centroid of the seed feature, face, or body; false to use another point as the reference point (see **Remarks**)
- `GeomPatt`: True to pattern the geometry, false to not

### Return Value

[Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertTableDrivenPattern](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertTableDrivenPattern.html).

## Remarks

Specify:

- coordinates for the input points in system units in a **.sldptab** or **.txt** file for FileName.
  - or -
- input points in system units in PointVar. Because each point has two coordinates (x, y), the size of PointVar is (2 x number_of_points).

This method requires selecting the input entities using these selection marks:

- 4 = Seed feature
- 16 = Coordinate system
- 32 = Reference point
- 128 = Seed face
- 256 = Seed body

If UseCentrod is false, then you must specify a reference point.

See the SOLIDWORKS Help for more information about table-driven patterns.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html)
[IFeatureManager::IInsertTableDrivenPattern Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertTableDrivenPattern.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
