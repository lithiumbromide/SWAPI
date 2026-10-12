---
title: "CreateFillet Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CreateFillet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateFillet.html"
---

# CreateFillet Method (ISketchManager)

Creates a sketch fillet using the selected sketch entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateFillet( _
   ByVal Radius As System.Double, _
   ByVal ConstrainedCorners As System.Integer _
) As SketchSegment
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim Radius As System.Double
Dim ConstrainedCorners As System.Integer
Dim value As SketchSegment

value = instance.CreateFillet(Radius, ConstrainedCorners)
```

### C#

```csharp
SketchSegment CreateFillet(
   System.double Radius,
   System.int ConstrainedCorners
)
```

### C++/CLI

```cpp
SketchSegment^ CreateFillet(
   System.double Radius,
   System.int ConstrainedCorners
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Radius`: Radius of the fillet in meters
- `ConstrainedCorners`: Action to take as defined in [swConstrainedCornerAction_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstrainedCornerAction_e.html) (see **Remarks**)

### Return Value

[Sketch segment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) for the fillet

## VBA Syntax

See [SketchManager::CreateFillet](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~CreateFillet.html).

## Examples

[Edit Radial Dimension (C#)](Edit_Radial_Dimension_Example_CSharp.htm)
[Edit Radial Dimension (VB.NET)](Edit_Radial_Dimension_Example_VBNET.htm)
[Edit Radial Dimension (VBA)](Edit_Radial_Dimension_Example_VB.htm)

## Remarks

The ConstrainedCorners parameter indicates what action to take if the corner to fillet is constrained or dimensioned. If the corner is not constrained or dimensioned, then this parameter is ignored.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
