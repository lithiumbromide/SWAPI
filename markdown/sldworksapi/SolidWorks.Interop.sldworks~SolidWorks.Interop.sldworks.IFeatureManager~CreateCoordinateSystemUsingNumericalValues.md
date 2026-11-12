---
title: "CreateCoordinateSystemUsingNumericalValues Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "CreateCoordinateSystemUsingNumericalValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateCoordinateSystemUsingNumericalValues.html"
---

# CreateCoordinateSystemUsingNumericalValues Method (IFeatureManager)

Creates a coordinate system feature using the specified numerical values for position and orientation with respect to the global coordinate system.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateCoordinateSystemUsingNumericalValues( _
   ByVal UseLocation As System.Boolean, _
   ByVal DeltaX As System.Double, _
   ByVal DeltaY As System.Double, _
   ByVal DeltaZ As System.Double, _
   ByVal UseRotation As System.Boolean, _
   ByVal AngleX As System.Double, _
   ByVal AngleY As System.Double, _
   ByVal AngleZ As System.Double _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim UseLocation As System.Boolean
Dim DeltaX As System.Double
Dim DeltaY As System.Double
Dim DeltaZ As System.Double
Dim UseRotation As System.Boolean
Dim AngleX As System.Double
Dim AngleY As System.Double
Dim AngleZ As System.Double
Dim value As Feature

value = instance.CreateCoordinateSystemUsingNumericalValues(UseLocation, DeltaX, DeltaY, DeltaZ, UseRotation, AngleX, AngleY, AngleZ)
```

### C#

```csharp
Feature CreateCoordinateSystemUsingNumericalValues(
   System.bool UseLocation,
   System.double DeltaX,
   System.double DeltaY,
   System.double DeltaZ,
   System.bool UseRotation,
   System.double AngleX,
   System.double AngleY,
   System.double AngleZ
)
```

### C++/CLI

```cpp
Feature^ CreateCoordinateSystemUsingNumericalValues(
   System.bool UseLocation,
   System.double DeltaX,
   System.double DeltaY,
   System.double DeltaZ,
   System.bool UseRotation,
   System.double AngleX,
   System.double AngleY,
   System.double AngleZ
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseLocation`: True to define the position of the coordinate system using numerical values, false to not
- `DeltaX`: Distance in meters along the x-axis of the global coordinate system; valid only if UseLocation is true
- `DeltaY`: Distance in meters along the y-axis of the global coordinate system; valid only if UseLocation is true
- `DeltaZ`: Distance in meters along the z-axis of the global coordinate system; valid only if UseLocation is true
- `UseRotation`: True to define the orientation of the coordinate system using numerical values, false to not
- `AngleX`: 0 <= Rotation in radians from the x-axis of the global coordinate system <= 6.283 radians; valid only if UseRotation is true
- `AngleY`: 0 <= Rotation in radians from the y-axis of the global coordinate system <= 6.283 radians; valid only if UseRotation is true
- `AngleZ`: 0 <= Rotation in radians from the z-axis of the global coordinate system <= 6.283 radians; valid only if UseRotation is true

### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::CreateCoordinateSystemUsingNumericalValues](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~CreateCoordinateSystemUsingNumericalValues.html).

## Examples

'VBA

'=============================================

'Preconditions:

'1. Open a new part.
'2. Open the Immediate window.

'Postconditions:

'1. Creates a new coordinate system at the specified position and angle relative to the global coordinate system.

'2. Select **Coordinate System1** in the FeatureManager design tree.

'3. Inspect the Immediate window and graphics area.

'=============================================

Option Explicit

Sub main()

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim swFeatMgr As FeatureManager

Dim swCoordFeat As SldWorks.Feature

Dim posVal, angVal As Double

Dim pos, ang As Double

Set swApp = Application.SldWorks

Set swModel = swApp.ActiveDoc

Set swFeatMgr = swModel.FeatureManager

pos = 200

posVal = pos / 1000 ' Position in meters

' 1 radian = 180º/p = 57.295779513º or approximately 57.3º

ang = 60

angVal = ang / 57.295779513 ' Angle in radians

Debug.Print "Position(mm) : [" & pos & ", " & pos & ", " & pos & "] Angle(deg) : [" & ang & ", " & ang & ", " & ang & "] "

Set swCoordFeat = swFeatMgr.**CreateCoordinateSystemUsingNumericalValues**(True, posVal, posVal, posVal, True, angVal, angVal, angVal)

Debug.Print "Name of the coordinate system feature : " & swCoordFeat.**Name**

End Sub

## Remarks

This method is valid only for parts and assemblies.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::CreateCoordinateSystem Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateCoordinateSystem.html)
[IFeatureManager::InsertCoordinateSystem Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCoordinateSystem.html)
[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
