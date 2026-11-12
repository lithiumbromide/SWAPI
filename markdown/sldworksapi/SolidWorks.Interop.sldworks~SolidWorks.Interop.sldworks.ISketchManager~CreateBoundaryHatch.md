---
title: "CreateBoundaryHatch Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CreateBoundaryHatch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateBoundaryHatch.html"
---

# CreateBoundaryHatch Method (ISketchManager)

Creates area hatch/fill boundary hatches using closed sketch profiles.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateBoundaryHatch( _
   ByVal Angle As System.Double, _
   ByVal Scale As System.Double, _
   ByVal Color As System.Integer, _
   ByVal Hatchname As System.String, _
   ByVal Layername As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim Angle As System.Double
Dim Scale As System.Double
Dim Color As System.Integer
Dim Hatchname As System.String
Dim Layername As System.String
Dim value As System.Object

value = instance.CreateBoundaryHatch(Angle, Scale, Color, Hatchname, Layername)
```

### C#

```csharp
System.object CreateBoundaryHatch(
   System.double Angle,
   System.double Scale,
   System.int Color,
   System.string Hatchname,
   System.string Layername
)
```

### C++/CLI

```cpp
System.Object^ CreateBoundaryHatch(
   System.double Angle,
   System.double Scale,
   System.int Color,
   System.String^ Hatchname,
   System.String^ Layername
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`: Angle of the hatch if hatch is not solid
- `Scale`: Scale factor for the hatch if hatch is not solid
- `Color`: COLORREF value describing the color used for this hatch
- `Hatchname`: Type or name of the hatch from the **Sldwks.ptn** file
- `Layername`: Layer name for the hatch if a drawing document

### Return Value

Array of [sketch hatches](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchHatch.html)

## VBA Syntax

See [SketchManager::CreateBoundaryHatch](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~CreateBoundaryHatch.html).

## Remarks

Before calling this method, select the closed sketch profile for the area hatch/fill boundary hatch.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::CreateRegionHatch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateRegionHatch.html)
[IModelDoc2::InsertHatchedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertHatchedFace.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
