---
title: "SetComponentVisibility Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "SetComponentVisibility"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentVisibility.html"
---

# SetComponentVisibility Method (IAssemblyDoc)

Hides or shows the selected component in the specified configurations in this assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetComponentVisibility( _
   ByVal Visibility As System.Boolean, _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Visibility As System.Boolean
Dim Config_opt As System.Integer
Dim Config_names As System.Object

instance.SetComponentVisibility(Visibility, Config_opt, Config_names)
```

### C#

```csharp
void SetComponentVisibility(
   System.bool Visibility,
   System.int Config_opt,
   System.object Config_names
)
```

### C++/CLI

```cpp
void SetComponentVisibility(
   System.bool Visibility,
   System.int Config_opt,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Visibility`: True to show the selected component, false to hide it
- `Config_opt`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_names`: Array of the names of the configurations for the component

## VBA Syntax

See [AssemblyDoc::SetComponentVisibility](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~SetComponentVisibility.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IComponent2::ISetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ISetVisibility.html)
[IComponent2::GetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetVisibility.html)
[IComponent2::SetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetVisibility.html)
[IComponent2::IGetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetVisibility.html)
[IComponent2::Visible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Visible.html)
[IAssemblyDoc::ISetComponentVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ISetComponentVisibility.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12
