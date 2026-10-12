---
title: "InsertProtrusionSwept Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertProtrusionSwept"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertProtrusionSwept.html"
---

# InsertProtrusionSwept Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::InsertProtrusionSwept3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertProtrusionSwept3.html).

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
Dim instance As IModelDoc2
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

See [ModelDoc2::InsertProtrusionSwept](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertProtrusionSwept.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
