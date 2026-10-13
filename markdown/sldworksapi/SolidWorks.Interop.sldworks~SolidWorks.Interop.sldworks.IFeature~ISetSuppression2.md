---
title: "ISetSuppression2 Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "ISetSuppression2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetSuppression2.html"
---

# ISetSuppression2 Method (IFeature)

Sets the suppression state of this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetSuppression2( _
   ByVal SuppressionState As System.Integer, _
   ByVal Config_opt As System.Integer, _
   ByVal Config_count As System.Integer, _
   ByRef Config_names As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim SuppressionState As System.Integer
Dim Config_opt As System.Integer
Dim Config_count As System.Integer
Dim Config_names As System.String
Dim value As System.Boolean

value = instance.ISetSuppression2(SuppressionState, Config_opt, Config_count, Config_names)
```

### C#

```csharp
System.bool ISetSuppression2(
   System.int SuppressionState,
   System.int Config_opt,
   System.int Config_count,
   ref System.string Config_names
)
```

### C++/CLI

```cpp
System.bool ISetSuppression2(
   System.int SuppressionState,
   System.int Config_opt,
   System.int Config_count,
   System.String^% Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SuppressionState`: Suppression state as defined in [swFeatureSuppressionAction_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureSuppressionAction_e.html)
- `Config_opt`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_count`: Number of configurations
- `Config_names`: Array of configuration names of size Config_count

### Return Value

True if feature is suppressed, false if not

## VBA Syntax

See [Feature::ISetSuppression2](ms-its:sldworksapivb6.chm::/sldworks~Feature~ISetSuppression2.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::SetSuppression2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetSuppression2.html)
[IFeature::IsSuppressed2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsSuppressed2.html)
[IFeature::IIsSuppressed2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IIsSuppressed2.html)
[IFeature::Visible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Visible.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
