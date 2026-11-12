---
title: "IMatchedBoolean Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "IMatchedBoolean"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IMatchedBoolean.html"
---

# IMatchedBoolean Method (IBody)

Obsolete. Superseded by [IBody2::IMatchedBoolean3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IMatchedBoolean3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IMatchedBoolean( _
   ByVal OperationType As System.Integer, _
   ByVal ToolBody As Body, _
   ByVal NumOfMatchingFaces As System.Integer, _
   ByRef FaceList1 As Face, _
   ByRef FaceList2 As Face, _
   ByRef ErrorCode As System.Integer _
) As EnumBodies
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim OperationType As System.Integer
Dim ToolBody As Body
Dim NumOfMatchingFaces As System.Integer
Dim FaceList1 As Face
Dim FaceList2 As Face
Dim ErrorCode As System.Integer
Dim value As EnumBodies

value = instance.IMatchedBoolean(OperationType, ToolBody, NumOfMatchingFaces, FaceList1, FaceList2, ErrorCode)
```

### C#

```csharp
EnumBodies IMatchedBoolean(
   System.int OperationType,
   Body ToolBody,
   System.int NumOfMatchingFaces,
   ref Face FaceList1,
   ref Face FaceList2,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
EnumBodies^ IMatchedBoolean(
   System.int OperationType,
   Body^ ToolBody,
   System.int NumOfMatchingFaces,
   Face^% FaceList1,
   Face^% FaceList2,
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

See [Body::IMatchedBoolean](ms-its:sldworksapivb6.chm::/sldworks~Body~IMatchedBoolean.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
