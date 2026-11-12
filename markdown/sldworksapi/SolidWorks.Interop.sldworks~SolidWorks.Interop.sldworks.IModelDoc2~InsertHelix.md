---
title: "InsertHelix Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertHelix"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertHelix.html"
---

# InsertHelix Method (IModelDoc2)

Creates a constant-pitch helix or spiral.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertHelix( _
   ByVal Reversed As System.Boolean, _
   ByVal Clockwised As System.Boolean, _
   ByVal Tapered As System.Boolean, _
   ByVal Outward As System.Boolean, _
   ByVal Helixdef As System.Integer, _
   ByVal Height As System.Double, _
   ByVal Pitch As System.Double, _
   ByVal Revolution As System.Double, _
   ByVal TaperAngle As System.Double, _
   ByVal Startangle As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Reversed As System.Boolean
Dim Clockwised As System.Boolean
Dim Tapered As System.Boolean
Dim Outward As System.Boolean
Dim Helixdef As System.Integer
Dim Height As System.Double
Dim Pitch As System.Double
Dim Revolution As System.Double
Dim TaperAngle As System.Double
Dim Startangle As System.Double

instance.InsertHelix(Reversed, Clockwised, Tapered, Outward, Helixdef, Height, Pitch, Revolution, TaperAngle, Startangle)
```

### C#

```csharp
void InsertHelix(
   System.bool Reversed,
   System.bool Clockwised,
   System.bool Tapered,
   System.bool Outward,
   System.int Helixdef,
   System.double Height,
   System.double Pitch,
   System.double Revolution,
   System.double TaperAngle,
   System.double Startangle
)
```

### C++/CLI

```cpp
void InsertHelix(
   System.bool Reversed,
   System.bool Clockwised,
   System.bool Tapered,
   System.bool Outward,
   System.int Helixdef,
   System.double Height,
   System.double Pitch,
   System.double Revolution,
   System.double TaperAngle,
   System.double Startangle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Reversed`: True creates a constant-pitch helix or spiral in the opposite direction of the circle used to define the diameter, false creates a constant-pitch helix or spiral in the direction of the circle's normal vector; the normal vector of a circle, for example, would be off the screen if the circle were drawn in a counter-clockwise direction
- `Clockwised`: True for clockwise, false for counter-clockwise
- `Tapered`: True to taper the constant-pitch helix, false for no taper
- `Outward`: True to taper the constant-pitch helix outward, false for inward
- `Helixdef`: Constant-pitch helix or spiral definition as defined by [swHelixDefinedBy_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHelixDefinedBy_e.html)
- `Height`: Height of constant-pitch helix in meters
- `Pitch`: Constant-pitch helix or spiral pitch
- `Revolution`: Number of revolutions
- `TaperAngle`: Taper angle of constant-pitch helix
- `Startangle`: Start angle rotation from base axis in radians

## VBA Syntax

See [ModelDoc2::InsertHelix](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertHelix.html).

## Examples

[Create Spiral (C#)](Create_Spiral_Example_CSharp.htm)
[Create Spiral (VB.NET)](Create_Spiral_Example_VBNET.htm)
[Create Spiral (VBA)](Create_Spiral_Example_VB.htm)

## Remarks

When creating a a spiral, you must specify the pitch and number of revolutions.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.html)
[IFeatureManager::InsertVariablePitchHelix Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertVariablePitchHelix.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
