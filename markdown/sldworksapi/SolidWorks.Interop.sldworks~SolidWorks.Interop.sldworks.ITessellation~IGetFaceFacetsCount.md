---
title: "IGetFaceFacetsCount Method (ITessellation)"
project: "SOLIDWORKS API Help"
interface: "ITessellation"
member: "IGetFaceFacetsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~IGetFaceFacetsCount.html"
---

# IGetFaceFacetsCount Method (ITessellation)

Obsolete. Superseded by [ITessellation::IGetFaceFacetsCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITessellation~IGetFaceFacetsCount2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFaceFacetsCount( _
   ByVal FaceObj As Face _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITessellation
Dim FaceObj As Face
Dim value As System.Integer

value = instance.IGetFaceFacetsCount(FaceObj)
```

### C#

```csharp
System.int IGetFaceFacetsCount(
   Face FaceObj
)
```

### C++/CLI

```cpp
System.int IGetFaceFacetsCount(
   Face^ FaceObj
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceObj`:

## VBA Syntax

See [Tessellation::IGetFaceFacetsCount](ms-its:sldworksapivb6.chm::/sldworks~Tessellation~IGetFaceFacetsCount.html).

## See Also

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.html)
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.html)
