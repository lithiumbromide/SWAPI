---
title: "Operations Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "Operations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Operations.html"
---

# Operations Method (IBody2)

Obsolete. Superseded by [IBody2::Operations2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~Operations2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Operations( _
   ByVal OperationType As System.Integer, _
   ByVal ToolBody As System.Object, _
   ByVal NumMaxSections As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim OperationType As System.Integer
Dim ToolBody As System.Object
Dim NumMaxSections As System.Integer
Dim value As System.Object

value = instance.Operations(OperationType, ToolBody, NumMaxSections)
```

### C#

```csharp
System.object Operations(
   System.int OperationType,
   System.object ToolBody,
   System.int NumMaxSections
)
```

### C++/CLI

```cpp
System.Object^ Operations(
   System.int OperationType,
   System.Object^ ToolBody,
   System.int NumMaxSections
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OperationType`:
- `ToolBody`:
- `NumMaxSections`:

## VBA Syntax

See [Body2::Operations](ms-its:sldworksapivb6.chm::/sldworks~Body2~Operations.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
