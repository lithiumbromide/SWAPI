---
title: "IGetFaces Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IGetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFaces.html"
---

# IGetFaces Method (IBody2)

Gets all of the faces on the body.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFaces( _
   ByVal Count As System.Integer _
) As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Count As System.Integer
Dim value As Face2

value = instance.IGetFaces(Count)
```

### C#

```csharp
Face2 IGetFaces(
   System.int Count
)
```

### C++/CLI

```cpp
Face2^ IGetFaces(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of faces on the body (see **Remarks**)

### Return Value

- in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) on the body
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IBody2::GetFaceCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetFaceCount.html) to get the value of Count.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::GetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFaces.html)
[IBody2::IGetFirstFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFirstFace.html)
[IBody2::GetFirstFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFirstFace.html)

## Availability

SOLIDWORKS 2008 SP1, Revision Number 16.1
