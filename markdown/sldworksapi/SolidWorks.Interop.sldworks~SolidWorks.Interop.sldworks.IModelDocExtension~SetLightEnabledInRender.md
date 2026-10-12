---
title: "SetLightEnabledInRender Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SetLightEnabledInRender"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetLightEnabledInRender.html"
---

# SetLightEnabledInRender Method (IModelDocExtension)

Sets whether a light is on in this model.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetLightEnabledInRender( _
   ByVal ID As System.Integer, _
   ByVal Val As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim ID As System.Integer
Dim Val As System.Boolean

instance.SetLightEnabledInRender(ID, Val)
```

### C#

```csharp
void SetLightEnabledInRender(
   System.int ID,
   System.bool Val
)
```

### C++/CLI

```cpp
void SetLightEnabledInRender(
   System.int ID,
   System.bool Val
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`: Light ID
- `Val`: True to enable the light, false to not

## VBA Syntax

See [ModelDocExtension::SetLightEnabledInRender](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~SetLightEnabledInRender.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetLightEnabledInRender Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetLightEnabledInRender.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
