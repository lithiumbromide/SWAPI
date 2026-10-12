---
title: "MatchedBoolean3 Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "MatchedBoolean3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MatchedBoolean3.html"
---

# MatchedBoolean3 Method (IBody2)

Obsolete. Superseded by [IBody2::MatchedBoolean4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~MatchedBoolean4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function MatchedBoolean3( _
   ByVal OperationType As System.Integer, _
   ByVal ToolBody As System.Object, _
   ByVal NumOfMatchingFaces As System.Integer, _
   ByVal FaceList1 As System.Object, _
   ByVal FaceList2 As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim OperationType As System.Integer
Dim ToolBody As System.Object
Dim NumOfMatchingFaces As System.Integer
Dim FaceList1 As System.Object
Dim FaceList2 As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.MatchedBoolean3(OperationType, ToolBody, NumOfMatchingFaces, FaceList1, FaceList2, ErrorCode)
```

### C#

```csharp
System.object MatchedBoolean3(
   System.int OperationType,
   System.object ToolBody,
   System.int NumOfMatchingFaces,
   System.object FaceList1,
   System.object FaceList2,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ MatchedBoolean3(
   System.int OperationType,
   System.Object^ ToolBody,
   System.int NumOfMatchingFaces,
   System.Object^ FaceList1,
   System.Object^ FaceList2,
   [Out] System.int ErrorCode
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OperationType`: One of the following operation types:

  - SWBODYADD
  - SWBODYCUT
  - SWBODYINTERSECT
- `ToolBody`: Array of bodies
- `NumOfMatchingFaces`: Number of matching faces
- `FaceList1`: First face list (see Remarks)
- `FaceList2`: Second face list (see Remarks)
- `ErrorCode`: Error indicated as defined in [swBodyOperationError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBodyOperationError_e.html)

### Return Value

Array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) formed by the operation

## VBA Syntax

See [Body2::MatchedBoolean3](ms-its:sldworksapivb6.chm::/sldworks~Body2~MatchedBoolean3.html).

## Remarks

The concept of match means that the caller tells the boolean operator beforehand which faces can be considered to coincide. Basically, the caller performs part of the boolean operation.

Sometimes the application knows that two faces match because of the way the bodies are constructed; i.e., the application knows which faces are intended to match.

Having a list of matching face pairs may allow the matched boolean operator to resolve other geometric operations that otherwise it would not be able to work out. In general, providing matched faces speeds up the boolean operation and makes results more reliable.

The arguments FaceList1 and FaceList2 arguments can be empty lists. If matching face pairs are passed in, these faces must match such that:

- the surface geometry is coinciding.
- for each edge in a face, there is an edge in the other face that coincides

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IMatchedBoolean3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMatchedBoolean3.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
