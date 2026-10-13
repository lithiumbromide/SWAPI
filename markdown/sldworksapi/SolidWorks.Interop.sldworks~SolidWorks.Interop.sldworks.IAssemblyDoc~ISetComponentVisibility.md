---
title: "ISetComponentVisibility Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "ISetComponentVisibility"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ISetComponentVisibility.html"
---

# ISetComponentVisibility Method (IAssemblyDoc)

Hides or shows the selected component in the specified configurations in this assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetComponentVisibility( _
   ByVal Visibility As System.Boolean, _
   ByVal Config_opt As System.Integer, _
   ByVal Config_count As System.Integer, _
   ByRef Config_names As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Visibility As System.Boolean
Dim Config_opt As System.Integer
Dim Config_count As System.Integer
Dim Config_names As System.String

instance.ISetComponentVisibility(Visibility, Config_opt, Config_count, Config_names)
```

### C#

```csharp
void ISetComponentVisibility(
   System.bool Visibility,
   System.int Config_opt,
   System.int Config_count,
   ref System.string Config_names
)
```

### C++/CLI

```cpp
void ISetComponentVisibility(
   System.bool Visibility,
   System.int Config_opt,
   System.int Config_count,
   System.String^% Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Visibility`: True to show the selected component, false to hide it
- `Config_opt`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_count`: Number of configurations for the component
- `Config_names`: Array of the names of the configurations for the component

## VBA Syntax

See [AssemblyDoc::ISetComponentVisibility](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~ISetComponentVisibility.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IComponent2::GetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetVisibility.html)
[IComponent2::ISetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ISetVisibility.html)
[IComponent2::Visible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Visible.html)
[IComponent2::SetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetVisibility.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12
