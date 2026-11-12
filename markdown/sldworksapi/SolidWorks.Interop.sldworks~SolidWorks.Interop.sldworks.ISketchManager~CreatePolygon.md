---
title: "CreatePolygon Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CreatePolygon"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreatePolygon.html"
---

# CreatePolygon Method (ISketchManager)

Creates a polygon in the active sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreatePolygon( _
   ByVal XC As System.Double, _
   ByVal YC As System.Double, _
   ByVal Zc As System.Double, _
   ByVal Xp As System.Double, _
   ByVal Yp As System.Double, _
   ByVal Zp As System.Double, _
   ByVal Sides As System.Integer, _
   ByVal Inscribed As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim XC As System.Double
Dim YC As System.Double
Dim Zc As System.Double
Dim Xp As System.Double
Dim Yp As System.Double
Dim Zp As System.Double
Dim Sides As System.Integer
Dim Inscribed As System.Boolean
Dim value As System.Object

value = instance.CreatePolygon(XC, YC, Zc, Xp, Yp, Zp, Sides, Inscribed)
```

### C#

```csharp
System.object CreatePolygon(
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double Xp,
   System.double Yp,
   System.double Zp,
   System.int Sides,
   System.bool Inscribed
)
```

### C++/CLI

```cpp
System.Object^ CreatePolygon(
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double Xp,
   System.double Yp,
   System.double Zp,
   System.int Sides,
   System.bool Inscribed
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XC`: X coordinate for the center
- `YC`: Y coordinate for the center
- `Zc`: Z coordinate for the center
- `Xp`: X coordinate of a vertex
- `Yp`: Y coordinate of a vertex
- `Zp`: Z coordinate of a vertex
- `Sides`: Number of sides in the polygon
- `Inscribed`: True to show an inscribed construction circle, false to show a circumscribed construction circle

### Return Value

Array of [sketch segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) in the polygon

## VBA Syntax

See [SketchManager::CreatePolygon](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~CreatePolygon.html).

## Examples

[Create Polygon (VBA)](Create_Polygon_Example_VB.htm)
[Create Polygon (VB.NET)](Create_Polygon_Example_VBNET.htm)
[Create Polygon (C#)](Create_Polygon_Example_CSharp.htm)

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
