---
title: "SetKeepLightInRenderScene Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SetKeepLightInRenderScene"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetKeepLightInRenderScene.html"
---

# SetKeepLightInRenderScene Method (IModelDocExtension)

Sets whether to keep a light when the scene changes.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetKeepLightInRenderScene( _
   ByVal ID As System.Integer, _
   ByVal Val As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim ID As System.Integer
Dim Val As System.Boolean

instance.SetKeepLightInRenderScene(ID, Val)
```

### C#

```csharp
void SetKeepLightInRenderScene(
   System.int ID,
   System.bool Val
)
```

### C++/CLI

```cpp
void SetKeepLightInRenderScene(
   System.int ID,
   System.bool Val
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`: Light ID
- `Val`: True to keep a light when the scene changes, false to not

## VBA Syntax

See [ModelDocExtension::SetKeepLightInRenderScene](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~SetKeepLightInRenderScene.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetKeepLightInRenderScene Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetKeepLightInRenderScene.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
