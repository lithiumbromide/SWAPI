---
title: "MatchedBoolean2 Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "MatchedBoolean2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MatchedBoolean2.html"
---

# MatchedBoolean2 Method (IBody2)

Obsolete. Superseded by [IBody2::MatchedBoolean3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~MatchedBoolean3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function MatchedBoolean2( _
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

value = instance.MatchedBoolean2(OperationType, ToolBody, NumOfMatchingFaces, FaceList1, FaceList2, ErrorCode)
```

### C#

```csharp
System.object MatchedBoolean2(
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
System.Object^ MatchedBoolean2(
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

- `OperationType`:
- `ToolBody`:
- `NumOfMatchingFaces`:
- `FaceList1`:
- `FaceList2`:
- `ErrorCode`:

## VBA Syntax

See [Body2::MatchedBoolean2](ms-its:sldworksapivb6.chm::/sldworks~Body2~MatchedBoolean2.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
