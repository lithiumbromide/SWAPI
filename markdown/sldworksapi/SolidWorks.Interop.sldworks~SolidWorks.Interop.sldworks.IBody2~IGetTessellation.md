---
title: "IGetTessellation Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IGetTessellation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetTessellation.html"
---

# IGetTessellation Method (IBody2)

Gets the [ITessellation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITessellation.html) object.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTessellation( _
   ByVal NumOfFaces As System.Integer, _
   ByRef FaceList As Face2 _
) As Tessellation
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim NumOfFaces As System.Integer
Dim FaceList As Face2
Dim value As Tessellation

value = instance.IGetTessellation(NumOfFaces, FaceList)
```

### C#

```csharp
Tessellation IGetTessellation(
   System.int NumOfFaces,
   ref Face2 FaceList
)
```

### C++/CLI

```cpp
Tessellation^ IGetTessellation(
   System.int NumOfFaces,
   Face2^% FaceList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`: Number of faces to tessellate
- `FaceList`: Array of faces to tessellate; if this is NULL, then SOLIDWORKS will tessellate the body

### Return Value

Pointer to the [ITessellation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITessellation.html) object

## VBA Syntax

See [Body2::IGetTessellation](ms-its:sldworksapivb6.chm::/sldworks~Body2~IGetTessellation.html).

## Examples

[Tessellate a Body (C#)](Tessellate_a_Body_Example_CSharp.htm)

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::GetTessellation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTessellation.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
