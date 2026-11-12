---
title: "IReverseEvaluate Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IReverseEvaluate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IReverseEvaluate.html"
---

# IReverseEvaluate Method (IFace2)

Gets the UV parameters for the given XYZ location on this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function IReverseEvaluate( _
   ByVal PositionX As System.Double, _
   ByVal PositionY As System.Double, _
   ByVal PositionZ As System.Double _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim PositionX As System.Double
Dim PositionY As System.Double
Dim PositionZ As System.Double
Dim value As System.Double

value = instance.IReverseEvaluate(PositionX, PositionY, PositionZ)
```

### C#

```csharp
System.double IReverseEvaluate(
   System.double PositionX,
   System.double PositionY,
   System.double PositionZ
)
```

### C++/CLI

```cpp
System.double IReverseEvaluate(
   System.double PositionX,
   System.double PositionY,
   System.double PositionZ
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PositionX`: X coordinate of this location on the face
- `PositionY`: Y coordinate of this location on the face
- `PositionZ`: Z coordinate of this location on the face

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles for the U and V parameters
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This method returns corrected UV parameters for periodic surfaces; thus, you should use this method when dealing with periodic surfaces.

For example, you can have a cylindrical surface that extends from 0 to 2pi in the Udir. The face related to this surface in some cases extends from 0 to pi, then from 0 to pi again. In this case, neither [ISurface::IReverseEvaluate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~IReverseEvaluate.html) nor [ISurface::ReverseEvaluate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface~ReverseEvaluate.html) will work for values greater than pi (the returned U value will be greater than Maximum U for the face). However, IFace2::IReverseEvaluate, and [IFace2::ReverseEvaluate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~ReverseEvaluate.html), will return the correct values.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[ICurve::ReverseEvaluate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~ReverseEvaluate.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
