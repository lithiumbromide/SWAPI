---
title: "IDeleteBlends3 Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IDeleteBlends3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteBlends3.html"
---

# IDeleteBlends3 Method (IBody2)

Removes a set of fillet faces from a temporary body and heals the body.

## Syntax

### Visual Basic (Declaration)

```vb
Function IDeleteBlends3( _
   ByVal NumOfFaces As System.Integer, _
   ByRef FaceList As Face2, _
   ByVal DoLocalCheck As System.Boolean, _
   ByVal UsePlanarCap As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim NumOfFaces As System.Integer
Dim FaceList As Face2
Dim DoLocalCheck As System.Boolean
Dim UsePlanarCap As System.Boolean
Dim value As System.Boolean

value = instance.IDeleteBlends3(NumOfFaces, FaceList, DoLocalCheck, UsePlanarCap)
```

### C#

```csharp
System.bool IDeleteBlends3(
   System.int NumOfFaces,
   ref Face2 FaceList,
   System.bool DoLocalCheck,
   System.bool UsePlanarCap
)
```

### C++/CLI

```cpp
System.bool IDeleteBlends3(
   System.int NumOfFaces,
   Face2^% FaceList,
   System.bool DoLocalCheck,
   System.bool UsePlanarCap
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`: Number of faces to delete
- `FaceList`: - in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) of size NumOfFaces to delete
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `DoLocalCheck`: True to perform a local check, false to not
- `UsePlanarCap`: True to use planar caps, false to not (see **Remarks**)

### Return Value

True if the set of fillet faces are removed, false if not

## Remarks

Typically when deleting blends, an entire chain of blends are deleted. However, if only a few blends are deleted from a chain of blends and the UsePlanarCap parameter is not set to true, then the resultant body might be invalid.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::DeleteBlends3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteBlends3.html)
[IBody2::DeleteFaces5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFaces5.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
