---
title: "MatchedBoolean Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "MatchedBoolean"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~MatchedBoolean.html"
---

# MatchedBoolean Method (IBody)

Obsolete. Superseded by [IBody2::MatchedBoolean3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~MatchedBoolean3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function MatchedBoolean( _
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
Dim instance As IBody
Dim OperationType As System.Integer
Dim ToolBody As System.Object
Dim NumOfMatchingFaces As System.Integer
Dim FaceList1 As System.Object
Dim FaceList2 As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.MatchedBoolean(OperationType, ToolBody, NumOfMatchingFaces, FaceList1, FaceList2, ErrorCode)
```

### C#

```csharp
System.object MatchedBoolean(
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
System.Object^ MatchedBoolean(
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

See [Body::MatchedBoolean](ms-its:sldworksapivb6.chm::/sldworks~Body~MatchedBoolean.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
