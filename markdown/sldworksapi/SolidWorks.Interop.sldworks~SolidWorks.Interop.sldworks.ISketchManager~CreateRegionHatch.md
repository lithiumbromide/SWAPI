---
title: "CreateRegionHatch Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CreateRegionHatch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateRegionHatch.html"
---

# CreateRegionHatch Method (ISketchManager)

Creates an area hatch/fill region hatch using a closed sketch profile.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateRegionHatch( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal Angle As System.Double, _
   ByVal Scale As System.Double, _
   ByVal Color As System.Integer, _
   ByVal Hatchname As System.String, _
   ByVal Layername As System.String _
) As SketchHatch
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Angle As System.Double
Dim Scale As System.Double
Dim Color As System.Integer
Dim Hatchname As System.String
Dim Layername As System.String
Dim value As SketchHatch

value = instance.CreateRegionHatch(X, Y, Z, Angle, Scale, Color, Hatchname, Layername)
```

### C#

```csharp
SketchHatch CreateRegionHatch(
   System.double X,
   System.double Y,
   System.double Z,
   System.double Angle,
   System.double Scale,
   System.int Color,
   System.string Hatchname,
   System.string Layername
)
```

### C++/CLI

```cpp
SketchHatch^ CreateRegionHatch(
   System.double X,
   System.double Y,
   System.double Z,
   System.double Angle,
   System.double Scale,
   System.int Color,
   System.String^ Hatchname,
   System.String^ Layername
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X coordinate anywhere within the closed sketch profile
- `Y`: Y coordinate anywhere within the closed sketch profile
- `Z`: Z coordinate anywhere within the closed sketch profile
- `Angle`: Angle of the hatch if the hatch is not solid
- `Scale`: Scale factor for the hatch if the hatch is not solid
- `Color`: COLORREF value describing the color used for the hatch
- `Hatchname`: Type or name of the hatch from the **Sldwks.ptn** file
- `Layername`: Layer name for the hatch if a drawing document

### Return Value

[Sketch hatch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchHatch.html)

## VBA Syntax

See [SketchManager::CreateRegionHatch](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~CreateRegionHatch.html).

## Remarks

This method creates a single area hatch/fill region hatch. All three point coordinates are important. This point is compared to all sketch contours to determine one unique external sketch region that contains the point.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::CreateBoundaryHatch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateBoundaryHatch.html)
[IModelDoc2::InsertHatchedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertHatchedFace.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
