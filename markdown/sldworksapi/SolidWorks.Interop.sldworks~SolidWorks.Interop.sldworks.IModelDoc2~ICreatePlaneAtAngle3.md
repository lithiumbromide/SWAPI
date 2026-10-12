---
title: "ICreatePlaneAtAngle3 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ICreatePlaneAtAngle3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneAtAngle3.html"
---

# ICreatePlaneAtAngle3 Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::InsertRefPlane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertRefPlane.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreatePlaneAtAngle3( _
   ByVal Val As System.Double, _
   ByVal FlipDir As System.Boolean, _
   ByVal AutoSize As System.Boolean _
) As RefPlane
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Val As System.Double
Dim FlipDir As System.Boolean
Dim AutoSize As System.Boolean
Dim value As RefPlane

value = instance.ICreatePlaneAtAngle3(Val, FlipDir, AutoSize)
```

### C#

```csharp
RefPlane ICreatePlaneAtAngle3(
   System.double Val,
   System.bool FlipDir,
   System.bool AutoSize
)
```

### C++/CLI

```cpp
RefPlane^ ICreatePlaneAtAngle3(
   System.double Val,
   System.bool FlipDir,
   System.bool AutoSize
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Val`: Angle from the selected plane in radians
- `FlipDir`: True to flip the plane the other way for first direction, false to not
- `AutoSize`: True to automatically size the plane, false to not

### Return Value

Newly created [reference plane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html)

## VBA Syntax

See [ModelDoc2::ICreatePlaneAtAngle3](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ICreatePlaneAtAngle3.html).

## Remarks

This method uses the current document setting for displaying the reference plane. If display of reference planes is disabled, then you do not see the reference plane on the screen. If display of reference planes is enabled, then you see it. [IModelDocExtension::GetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetUserPreferenceToggle.html) swDisplayPlanes and [IModelDocExtenison::SetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SetUserPreferenceToggle.html) swDisplayPlanes get or set this display preference.

This method does not select the reference plane after it is created. Objects that are selected before running this method are still selected when the method completes, not the newly created reference plane.

This method returns an IRefPlane object. This object can then be used for subsequent operations on the reference plane feature. Having a IRefPlane object may not be useful, except that it is a feature, which is an entity, so methods available on those objects are available. For an OLE user, those functions are directly accessible; for a COM user, those functions are available via QueryInterface. For example, to select the reference plane, use [IEntity::Select4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity~Select4.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::CreatePlaneAtAngle3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneAtAngle3.html)
[IModelDoc2::CreatePlaneAtOffset3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneAtOffset3.html)
[IModelDoc2::CreatePlaneAtSurface3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneAtSurface3.html)
[IModelDoc2::CreatePlaneFixed2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneFixed2.html)
[IModelDoc2::CreatePlanePerCurveAndPassPoint3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlanePerCurveAndPassPoint3.html)
[IModelDoc2::CreatePlaneThru3Points3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneThru3Points3.html)
[IModelDoc2::CreatePlaneThruLineAndPt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneThruLineAndPt.html)
[IModelDoc2::CreatePlaneThruPtParallelToPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneThruPtParallelToPlane.html)
[IModelDoc2::GetVisibilityOfConstructPlanes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetVisibilityOfConstructPlanes.html)
[IModelDoc2::ICreatePlaneAtOffset3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneAtOffset3.html)
[IModelDoc2::ICreatePlaneAtSurface3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneAtSurface3.html)
[IModelDoc2::ICreatePlaneFixed2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneFixed2.html)
[IModelDoc2::ICreatePlanePerCurveAndPassPoint3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlanePerCurveAndPassPoint3.html)
[IModelDoc2::ICreatePlaneThru3Points3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneThru3Points3.html)
[IModelDoc2::ICreatePlaneThruLineAndPt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneThruLineAndPt.html)
[IModelDoc2::ICreatePlaneThruPtParallelToPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneThruPtParallelToPlane.html)
[IModelDoc2::ViewDispRefplanes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewDispRefplanes.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
