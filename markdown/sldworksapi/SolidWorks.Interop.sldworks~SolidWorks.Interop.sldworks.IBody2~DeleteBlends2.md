---
title: "DeleteBlends2 Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "DeleteBlends2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteBlends2.html"
---

# DeleteBlends2 Method (IBody2)

Obsolete. Superseded by [IBody2::DeleteBlends3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~DeleteBlends3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteBlends2( _
   ByVal NumOfFaces As System.Integer, _
   ByVal FaceList As System.Object, _
   ByVal DoLocalCheck As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim NumOfFaces As System.Integer
Dim FaceList As System.Object
Dim DoLocalCheck As System.Boolean
Dim value As System.Boolean

value = instance.DeleteBlends2(NumOfFaces, FaceList, DoLocalCheck)
```

### C#

```csharp
System.bool DeleteBlends2(
   System.int NumOfFaces,
   System.object FaceList,
   System.bool DoLocalCheck
)
```

### C++/CLI

```cpp
System.bool DeleteBlends2(
   System.int NumOfFaces,
   System.Object^ FaceList,
   System.bool DoLocalCheck
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`: Number of faces to delete
- `FaceList`: List of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to delete
- `DoLocalCheck`: True to perform a local check, false to not

### Return Value

True if the set of fillet faces are removed, false if not

## VBA Syntax

See [Body2::DeleteBlends2](ms-its:sldworksapivb6.chm::/sldworks~Body2~DeleteBlends2.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IDeleteBlends2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteBlends2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
