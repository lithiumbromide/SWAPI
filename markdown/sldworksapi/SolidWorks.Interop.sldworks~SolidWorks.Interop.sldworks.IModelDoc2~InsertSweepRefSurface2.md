---
title: "InsertSweepRefSurface2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertSweepRefSurface2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSweepRefSurface2.html"
---

# InsertSweepRefSurface2 Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::InsertProtrusionSwept3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertProtrusionSwept3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertSweepRefSurface2( _
   ByVal Propagate As System.Boolean, _
   ByVal TwistCtrlOption As System.Short, _
   ByVal KeepTangency As System.Boolean, _
   ByVal ForceNonRational As System.Boolean, _
   ByVal StartMatchingType As System.Short, _
   ByVal EndMatchingType As System.Short _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Propagate As System.Boolean
Dim TwistCtrlOption As System.Short
Dim KeepTangency As System.Boolean
Dim ForceNonRational As System.Boolean
Dim StartMatchingType As System.Short
Dim EndMatchingType As System.Short

instance.InsertSweepRefSurface2(Propagate, TwistCtrlOption, KeepTangency, ForceNonRational, StartMatchingType, EndMatchingType)
```

### C#

```csharp
void InsertSweepRefSurface2(
   System.bool Propagate,
   System.short TwistCtrlOption,
   System.bool KeepTangency,
   System.bool ForceNonRational,
   System.short StartMatchingType,
   System.short EndMatchingType
)
```

### C++/CLI

```cpp
void InsertSweepRefSurface2(
   System.bool Propagate,
   System.short TwistCtrlOption,
   System.bool KeepTangency,
   System.bool ForceNonRational,
   System.short StartMatchingType,
   System.short EndMatchingType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Propagate`:
- `TwistCtrlOption`:
- `KeepTangency`:
- `ForceNonRational`:
- `StartMatchingType`:
- `EndMatchingType`:

## VBA Syntax

See [ModelDoc2::InsertSweepRefSurface2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertSweepRefSurface2.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
