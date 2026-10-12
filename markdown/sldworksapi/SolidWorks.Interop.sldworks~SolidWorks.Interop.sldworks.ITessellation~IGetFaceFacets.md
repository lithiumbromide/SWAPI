---
title: "IGetFaceFacets Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "IGetFaceFacets"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFaceFacets.html"
---

# IGetFaceFacets Method (ITessellation)

Obsolete. Superseded by [ITessellation::IGetFaceFacets2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITessellation~IGetFaceFacets2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFaceFacets( _
   ByVal FaceObj As Face _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim FaceObj As Face
Dim value As System.Integer

value = instance.IGetFaceFacets(FaceObj)
```

### C#

```csharp
System.int IGetFaceFacets(
   Face FaceObj
)
```

### C++/CLI

```cpp
System.int IGetFaceFacets(
   Face^ FaceObj
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceObj`:

## VBA Syntax

See [Tessellation::IGetFaceFacets](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~IGetFaceFacets.html).

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
