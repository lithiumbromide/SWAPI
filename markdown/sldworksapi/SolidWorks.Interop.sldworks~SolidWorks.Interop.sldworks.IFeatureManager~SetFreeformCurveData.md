---
title: "SetFreeformCurveData Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "SetFreeformCurveData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetFreeformCurveData.html"
---

# SetFreeformCurveData Method (IFeatureManager)

Adds a curve to the pre-selected face for a Freeform feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetFreeformCurveData( _
   ByVal Direction As System.Short, _
   ByVal CurveParameter As System.Double, _
   ByVal Tangent0X As System.Double, _
   ByVal Tangent0Y As System.Double, _
   ByVal Tangent0Z As System.Double, _
   ByVal Tangent1X As System.Double, _
   ByVal Tangent1Y As System.Double, _
   ByVal Tangent1Z As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Direction As System.Short
Dim CurveParameter As System.Double
Dim Tangent0X As System.Double
Dim Tangent0Y As System.Double
Dim Tangent0Z As System.Double
Dim Tangent1X As System.Double
Dim Tangent1Y As System.Double
Dim Tangent1Z As System.Double

instance.SetFreeformCurveData(Direction, CurveParameter, Tangent0X, Tangent0Y, Tangent0Z, Tangent1X, Tangent1Y, Tangent1Z)
```

### C#

```csharp
void SetFreeformCurveData(
   System.short Direction,
   System.double CurveParameter,
   System.double Tangent0X,
   System.double Tangent0Y,
   System.double Tangent0Z,
   System.double Tangent1X,
   System.double Tangent1Y,
   System.double Tangent1Z
)
```

### C++/CLI

```cpp
void SetFreeformCurveData(
   System.short Direction,
   System.double CurveParameter,
   System.double Tangent0X,
   System.double Tangent0Y,
   System.double Tangent0Z,
   System.double Tangent1X,
   System.double Tangent1Y,
   System.double Tangent1Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Direction`: Direction of the curve; valid values are either 0 or 1
- `CurveParameter`: [Where on the face to add the curve](sldworksAPIProgGuide.chm::/Miscellaneous/FreeFormCurves.htm); valid values are between 0 and 1
- `Tangent0X`: Tangent vector at one end of curve
- `Tangent0Y`: Tangent vector at one end of curve
- `Tangent0Z`: Tangent vector at one end of curve
- `Tangent1X`: Tangent vector at other end of curve
- `Tangent1Y`: Tangent vector at other end of curve
- `Tangent1Z`: Tangent vector at other end of curve

## VBA Syntax

See [FeatureManager::SetFreeformCurveData](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~SetFreeformCurveData.html).

## Remarks

The SOLIDWORKS API Freeform-related methods are intended to journal the actions performed by an interactive user while creating the feature. Because user interaction is required to create a Freeform feature, fully automating the creation of it is not possible using the SOLIDWORKS API.

The typical steps performed by an interactive user to create a Freeform feature are:

1. Select the face to form.
2. Add curves on the selected face. Corresponds to IFeatureManager::SetFreeformCurveData.
3. Add points on the curves. Corresponds to [IFeatureManager::SetFreeformPointData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~SetFreeformPointData.html).
4. Specify boundary continuity. Corresponds to [IFeatureManager::SetFreeformBoundaryContinuity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~SetFreeformBoundaryContinuity.html).

  Interactively pull or push the points to change the shape of the selected face.
5. Insert the Freeform feature. Corresponds to this method, [IFeatureManager::InsertFreeform2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertFreeform2.html).

Record a macro while interactively creating a Freeform feature, then examine the macro to see the order in which the Freeform-related methods are recorded.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
