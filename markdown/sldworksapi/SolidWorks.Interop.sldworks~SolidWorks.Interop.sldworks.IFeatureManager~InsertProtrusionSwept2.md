---
title: "InsertProtrusionSwept2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertProtrusionSwept2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertProtrusionSwept2.html"
---

# InsertProtrusionSwept2 Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertProtusionSwept3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertProtrusionSwept3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertProtrusionSwept2( _
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
   ByVal ThinType As System.Short, _
   ByVal PathAlign As System.Short, _
   ByVal Merge As System.Boolean, _
   ByVal UseFeatScope As System.Boolean, _
   ByVal UseAutoSelect As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
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
Dim PathAlign As System.Short
Dim Merge As System.Boolean
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim value As Feature

value = instance.InsertProtrusionSwept2(Propagate, Alignment, TwistCtrlOption, KeepTangency, ForceNonRational, StartMatchingType, EndMatchingType, IsThinBody, Thickness1, Thickness2, ThinType, PathAlign, Merge, UseFeatScope, UseAutoSelect)
```

### C#

```csharp
Feature InsertProtrusionSwept2(
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
   System.short ThinType,
   System.short PathAlign,
   System.bool Merge,
   System.bool UseFeatScope,
   System.bool UseAutoSelect
)
```

### C++/CLI

```cpp
Feature^ InsertProtrusionSwept2(
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
   System.short ThinType,
   System.short PathAlign,
   System.bool Merge,
   System.bool UseFeatScope,
   System.bool UseAutoSelect
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
- `PathAlign`:
- `Merge`:
- `UseFeatScope`:
- `UseAutoSelect`:

## VBA Syntax

See [FeatureManager::InsertProtrusionSwept2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertProtrusionSwept2.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
