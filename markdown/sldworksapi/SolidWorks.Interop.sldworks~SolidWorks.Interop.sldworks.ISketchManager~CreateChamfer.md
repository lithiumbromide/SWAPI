---
title: "CreateChamfer Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CreateChamfer"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateChamfer.html"
---

# CreateChamfer Method (ISketchManager)

Creates a chamfer between two selected sketch entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateChamfer( _
   ByVal Type As System.Integer, _
   ByVal Distance As System.Double, _
   ByVal AngleORdist As System.Double _
) As SketchSegment
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim Type As System.Integer
Dim Distance As System.Double
Dim AngleORdist As System.Double
Dim value As SketchSegment

value = instance.CreateChamfer(Type, Distance, AngleORdist)
```

### C#

```csharp
SketchSegment CreateChamfer(
   System.int Type,
   System.double Distance,
   System.double AngleORdist
)
```

### C++/CLI

```cpp
SketchSegment^ CreateChamfer(
   System.int Type,
   System.double Distance,
   System.double AngleORdist
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Type of chamfer as defined in [swSketchChamferType_e](ms-its:swconst.chm::/SOLIDWORKS.interop.swconst~SOLIDWORKS.interop.swconst.swSketchChamferType_e.html)
- `Distance`: Distance of the chamfer
- `AngleORdist`: - If Type = swSketchChamfer_DistanceDistance, then the second chamfer distance
  - If Type = swSketchChamfer_DistanceAngle, then the second chamfer angle
  - If Type = swSketchChamfer_DistanceEqual, then this argument is ignored because Distance
    is used for both edges

### Return Value

[Sketch segment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) for the chamfer

## VBA Syntax

See [SketchManager::CreateChamfer](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~CreateChamfer.html).

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
