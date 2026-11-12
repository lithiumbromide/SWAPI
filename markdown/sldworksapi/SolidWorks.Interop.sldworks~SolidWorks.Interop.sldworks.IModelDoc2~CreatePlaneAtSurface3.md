---
title: "CreatePlaneAtSurface3 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "CreatePlaneAtSurface3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneAtSurface3.html"
---

# CreatePlaneAtSurface3 Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::InsertRefPlane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertRefPlane.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreatePlaneAtSurface3( _
   ByVal InterIndex As System.Short, _
   ByVal ProjOpt As System.Boolean, _
   ByVal ReverseDir As System.Boolean, _
   ByVal NormalPlane As System.Boolean, _
   ByVal Angle As System.Double, _
   ByVal AutoSize As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim InterIndex As System.Short
Dim ProjOpt As System.Boolean
Dim ReverseDir As System.Boolean
Dim NormalPlane As System.Boolean
Dim Angle As System.Double
Dim AutoSize As System.Boolean
Dim value As System.Object

value = instance.CreatePlaneAtSurface3(InterIndex, ProjOpt, ReverseDir, NormalPlane, Angle, AutoSize)
```

### C#

```csharp
System.object CreatePlaneAtSurface3(
   System.short InterIndex,
   System.bool ProjOpt,
   System.bool ReverseDir,
   System.bool NormalPlane,
   System.double Angle,
   System.bool AutoSize
)
```

### C++/CLI

```cpp
System.Object^ CreatePlaneAtSurface3(
   System.short InterIndex,
   System.bool ProjOpt,
   System.bool ReverseDir,
   System.bool NormalPlane,
   System.double Angle,
   System.bool AutoSize
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InterIndex`: - Multiple intersections - other solutions may exist
  - a surface, plane, and edge - the intersection index is the intersection point to use when there are multiple intersections; when the intersection index input is more than the number of intersection points, the index of the last intersection point found will be used
- `ProjOpt`: True to project the plane along the sketch normal toward the reference surface, false to project the plane to the nearest location on the reference surface
- `ReverseDir`: True to create the plane on the opposite side of the sketch plane, false to not
- `NormalPlane`: True to find the plane normal to the surface for a conical surface, false to find the plane tangent to the surface
- `Angle`: Value of the angular offset of the normal plane, relative to a chosen reference plane
- `AutoSize`: True to automatically size the plane, false to not

### Return Value

Newly created [reference plane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html)

## VBA Syntax

See [ModelDoc2::CreatePlaneAtSurface3](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~CreatePlaneAtSurface3.html).

## Remarks

This method uses the current document setting for displaying of the reference plane as it is created.

| If display of reference planes is... | Then you ... |
| --- | --- |
| Enabled | See the reference plane on the screen as it is created |
| Disabled | Do not see the reference plane on the screen as it is created |

The [IModelDocExtension::GetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceToggle.html) and [IModelDocExtension::SetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SetUserPreferenceToggle.html) methods, with swDisplayPlanes, get or set this display preference.

This method does not select the reference plane after it is created. Objects that are selected before running this method are still selected when the method completes, not the newly created reference plane.

This method returns a RefPlane object. You can use this object for further operations on the reference plane feature. Although just having a reference plane may not be useful, it is a feature, which is an entity, so methods available on those objects are available.

| For this type of user... | Those functions are... |
| --- | --- |
| OLE | Directly accessible |
| COM | Available via use of a QueryInterface |

For example, if the reference plane must be selected, use [IEntity::Select4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity~Select4.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::CreatePlaneAtAngle3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneAtAngle3.html)
[IModelDoc2::CreatePlaneAtOffset3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneAtOffset3.html)
[IModelDoc2::CreatePlaneFixed2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneFixed2.html)
[IModelDoc2::CreatePlanePerCurveAndPassPoint3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlanePerCurveAndPassPoint3.html)
[IModelDoc2::CreatePlaneThru3Points3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneThru3Points3.html)
[IModelDoc2::CreatePlaneThruLineAndPt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneThruLineAndPt.html)
[IModelDoc2::CreatePlaneThruPtParallelToPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneThruPtParallelToPlane.html)
[IModelDoc2::ICreatePlaneAtAngle3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneAtAngle3.html)
[IModelDoc2::ICreatePlaneAtOffset3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneAtOffset3.html)
[IModelDoc2::ICreatePlaneAtSurface3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneAtSurface3.html)
[IModelDoc2::ICreatePlaneFixed2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneFixed2.html)
[IModelDoc2::ICreatePlanePerCurveAndPassPoint3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlanePerCurveAndPassPoint3.html)
[IModelDoc2::ICreatePlaneThru3Points3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneThru3Points3.html)
[IModelDoc2::ICreatePlaneThruLineAndPt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneThruLineAndPt.html)
[IModelDoc2::ICreatePlaneThruPtParallelToPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneThruPtParallelToPlane.html)
[IModelDoc2::GetVisibilityOfConstructPlanes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetVisibilityOfConstructPlanes.html)
[IModelDoc2::ViewDispRefplanes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewDispRefplanes.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
