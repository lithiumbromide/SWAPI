---
title: "IGetFaces Method (IMateLoadReference)"
project: "SOLIDWORKS API Help"
interface: "IMateLoadReference"
member: "IGetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference~IGetFaces.html"
---

# IGetFaces Method (IMateLoadReference)

Gets the supplemental faces of the mate associated with the specified component.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFaces( _
   ByVal WhichOne As System.Integer, _
   ByVal FaceCount As System.Integer _
) As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IMateLoadReference
Dim WhichOne As System.Integer
Dim FaceCount As System.Integer
Dim value As Face2

value = instance.IGetFaces(WhichOne, FaceCount)
```

### C#

```csharp
Face2 IGetFaces(
   System.int WhichOne,
   System.int FaceCount
)
```

### C++/CLI

```cpp
Face2^ IGetFaces(
   System.int WhichOne,
   System.int FaceCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichOne`: - 0 = Component1
  - 1 = Component2
- `FaceCount`: Number of supplemental faces

### Return Value

- in-process, unmanaged C++: Pointer to an array of supplemental [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The supplemental faces can belong to one of two components. Specify the component that owns the supplemental faces that you want to access.

Before calling this method, call [IMateLoadReference::GetFacesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateLoadReference~GetFacesCount.html) to determine the size of the array for that method.

## See Also

[IMateLoadReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference.html)
[IMateLoadReference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference_members.html)
[IMateLoadReference::GetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference~GetFaces.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
