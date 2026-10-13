---
title: "SetSpeedPakConfigurations Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "SetSpeedPakConfigurations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetSpeedPakConfigurations.html"
---

# SetSpeedPakConfigurations Method (IAssemblyDoc)

Sets the configurations in the selected subassemblies to which to apply SpeedPak in this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSpeedPakConfigurations( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Config_opt As System.Integer
Dim Config_names As System.Object
Dim value As System.Boolean

value = instance.SetSpeedPakConfigurations(Config_opt, Config_names)
```

### C#

```csharp
System.bool SetSpeedPakConfigurations(
   System.int Config_opt,
   System.object Config_names
)
```

### C++/CLI

```cpp
System.bool SetSpeedPakConfigurations(
   System.int Config_opt,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Config_opt`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html) (see **Remarks**)
- `Config_names`: Array of the names of the configurations in the selected subassemblies to which to apply SpeedPak; valid only if Config_opt = swInConfigurationOpts_e.swSpecifyConfiguration (see **Remarks**)

### Return Value

True if the specified configurations in the selected subassemblies are applied SpeedPak, false if not

## VBA Syntax

See [AssemblyDoc::SetSpeedPakConfigurations](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~SetSpeedPakConfigurations.html).

## Remarks

Valid option for Config_opt is:

- swInConfigurationOpts_e.swAllConfiguration,
- swInConfigurationOpts_e.swSpecifyConfiguration, or
- swInConfigurationOpts_e.swThisConfiguration

If Config_names = swInConfigurationOpts_e.swAllConfiguration or swInConfigurationOpts_e.swThisConfiguration, then pass Nothing or null.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::CreateSpeedPak Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateSpeedPak.html)
[IAssemblyDoc::SetSpeedPakToParent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetSpeedPakToParent.html)
[IAssemblyDoc::UpdateSpeedPak Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateSpeedPak.html)
[IAssemblyDoc::UseSpeedPak Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UseSpeedPak.html)
[IAssemblyDoc::IsSpeedPak Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSpeedPak.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
