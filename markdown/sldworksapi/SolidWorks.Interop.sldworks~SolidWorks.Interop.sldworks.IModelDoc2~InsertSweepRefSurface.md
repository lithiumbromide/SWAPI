---
title: "InsertSweepRefSurface Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertSweepRefSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSweepRefSurface.html"
---

# InsertSweepRefSurface Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::InsertProtrusionSwept3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertProtrusionSwept3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertSweepRefSurface( _
   ByVal Propagate As System.Boolean, _
   ByVal TwistCtrlOption As System.Short, _
   ByVal KeepTangency As System.Boolean, _
   ByVal ForceNonRational As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Propagate As System.Boolean
Dim TwistCtrlOption As System.Short
Dim KeepTangency As System.Boolean
Dim ForceNonRational As System.Boolean

instance.InsertSweepRefSurface(Propagate, TwistCtrlOption, KeepTangency, ForceNonRational)
```

### C#

```csharp
void InsertSweepRefSurface(
   System.bool Propagate,
   System.short TwistCtrlOption,
   System.bool KeepTangency,
   System.bool ForceNonRational
)
```

### C++/CLI

```cpp
void InsertSweepRefSurface(
   System.bool Propagate,
   System.short TwistCtrlOption,
   System.bool KeepTangency,
   System.bool ForceNonRational
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Propagate`:
- `TwistCtrlOption`:
- `KeepTangency`:
- `ForceNonRational`:

## VBA Syntax

See [ModelDoc2::InsertSweepRefSurface](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertSweepRefSurface.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
