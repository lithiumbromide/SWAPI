---
title: "DeleteBlends3 Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "DeleteBlends3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteBlends3.html"
---

# DeleteBlends3 Method (IBody2)

Removes a set of fillet faces from a temporary body and heals the body.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteBlends3( _
   ByVal FaceList As System.Object, _
   ByVal DoLocalCheck As System.Boolean, _
   ByVal UsePlanarCap As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim FaceList As System.Object
Dim DoLocalCheck As System.Boolean
Dim UsePlanarCap As System.Boolean
Dim value As System.Boolean

value = instance.DeleteBlends3(FaceList, DoLocalCheck, UsePlanarCap)
```

### C#

```csharp
System.bool DeleteBlends3(
   System.object FaceList,
   System.bool DoLocalCheck,
   System.bool UsePlanarCap
)
```

### C++/CLI

```cpp
System.bool DeleteBlends3(
   System.Object^ FaceList,
   System.bool DoLocalCheck,
   System.bool UsePlanarCap
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceList`: List of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to delete
- `DoLocalCheck`: True to perform a local check, false to not
- `UsePlanarCap`: True to use planar caps, false to not (see **Remarks**)

### Return Value

True if the set of fillet faces are removed, false if not

## VBA Syntax

See [Body2::DeleteBlends3](ms-its:sldworksapivb6.chm::/sldworks~Body2~DeleteBlends2.html).

## Examples

[Delete Blended Faces (C#)](Delete_Blended_Faces_Example_CSharp.htm)
[Delete Blended Faces (VB.NET)](Delete_Blended_Faces_Example_VBNET.htm)
[Delete Blended Faces (VBA)](Delete_Blended_Faces_Example_VB.htm)

## Remarks

Typically when deleting blends, an entire chain of blends is deleted. However, if only a few blends are deleted from a chain of blends and the UsePlanarCap parameter is not set to true, then the resultant body might be invalid.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IDeleteBlends3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteBlends3.html)
[IBody5::DeleteFaces5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFaces5.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
