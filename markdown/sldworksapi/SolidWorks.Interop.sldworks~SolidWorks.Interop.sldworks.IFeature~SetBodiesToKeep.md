---
title: "SetBodiesToKeep Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "SetBodiesToKeep"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetBodiesToKeep.html"
---

# SetBodiesToKeep Method (IFeature)

Set the bodies to keep and their configurations for features that create multiple bodies in parts and assemblies.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetBodiesToKeep( _
   ByVal AllBodies As System.Boolean, _
   ByVal BodiesToKeep As System.Object, _
   ByVal ConfigOption As System.Integer, _
   ByVal ConfigNames As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim AllBodies As System.Boolean
Dim BodiesToKeep As System.Object
Dim ConfigOption As System.Integer
Dim ConfigNames As System.Object

instance.SetBodiesToKeep(AllBodies, BodiesToKeep, ConfigOption, ConfigNames)
```

### C#

```csharp
void SetBodiesToKeep(
   System.bool AllBodies,
   System.object BodiesToKeep,
   System.int ConfigOption,
   System.object ConfigNames
)
```

### C++/CLI

```cpp
void SetBodiesToKeep(
   System.bool AllBodies,
   System.Object^ BodiesToKeep,
   System.int ConfigOption,
   System.Object^ ConfigNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AllBodies`: True to keep all bodies, false to not
- `BodiesToKeep`: Array of bodies to keep
- `ConfigOption`: Configuration options as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `ConfigNames`: Array of configuration names

## VBA Syntax

See [Feature::SetBodiesToKeep](ms-its:sldworksapivb6.chm::/sldworks~Feature~SetBodiesToKeep.html).

## Examples

[Cut Body and Keep All Bodies (C#)](Cut_Body_and_Keep_All_Bodies_Example_CSharp.htm)
[Cut Body and Keep All Bodies (VB.NET)](Cut_Body_and_Keep_All_Bodies_Example_VBNET.htm)
[Cut Body and Keep All Bodies (VBA)](Cut_Body_and_Keep_All_Bodies_Example_VB.htm)

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IAssemblyDoc PromptBodiesToKeepNotify Event](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_PromptBodiesToKeepNotifyEventHandler.html)
[IPartDoc PromptBodiesToKeepNotify Event](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_PromptBodiesToKeepNotifyEventHandler.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
