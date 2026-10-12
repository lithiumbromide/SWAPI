---
title: "InsertCavity4 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "InsertCavity4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertCavity4.html"
---

# InsertCavity4 Method (IAssemblyDoc)

Inserts a cavity to the active part using a selected component.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertCavity4( _
   ByVal ScaleFactor_x As System.Double, _
   ByVal ScaleFactor_y As System.Double, _
   ByVal ScaleFactor_z As System.Double, _
   ByVal IsUniform As System.Boolean, _
   ByVal ScaleType As System.Integer, _
   ByVal KeepPieceIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim ScaleFactor_x As System.Double
Dim ScaleFactor_y As System.Double
Dim ScaleFactor_z As System.Double
Dim IsUniform As System.Boolean
Dim ScaleType As System.Integer
Dim KeepPieceIndex As System.Integer

instance.InsertCavity4(ScaleFactor_x, ScaleFactor_y, ScaleFactor_z, IsUniform, ScaleType, KeepPieceIndex)
```

### C#

```csharp
void InsertCavity4(
   System.double ScaleFactor_x,
   System.double ScaleFactor_y,
   System.double ScaleFactor_z,
   System.bool IsUniform,
   System.int ScaleType,
   System.int KeepPieceIndex
)
```

### C++/CLI

```cpp
void InsertCavity4(
   System.double ScaleFactor_x,
   System.double ScaleFactor_y,
   System.double ScaleFactor_z,
   System.bool IsUniform,
   System.int ScaleType,
   System.int KeepPieceIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ScaleFactor_x`: Scaling factor in the x direction
- `ScaleFactor_y`: Scaling factor in the y direction
- `ScaleFactor_z`: Scaling factor in the z direction
- `IsUniform`: True to use the first scale argument as the uniform scale, false to not
- `ScaleType`: Type of scaling as defined in [swCavityScaleType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCavityScaleType_e.html)
- `KeepPieceIndex`: Piece to keep if there is ambiguity

## VBA Syntax

See [AssemblyDoc::InsertCavity4](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~InsertCavity4.html).

## Examples

[Insert Cavity (C#)](Insert_Cavity_Example_CSharp.htm)
[Insert Cavity (VB.NET)](Insert_Cavity_Example_VBNET.htm)
[Insert Cavity (VBA)](Insert_Cavity_Example_VB.htm)

## Remarks

This operation is performed in the context of an assembly document. The component being edited in the context of the assembly receives the new cavity feature.

Set the scaleFactor argument as appropriate for your casting material. The scaling factor is expressed as a percentage (+/- 20%) of the size of the cavity part. Pass it in as a value within the range of -20 to +20.

SOLIDWORKS uses the following formula to determine the size of the cavity:

```vb
cavitysize = partsize * (1 + scaleFactor/100)
```

When there is ambiguity in the result of a cut, SOLIDWORKS uses KeepPieceIndex to determine which result to use. You can set this parameter to -1 if there is no ambiguity; otherwise, you should use the index of the result, in the range between 0 and 1 less than the possible number of outcomes.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
