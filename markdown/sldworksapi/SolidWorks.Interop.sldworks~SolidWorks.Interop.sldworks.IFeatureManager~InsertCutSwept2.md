---
title: "InsertCutSwept2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertCutSwept2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCutSwept2.html"
---

# InsertCutSwept2 Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertCutSwept3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertCutSwept3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertCutSwept2( _
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
Dim UseFeatScope As System.Boolean
Dim UseAutoSelect As System.Boolean
Dim value As Feature

value = instance.InsertCutSwept2(Propagate, Alignment, TwistCtrlOption, KeepTangency, ForceNonRational, StartMatchingType, EndMatchingType, IsThinBody, Thickness1, Thickness2, ThinType, PathAlign, UseFeatScope, UseAutoSelect)
```

### C#

```csharp
Feature InsertCutSwept2(
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
   System.bool UseFeatScope,
   System.bool UseAutoSelect
)
```

### C++/CLI

```cpp
Feature^ InsertCutSwept2(
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
- `UseFeatScope`:
- `UseAutoSelect`:

## VBA Syntax

See [FeatureManager::InsertCutSwept2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertCutSwept2.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
