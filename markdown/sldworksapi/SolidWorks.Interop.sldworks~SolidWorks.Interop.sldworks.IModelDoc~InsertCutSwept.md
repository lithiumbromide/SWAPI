---
title: "InsertCutSwept Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertCutSwept"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertCutSwept.html"
---

# InsertCutSwept Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertCutSwept](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertCutSwept.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertCutSwept( _
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

instance.InsertCutSwept(Propagate, Alignment, KeepNormalConstant)
```

### C#

```csharp
void InsertCutSwept(
   System.bool Propagate,
   System.bool Alignment,
   System.bool KeepNormalConstant
)
```

### C++/CLI

```cpp
void InsertCutSwept(
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

See [ModelDoc::InsertCutSwept](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertCutSwept.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
