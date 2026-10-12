---
title: "GetExcludeFromBOM2 Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetExcludeFromBOM2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetExcludeFromBOM2.html"
---

# GetExcludeFromBOM2 Method (IComponent2)

Gets whether this component is excluded from the bills of materials (BOMs) in the specified configurations.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExcludeFromBOM2( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim Config_opt As System.Integer
Dim Config_names As System.Object
Dim value As System.Object

value = instance.GetExcludeFromBOM2(Config_opt, Config_names)
```

### C#

```csharp
System.object GetExcludeFromBOM2(
   System.int Config_opt,
   System.object Config_names
)
```

### C++/CLI

```cpp
System.Object^ GetExcludeFromBOM2(
   System.int Config_opt,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Config_opt`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_names`: Array of the names of configurations in whose BOMs this component is excluded or included; null or Nothing if Config_opt is set to swInConfigurationOpts_e.swAllConfiguration or swInConfigurationOpts_e.swThisConfiguration

### Return Value

Array of values indicating whether this component is:

- excluded (true) from

- or -

- included (false) in

the BOMs of the specified configurations.

## VBA Syntax

See [Component2::GetExcludeFromBOM2](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetExcludeFromBOM2.html).

## Remarks

This method is valid only for [table-based bills of materials](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html); it does not work for Microsoft Excel-based bills of materials.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IAssemblyDoc::CompConfigProperties6 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties6.html)
[IComponent2::SetExcludeFromBOM2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetExcludeFromBOM2.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
