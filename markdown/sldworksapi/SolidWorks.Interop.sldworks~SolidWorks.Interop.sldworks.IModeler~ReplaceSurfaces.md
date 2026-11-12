---
title: "ReplaceSurfaces Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ReplaceSurfaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ReplaceSurfaces.html"
---

# ReplaceSurfaces Method (IModeler)

Replaces the surfaces of the given faces.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReplaceSurfaces( _
   ByVal NFaces As System.Integer, _
   ByVal FaceArray As System.Object, _
   ByVal NewSurfArray As System.Object, _
   ByVal SenseArray As System.Object, _
   ByVal Tolerance As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim NFaces As System.Integer
Dim FaceArray As System.Object
Dim NewSurfArray As System.Object
Dim SenseArray As System.Object
Dim Tolerance As System.Double
Dim value As System.Boolean

value = instance.ReplaceSurfaces(NFaces, FaceArray, NewSurfArray, SenseArray, Tolerance)
```

### C#

```csharp
System.bool ReplaceSurfaces(
   System.int NFaces,
   System.object FaceArray,
   System.object NewSurfArray,
   System.object SenseArray,
   System.double Tolerance
)
```

### C++/CLI

```cpp
System.bool ReplaceSurfaces(
   System.int NFaces,
   System.Object^ FaceArray,
   System.Object^ NewSurfArray,
   System.Object^ SenseArray,
   System.double Tolerance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NFaces`: Number of faces to have surfaces replaced
- `FaceArray`: Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to have the surfaces replaced
- `NewSurfArray`: Array of [surfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html) to be replaced in these faces
- `SenseArray`: Array of the senses of each surface in NewSurfArray
- `Tolerance`: Tolerance

### Return Value

True if operation is successful, false if not

## VBA Syntax

See [Modeler::ReplaceSurfaces](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ReplaceSurfaces.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::IReplaceSurfaces2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IReplaceSurfaces2.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 0.0
