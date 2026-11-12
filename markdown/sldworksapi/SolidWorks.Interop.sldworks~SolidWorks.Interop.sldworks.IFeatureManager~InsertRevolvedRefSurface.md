---
title: "InsertRevolvedRefSurface Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertRevolvedRefSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertRevolvedRefSurface.html"
---

# InsertRevolvedRefSurface Method (IFeatureManager)

Creates a revolved reference surface by revolving a profile around a centerline.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertRevolvedRefSurface( _
   ByVal Angle As System.Double, _
   ByVal ReverseDir As System.Boolean, _
   ByVal Angle2 As System.Double, _
   ByVal RevType As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Angle As System.Double
Dim ReverseDir As System.Boolean
Dim Angle2 As System.Double
Dim RevType As System.Integer
Dim value As Feature

value = instance.InsertRevolvedRefSurface(Angle, ReverseDir, Angle2, RevType)
```

### C#

```csharp
Feature InsertRevolvedRefSurface(
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType
)
```

### C++/CLI

```cpp
Feature^ InsertRevolvedRefSurface(
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`: Angle of revolution in radians
- `ReverseDir`: Angle is positive or negative (True or false)
- `Angle2`: Angle of revolution in radians
- `RevType`: Type of revolution (see **Remarks**)

### Return Value

Pointer to [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertRevolvedRefSurface](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertRevolvedRefSurface.html).

## Remarks

Make the selections using [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) before calling this method. See the SOLIDWORKS Help for information about what entities are valid for selection.

The RevType argument can be one of these values:

- 0 = One direction revolution.
- 1 = MidPlane revolution. For this type of revolve, the angle specification specifies the full revolution. The angle to revolve is (angle/2) on either side of the sketch. The ReverseDir argument has no effect.
- 2 = Two direction revolution. For a two direction revolve, Angle is the angle to revolve in Direction1 and Angle2 is the angle to revolve in Direction2.

This method does not support 3D sketches.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
