---
title: "SetVisibility Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "SetVisibility"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetVisibility.html"
---

# SetVisibility Method (IComponent2)

Sets the visibility state for this component.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetVisibility( _
   ByVal State As System.Integer, _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim State As System.Integer
Dim Config_opt As System.Integer
Dim Config_names As System.Object

instance.SetVisibility(State, Config_opt, Config_names)
```

### C#

```csharp
void SetVisibility(
   System.int State,
   System.int Config_opt,
   System.object Config_names
)
```

### C++/CLI

```cpp
void SetVisibility(
   System.int State,
   System.int Config_opt,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `State`: Visibility state as defined in [swComponentVisibilityState_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentVisibilityState_e.html)
- `Config_opt`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_names`: Array of configuration names; valid only if Config_opt is set to swInConfigurationOpts_e.swSpecifyConfiguration

## VBA Syntax

See [Component2::SetVisibility](ms-its:sldworksapivb6.chm::/sldworks~Component2~SetVisibility.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::Visible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Visible.html)
[IComponent2::ISetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ISetVisibility.html)
[IComponent2::IGetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetVisibility.html)
[IComponent2::GetVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetVisibility.html)
[IComponent2::IsHidden Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsHidden.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.o
