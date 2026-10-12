---
title: "IMatchedBoolean Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IMatchedBoolean"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMatchedBoolean.html"
---

# IMatchedBoolean Method (IBody2)

Obsolete. Superseded by [IBody2::IMatchedBoolean3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IMatchedBoolean3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IMatchedBoolean( _
   ByVal OperationType As System.Integer, _
   ByVal ToolBody As Body2, _
   ByVal NumOfMatchingFaces As System.Integer, _
   ByRef FaceList1 As Face2, _
   ByRef FaceList2 As Face2, _
   ByRef ErrorCode As System.Integer _
) As EnumBodies2
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim OperationType As System.Integer
Dim ToolBody As Body2
Dim NumOfMatchingFaces As System.Integer
Dim FaceList1 As Face2
Dim FaceList2 As Face2
Dim ErrorCode As System.Integer
Dim value As EnumBodies2

value = instance.IMatchedBoolean(OperationType, ToolBody, NumOfMatchingFaces, FaceList1, FaceList2, ErrorCode)
```

### C#

```csharp
EnumBodies2 IMatchedBoolean(
   System.int OperationType,
   Body2 ToolBody,
   System.int NumOfMatchingFaces,
   ref Face2 FaceList1,
   ref Face2 FaceList2,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
EnumBodies2^ IMatchedBoolean(
   System.int OperationType,
   Body2^ ToolBody,
   System.int NumOfMatchingFaces,
   Face2^% FaceList1,
   Face2^% FaceList2,
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

See [Body2::IMatchedBoolean](ms-its:sldworksapivb6.chm::/sldworks~Body2~IMatchedBoolean.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
