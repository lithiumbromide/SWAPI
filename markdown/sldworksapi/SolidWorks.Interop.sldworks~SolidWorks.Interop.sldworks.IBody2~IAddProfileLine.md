---
title: "IAddProfileLine Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IAddProfileLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileLine.html"
---

# IAddProfileLine Method (IBody2)

Creates a line profile curve and returns a pointer to that curve.

## Syntax

### Visual Basic (Declaration)

```vb
Function IAddProfileLine( _
   ByVal RootPoint As System.Object, _
   ByVal Direction As System.Object _
) As Curve
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim RootPoint As System.Object
Dim Direction As System.Object
Dim value As Curve

value = instance.IAddProfileLine(RootPoint, Direction)
```

### C#

```csharp
Curve IAddProfileLine(
   System.object RootPoint,
   System.object Direction
)
```

### C++/CLI

```cpp
Curve^ IAddProfileLine(
   System.Object^ RootPoint,
   System.Object^ Direction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RootPoint`: Array of 3 doubles (x,y,z)
- `Direction`: Array of 3 doubles (x,y,z)

### Return Value

Line profile, [ICurve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurve.html)

## VBA Syntax

See [Body2::IAddProfileLine](ms-its:sldworksapivb6.chm::/sldworks~Body2~IAddProfileLine.html).

## Examples

[Create Imported Surface Body from Sketch (C#)](Create_Imported_Surface_Body_from_Sketch_Example_CSharp.htm)

## Remarks

You can use this method with [IBody2::ICreateRevolutionSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateRevolutionSurface.html) to generate a cylindrical surface of revolution or with [IBody2::ICreateExtrusionSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateExtrusionSurface.html) to generate a tabulated cylinder.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::AddProfileLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileLine.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
