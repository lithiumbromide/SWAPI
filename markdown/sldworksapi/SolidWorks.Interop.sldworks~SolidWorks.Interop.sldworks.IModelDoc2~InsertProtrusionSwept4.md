---
title: "InsertProtrusionSwept4 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertProtrusionSwept4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertProtrusionSwept4.html"
---

# InsertProtrusionSwept4 Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::InsertProtrusionSwept3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertProtrusionSwept3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertProtrusionSwept4( _
   ByVal Propagate As System.Boolean, _
   ByVal Alignment As System.Boolean, _
   ByVal TwistCtrlOption As System.Short, _
   ByVal KeepTangency As System.Boolean, _
   ByVal ForceNonRational As System.Boolean, _
   ByVal StartMatchingType As System.Short, _
   ByVal EndMatchingType As System.Short, _
   ByVal IsThinBody As System.Boolean, _
   ByVal Thickness1 As System.Double, _
   ByVal Thickness2 As System.Double, _
   ByVal ThinType As System.Short _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Propagate As System.Boolean
Dim Alignment As System.Boolean
Dim TwistCtrlOption As System.Short
Dim KeepTangency As System.Boolean
Dim ForceNonRational As System.Boolean
Dim StartMatchingType As System.Short
Dim EndMatchingType As System.Short
Dim IsThinBody As System.Boolean
Dim Thickness1 As System.Double
Dim Thickness2 As System.Double
Dim ThinType As System.Short

instance.InsertProtrusionSwept4(Propagate, Alignment, TwistCtrlOption, KeepTangency, ForceNonRational, StartMatchingType, EndMatchingType, IsThinBody, Thickness1, Thickness2, ThinType)
```

### C#

```csharp
void InsertProtrusionSwept4(
   System.bool Propagate,
   System.bool Alignment,
   System.short TwistCtrlOption,
   System.bool KeepTangency,
   System.bool ForceNonRational,
   System.short StartMatchingType,
   System.short EndMatchingType,
   System.bool IsThinBody,
   System.double Thickness1,
   System.double Thickness2,
   System.short ThinType
)
```

### C++/CLI

```cpp
void InsertProtrusionSwept4(
   System.bool Propagate,
   System.bool Alignment,
   System.short TwistCtrlOption,
   System.bool KeepTangency,
   System.bool ForceNonRational,
   System.short StartMatchingType,
   System.short EndMatchingType,
   System.bool IsThinBody,
   System.double Thickness1,
   System.double Thickness2,
   System.short ThinType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Propagate`:
- `Alignment`:
- `TwistCtrlOption`:
- `KeepTangency`:
- `ForceNonRational`:
- `StartMatchingType`:
- `EndMatchingType`:
- `IsThinBody`:
- `Thickness1`:
- `Thickness2`:
- `ThinType`:

## VBA Syntax

See [ModelDoc2::InsertProtrusionSwept4](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertProtrusionSwept4.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
