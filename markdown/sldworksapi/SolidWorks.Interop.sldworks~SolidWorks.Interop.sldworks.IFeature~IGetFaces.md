---
title: "IGetFaces Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "IGetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetFaces.html"
---

# IGetFaces Method (IFeature)

Obsolete. Superseded by [IFeature::IGetFaces2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetFaces2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFaces( _
   ByRef FaceCount As System.Integer _
) As Face
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim FaceCount As System.Integer
Dim value As Face

value = instance.IGetFaces(FaceCount)
```

### C#

```csharp
Face IGetFaces(
   out System.int FaceCount
)
```

### C++/CLI

```cpp
Face^ IGetFaces(
   [Out] System.int FaceCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceCount`:

## VBA Syntax

See [Feature::IGetFaces](ms-its:sldworksapivb6.chm::/sldworks~Feature~IGetFaces.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
