---
title: "InsertCutSwept Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertCutSwept"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCutSwept.html"
---

# InsertCutSwept Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::InsertCutSwept3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertCutSwept3.html).

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
Dim instance As IModelDoc2
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

See [ModelDoc2::InsertCutSwept](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertCutSwept.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
