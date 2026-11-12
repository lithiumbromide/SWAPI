---
title: "IIsSuppressed2 Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "IIsSuppressed2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IIsSuppressed2.html"
---

# IIsSuppressed2 Method (IFeature)

Gets whether the feature in the specified configurations is suppressed.

## Syntax

### Visual Basic (Declaration)

```vb
Function IIsSuppressed2( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_count As System.Integer, _
   ByRef Config_names As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim Config_opt As System.Integer
Dim Config_count As System.Integer
Dim Config_names As System.String
Dim value As System.Boolean

value = instance.IIsSuppressed2(Config_opt, Config_count, Config_names)
```

### C#

```csharp
System.bool IIsSuppressed2(
   System.int Config_opt,
   System.int Config_count,
   ref System.string Config_names
)
```

### C++/CLI

```cpp
System.bool IIsSuppressed2(
   System.int Config_opt,
   System.int Config_count,
   System.String^% Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Config_opt`: Configuration option as defined by [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_count`: Number of configurations in this feature
- `Config_names`: Array of configuration names

### Return Value

Array of the suppression states for the feature in the specified configurations

## VBA Syntax

See [Feature::IIsSuppressed2](ms-its:sldworksapivb6.chm::/sldworks~Feature~IIsSuppressed2.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::ISetSuppression2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetSuppression2.html)
[IFeature::IsSuppressed2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsSuppressed2.html)
[IFeature::SetSuppression2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetSuppression2.html)
[IFeature::Visible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Visible.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
