---
title: "Operations Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "Operations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~Operations.html"
---

# Operations Method (IBody)

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
Dim instance As IBody
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

See [Body::Operations](ms-its:sldworksapivb6.chm::/sldworks~Body~Operations.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
