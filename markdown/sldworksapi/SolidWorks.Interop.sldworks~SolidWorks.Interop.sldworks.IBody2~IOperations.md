---
title: "IOperations Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IOperations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IOperations.html"
---

# IOperations Method (IBody2)

Obsolete. Superseded by [IBody2::Operations2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IOperations2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IOperations( _
   ByVal OperationType As System.Integer, _
   ByVal ToolBody As Body2, _
   ByVal NumMaxSections As System.Integer, _
   ByRef ResultingBodies As Body2 _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim OperationType As System.Integer
Dim ToolBody As Body2
Dim NumMaxSections As System.Integer
Dim ResultingBodies As Body2
Dim value As System.Integer

value = instance.IOperations(OperationType, ToolBody, NumMaxSections, ResultingBodies)
```

### C#

```csharp
System.int IOperations(
   System.int OperationType,
   Body2 ToolBody,
   System.int NumMaxSections,
   ref Body2 ResultingBodies
)
```

### C++/CLI

```cpp
System.int IOperations(
   System.int OperationType,
   Body2^ ToolBody,
   System.int NumMaxSections,
   Body2^% ResultingBodies
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OperationType`:
- `ToolBody`:
- `NumMaxSections`:
- `ResultingBodies`:

## VBA Syntax

See [Body2::IOperations](ms-its:sldworksapivb6.chm::/sldworks~Body2~IOperations.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
