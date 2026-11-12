---
title: "SetOverrideOptions Method (IMassProperty2)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty2"
member: "SetOverrideOptions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~SetOverrideOptions.html"
---

# SetOverrideOptions Method (IMassProperty2)

Sets the mass property override options for the selected bodies/components.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetOverrideOptions( _
   ByVal Options As System.Object, _
   ByVal Config_option As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty2
Dim Options As System.Object
Dim Config_option As System.Integer
Dim Config_names As System.Object
Dim value As System.Boolean

value = instance.SetOverrideOptions(Options, Config_option, Config_names)
```

### C#

```csharp
System.bool SetOverrideOptions(
   System.object Options,
   System.int Config_option,
   System.object Config_names
)
```

### C++/CLI

```cpp
System.bool SetOverrideOptions(
   System.Object^ Options,
   System.int Config_option,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Options`: [IMassPropertyOverrideOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions.html)
- `Config_option`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_names`: Array of configuration names; valid only if Config_option = swInConfigurationOpts_e.swSpecifyConfiguration

### Return Value

True if the mass property override options are set successfully, false if not

## VBA Syntax

See [MassProperty2::SetOverrideOptions](ms-its:sldworksapivb6.chm::/sldworks~MassProperty2~SetOverrideOptions.html).

## Examples

See the [IMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html) examples.

## See Also

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html)
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.html)
[IMassProperty2::GetOverrideOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~GetOverrideOptions.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
