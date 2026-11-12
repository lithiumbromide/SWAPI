---
title: "IOperations2 Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "IOperations2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IOperations2.html"
---

# IOperations2 Method (IBody)

Obsolete. Superseded by [IBody2::IOperations2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IOperations2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IOperations2( _
   ByVal OperationType As System.Integer, _
   ByVal ToolBody As Body, _
   ByRef ErrorCode As System.Integer _
) As EnumBodies
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim OperationType As System.Integer
Dim ToolBody As Body
Dim ErrorCode As System.Integer
Dim value As EnumBodies

value = instance.IOperations2(OperationType, ToolBody, ErrorCode)
```

### C#

```csharp
EnumBodies IOperations2(
   System.int OperationType,
   Body ToolBody,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
EnumBodies^ IOperations2(
   System.int OperationType,
   Body^ ToolBody,
   [Out] System.int ErrorCode
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OperationType`:
- `ToolBody`:
- `ErrorCode`:

## VBA Syntax

See [Body::IOperations2](ms-its:sldworksapivb6.chm::/sldworks~Body~IOperations2.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
