---
title: "IsSuppressed2 Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "IsSuppressed2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsSuppressed2.html"
---

# IsSuppressed2 Method (IFeature)

Gets whether the feature in the specified configurations is suppressed.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsSuppressed2( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim Config_opt As System.Integer
Dim Config_names As System.Object
Dim value As System.Object

value = instance.IsSuppressed2(Config_opt, Config_names)
```

### C#

```csharp
System.object IsSuppressed2(
   System.int Config_opt,
   System.object Config_names
)
```

### C++/CLI

```cpp
System.Object^ IsSuppressed2(
   System.int Config_opt,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Config_opt`: Configuration option as defined by [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_names`: Array of configuration names

### Return Value

Array of Booleans indicating the suppression states for the feature in the specified configurations

## VBA Syntax

See [Feature::IsSuppressed2](ms-its:sldworksapivb6.chm::/sldworks~Feature~IsSuppressed2.html).

## Examples

[Is Feature Suppressed in Configuration (VBA)](Is_Feature_Suppressed_in_Specified_Configurations_Example_VB.htm)
[Get Solid Bodies from Cut-list Folders and Get Custom Properties (C#)](Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_CSharp.htm)
[Get Solid Bodies from Cut-list Folders and Get Custom Properties (VB.NET)](Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_VBNET.htm)
[Get Solid Bodies from Cut-list Folders and Get Custom Properties (VBA)](Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_VB.htm)

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::IIsSuppressed2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IIsSuppressed2.html)
[IFeature::SetSuppression2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetSuppression2.html)
[IFeature::ISetSuppression2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetSuppression2.html)
[IFeature::Visible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Visible.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
