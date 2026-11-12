---
title: "InsertSweepRefSurface Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertSweepRefSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertSweepRefSurface.html"
---

# InsertSweepRefSurface Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertSweepRefSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertSweepRefSurface.html).

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
Dim instance As IModelDoc
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

See [ModelDoc::InsertSweepRefSurface](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertSweepRefSurface.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
