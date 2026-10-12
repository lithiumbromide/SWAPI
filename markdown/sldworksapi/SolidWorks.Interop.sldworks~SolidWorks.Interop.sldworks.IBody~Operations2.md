---
title: "Operations2 Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "Operations2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~Operations2.html"
---

# Operations2 Method (IBody)

Obsolete. Superseded by [IBody2::Operations2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~Operations2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Operations2( _
   ByVal OperationType As System.Integer, _
   ByVal ToolBody As System.Object, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim OperationType As System.Integer
Dim ToolBody As System.Object
Dim ErrorCode As System.Integer
Dim value As System.Object

value = instance.Operations2(OperationType, ToolBody, ErrorCode)
```

### C#

```csharp
System.object Operations2(
   System.int OperationType,
   System.object ToolBody,
   out System.int ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ Operations2(
   System.int OperationType,
   System.Object^ ToolBody,
   [Out] System.int ErrorCode
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OperationType`:
- `ToolBody`:
- `ErrorCode`:

## VBA Syntax

See [Body::Operations2](ms-its:sldworksapivb6.chm::/sldworks~Body~Operations2.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
