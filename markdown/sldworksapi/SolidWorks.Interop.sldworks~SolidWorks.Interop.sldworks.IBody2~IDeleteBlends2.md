---
title: "IDeleteBlends2 Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IDeleteBlends2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteBlends2.html"
---

# IDeleteBlends2 Method (IBody2)

Obsolete. Superseded by [IBody2::DeleteBlends3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IDeleteBlends3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IDeleteBlends2( _
   ByVal NumOfFaces As System.Integer, _
   ByRef FaceList As Face2, _
   ByVal DoLocalCheck As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim NumOfFaces As System.Integer
Dim FaceList As Face2
Dim DoLocalCheck As System.Boolean
Dim value As System.Boolean

value = instance.IDeleteBlends2(NumOfFaces, FaceList, DoLocalCheck)
```

### C#

```csharp
System.bool IDeleteBlends2(
   System.int NumOfFaces,
   ref Face2 FaceList,
   System.bool DoLocalCheck
)
```

### C++/CLI

```cpp
System.bool IDeleteBlends2(
   System.int NumOfFaces,
   Face2^% FaceList,
   System.bool DoLocalCheck
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`: Number of faces to delete
- `FaceList`: - in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) of size NumOfFaces to delete
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `DoLocalCheck`: True to perform a local check, false if not

### Return Value

True if a set of fillet faces are removed, false if not

## VBA Syntax

See [Body2::IDeleteBlends2](ms-its:sldworksapivb6.chm::/sldworks~Body2~IDeleteBlends2.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::DeleteBlends2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteBlends2.html)
[IBody2::DeleteFaces5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFaces5.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
