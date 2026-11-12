---
title: "InsertProtrusionSwept Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertProtrusionSwept"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertProtrusionSwept.html"
---

# InsertProtrusionSwept Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertProtrusionSwept](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertProtrusionSwept.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertProtrusionSwept( _
   ByVal Propagate As System.Boolean, _
   ByVal Alignment As System.Boolean, _
   ByVal KeepNormalConstant As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Propagate As System.Boolean
Dim Alignment As System.Boolean
Dim KeepNormalConstant As System.Boolean

instance.InsertProtrusionSwept(Propagate, Alignment, KeepNormalConstant)
```

### C#

```csharp
void InsertProtrusionSwept(
   System.bool Propagate,
   System.bool Alignment,
   System.bool KeepNormalConstant
)
```

### C++/CLI

```cpp
void InsertProtrusionSwept(
   System.bool Propagate,
   System.bool Alignment,
   System.bool KeepNormalConstant
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Propagate`:
- `Alignment`:
- `KeepNormalConstant`:

## VBA Syntax

See [ModelDoc::InsertProtrusionSwept](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertProtrusionSwept.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
