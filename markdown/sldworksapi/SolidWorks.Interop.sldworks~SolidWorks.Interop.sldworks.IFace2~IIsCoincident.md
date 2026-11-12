---
title: "IIsCoincident Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IIsCoincident"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IIsCoincident.html"
---

# IIsCoincident Method (IFace2)

Gets whether this face and the specified face, which is located on a different body, are coincident.

## Syntax

### Visual Basic (Declaration)

```vb
Function IIsCoincident( _
   ByVal FaceIn As Face2, _
   ByVal Tolerance As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim FaceIn As Face2
Dim Tolerance As System.Double
Dim value As System.Integer

value = instance.IIsCoincident(FaceIn, Tolerance)
```

### C#

```csharp
System.int IIsCoincident(
   Face2 FaceIn,
   System.double Tolerance
)
```

### C++/CLI

```cpp
System.int IIsCoincident(
   Face2^ FaceIn,
   System.double Tolerance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceIn`: [Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) located on a different body
- `Tolerance`: Tolerance

### Return Value

Result as defined in [swFaceCoincidentResult_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFaceCoincidentResult_e.html) (see Remarks)

## VBA Syntax

See [Face2::IIsCoincident](ms-its:sldworksapivb6.chm::/sldworks~Face2~IIsCoincident.html).

## Remarks

For two faces to be considered coincident, they must have similar corresponding loops and all points on one face must be within the specified tolerance of the other face, and vice versa.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::IsCoincident Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IsCoincident.html)

## Availability

SOLIDWORKS 2007 SP3, Revision Number 15.3
