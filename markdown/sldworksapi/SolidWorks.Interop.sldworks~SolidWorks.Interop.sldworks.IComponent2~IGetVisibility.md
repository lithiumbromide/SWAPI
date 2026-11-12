---
title: "IGetVisibility Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IGetVisibility"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetVisibility.html"
---

# IGetVisibility Method (IComponent2)

Gets the visibility state for this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetVisibility( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_count As System.Integer, _
   ByRef Config_names As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim Config_opt As System.Integer
Dim Config_count As System.Integer
Dim Config_names As System.String
Dim value As System.Integer

value = instance.IGetVisibility(Config_opt, Config_count, Config_names)
```

### C#

```csharp
System.int IGetVisibility(
   System.int Config_opt,
   System.int Config_count,
   ref System.string Config_names
)
```

### C++/CLI

```cpp
System.int IGetVisibility(
   System.int Config_opt,
   System.int Config_count,
   System.String^% Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Config_opt`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_count`: Number of configurations for this component
- `Config_names`: Array of configuration names of size Config_count

### Return Value

Array of visibility states of size Config_count

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetVisibility.html)
[IComponent2::SetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetVisibility.html)
[IComponent2::Visible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Visible.html)
[IAssemblyDoc::SetComponentVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentVisibility.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
