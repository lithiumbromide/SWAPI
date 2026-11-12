---
title: "GetMiddleSurface Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetMiddleSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMiddleSurface.html"
---

# GetMiddleSurface Method (IBody2)

Inserts a midsurface in a body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMiddleSurface( _
   ByVal PlacementPercentage As System.Double, _
   ByRef Face1List As System.Object, _
   ByRef Face2List As System.Object, _
   ByRef Thickness As System.Object, _
   ByRef MiddleSurfaceBody As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim PlacementPercentage As System.Double
Dim Face1List As System.Object
Dim Face2List As System.Object
Dim Thickness As System.Object
Dim MiddleSurfaceBody As System.Object
Dim value As System.Integer

value = instance.GetMiddleSurface(PlacementPercentage, Face1List, Face2List, Thickness, MiddleSurfaceBody)
```

### C#

```csharp
System.int GetMiddleSurface(
   System.double PlacementPercentage,
   out System.object Face1List,
   out System.object Face2List,
   out System.object Thickness,
   out System.object MiddleSurfaceBody
)
```

### C++/CLI

```cpp
System.int GetMiddleSurface(
   System.double PlacementPercentage,
   [Out] System.Object^ Face1List,
   [Out] System.Object^ Face2List,
   [Out] System.Object^ Thickness,
   [Out] System.Object^ MiddleSurfaceBody
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PlacementPercentage`: Position where to insert the midsurface in the body; value of 50 indicates to insert the surface in the middle
- `Face1List`: Array of faces into which the midsurface will be or was inserted; you can provide an array of faces for this parameter and Face2List; if you do not, then the faces are determined internally
- `Face2List`: Array of faces into which the midsurface will be or was inserted; you can provide an array of faces for this parameter and Face1List; if you do not, then the faces are determined internally
- `Thickness`: Array containing minimum and maximum thickness of sheet metal for pairs of faces
- `MiddleSurfaceBody`: [Middle surface body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

### Return Value

0 if no errors; -1 if errors

## VBA Syntax

See [Body2::GetMiddleSurface](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetMiddleSurface.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IGetMiddleSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetMiddleSurface.html)

## Availability

SOLIDWORKS 2009 FCS, Revsion Number 17.0
