---
title: "IReplaceSurfaces2 Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "IReplaceSurfaces2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IReplaceSurfaces2.html"
---

# IReplaceSurfaces2 Method (IModeler)

Replaces the surfaces of the given faces.

## Syntax

### Visual Basic (Declaration)

```vb
Function IReplaceSurfaces2( _
   ByVal NFaces As System.Integer, _
   ByRef FaceArray As Face2, _
   ByRef NewSurfArray As Surface, _
   ByRef SenseArray As System.Integer, _
   ByVal Tolerance As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim NFaces As System.Integer
Dim FaceArray As Face2
Dim NewSurfArray As Surface
Dim SenseArray As System.Integer
Dim Tolerance As System.Double
Dim value As System.Boolean

value = instance.IReplaceSurfaces2(NFaces, FaceArray, NewSurfArray, SenseArray, Tolerance)
```

### C#

```csharp
System.bool IReplaceSurfaces2(
   System.int NFaces,
   ref Face2 FaceArray,
   ref Surface NewSurfArray,
   ref System.int SenseArray,
   System.double Tolerance
)
```

### C++/CLI

```cpp
System.bool IReplaceSurfaces2(
   System.int NFaces,
   Face2^% FaceArray,
   Surface^% NewSurfArray,
   System.int% SenseArray,
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

See [Modeler::IReplaceSurfaces2](ms-its:sldworksapivb6.chm::/sldworks~Modeler~IReplaceSurfaces2.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::ReplaceSurfaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ReplaceSurfaces.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
