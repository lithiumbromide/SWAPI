---
title: "IOperations Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "IOperations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IOperations.html"
---

# IOperations Method (IBody)

Obsolete. Superseded by [IBody2::IOperations2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IOperations2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IOperations( _
   ByVal OperationType As System.Integer, _
   ByVal ToolBody As Body, _
   ByVal NumMaxSections As System.Integer, _
   ByRef ResultingBodies As Body _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim OperationType As System.Integer
Dim ToolBody As Body
Dim NumMaxSections As System.Integer
Dim ResultingBodies As Body
Dim value As System.Integer

value = instance.IOperations(OperationType, ToolBody, NumMaxSections, ResultingBodies)
```

### C#

```csharp
System.int IOperations(
   System.int OperationType,
   Body ToolBody,
   System.int NumMaxSections,
   ref Body ResultingBodies
)
```

### C++/CLI

```cpp
System.int IOperations(
   System.int OperationType,
   Body^ ToolBody,
   System.int NumMaxSections,
   Body^% ResultingBodies
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OperationType`:
- `ToolBody`:
- `NumMaxSections`:
- `ResultingBodies`:

## VBA Syntax

See [Body::IOperations](ms-its:sldworksapivb6.chm::/sldworks~Body~IOperations.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
