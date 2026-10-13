---
title: "MoveRotateLiveSectionPlane Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "MoveRotateLiveSectionPlane"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~MoveRotateLiveSectionPlane.html"
---

# MoveRotateLiveSectionPlane Method (IFeatureManager)

Moves or rotates the selected Live Section Plane using the selected Live Section Plane and its manipulator.

## Syntax

### Visual Basic (Declaration)

```vb
Function MoveRotateLiveSectionPlane( _
   ByVal Feat As System.String, _
   ByVal Type As System.Short, _
   ByVal XorDeltaX As System.Double, _
   ByVal YorDeltaY As System.Double, _
   ByVal ZorDeltaZ As System.Double, _
   ByVal Axisx As System.Double, _
   ByVal Axisy As System.Double, _
   ByVal Axisz As System.Double, _
   ByVal Angle As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Feat As System.String
Dim Type As System.Short
Dim XorDeltaX As System.Double
Dim YorDeltaY As System.Double
Dim ZorDeltaZ As System.Double
Dim Axisx As System.Double
Dim Axisy As System.Double
Dim Axisz As System.Double
Dim Angle As System.Double
Dim value As System.Boolean

value = instance.MoveRotateLiveSectionPlane(Feat, Type, XorDeltaX, YorDeltaY, ZorDeltaZ, Axisx, Axisy, Axisz, Angle)
```

### C#

```csharp
System.bool MoveRotateLiveSectionPlane(
   System.string Feat,
   System.short Type,
   System.double XorDeltaX,
   System.double YorDeltaY,
   System.double ZorDeltaZ,
   System.double Axisx,
   System.double Axisy,
   System.double Axisz,
   System.double Angle
)
```

### C++/CLI

```cpp
System.bool MoveRotateLiveSectionPlane(
   System.String^ Feat,
   System.short Type,
   System.double XorDeltaX,
   System.double YorDeltaY,
   System.double ZorDeltaZ,
   System.double Axisx,
   System.double Axisy,
   System.double Axisz,
   System.double Angle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Feat`: Name of the Live Section Plane as it appears in the FeatureManager design tree
- `Type`: - 0 = Move only, then (XorDeltaX, YorDeltaY, and ZorDeltaZ) is delta vector
  - 1 = Rotate only, then (XorDeltaX, YorDeltaY, and ZorDeltaZ) is the pivot point for rotation, (axisX, axisY, axisZ) is rotating axis
- `XorDeltaX`: Delta X
- `YorDeltaY`: Delta Y
- `ZorDeltaZ`: Delta Z
- `Axisx`: X axis
- `Axisy`: Y axis
- `Axisz`: Z axis
- `Angle`: Value by to rotate the Live Section Plane

### Return Value

True if the Live Section Plane moves or rotates, false if not

## VBA Syntax

See [FeatureManager::MoveRotateLiveSectionPlane](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~MoveRotateLiveSectionPlane.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::InsertLiveSectionPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertLiveSectionPlane.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
