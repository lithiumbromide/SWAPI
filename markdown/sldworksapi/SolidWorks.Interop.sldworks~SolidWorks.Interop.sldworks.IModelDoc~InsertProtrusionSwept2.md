---
title: "InsertProtrusionSwept2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertProtrusionSwept2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertProtrusionSwept2.html"
---

# InsertProtrusionSwept2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertProtrusionSwept2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertProtrusionSwept2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertProtrusionSwept2( _
   ByVal Propagate As System.Boolean, _
   ByVal Alignment As System.Boolean, _
   ByVal TwistCtrlOption As System.Short, _
   ByVal KeepTangency As System.Boolean, _
   ByVal ForceNonRational As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Propagate As System.Boolean
Dim Alignment As System.Boolean
Dim TwistCtrlOption As System.Short
Dim KeepTangency As System.Boolean
Dim ForceNonRational As System.Boolean

instance.InsertProtrusionSwept2(Propagate, Alignment, TwistCtrlOption, KeepTangency, ForceNonRational)
```

### C#

```csharp
void InsertProtrusionSwept2(
   System.bool Propagate,
   System.bool Alignment,
   System.short TwistCtrlOption,
   System.bool KeepTangency,
   System.bool ForceNonRational
)
```

### C++/CLI

```cpp
void InsertProtrusionSwept2(
   System.bool Propagate,
   System.bool Alignment,
   System.short TwistCtrlOption,
   System.bool KeepTangency,
   System.bool ForceNonRational
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Propagate`:
- `Alignment`:
- `TwistCtrlOption`:
- `KeepTangency`:
- `ForceNonRational`:

## VBA Syntax

See [ModelDoc::InsertProtrusionSwept2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertProtrusionSwept2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
