---
title: "GetKeepLightInRenderScene Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetKeepLightInRenderScene"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetKeepLightInRenderScene.html"
---

# GetKeepLightInRenderScene Method (IModelDocExtension)

Gets whether a light is kept when the scene changes.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetKeepLightInRenderScene( _
   ByVal ID As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim ID As System.Integer
Dim value As System.Boolean

value = instance.GetKeepLightInRenderScene(ID)
```

### C#

```csharp
System.bool GetKeepLightInRenderScene(
   System.int ID
)
```

### C++/CLI

```cpp
System.bool GetKeepLightInRenderScene(
   System.int ID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`: Light ID

### Return Value

True if the light is kept when the scene changes, false if the light is deleted when the scene changes

## VBA Syntax

See [ModelDocExtension::GetKeepLightInRenderScene](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~GetKeepLightInRenderScene.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::SetKeepLightInRenderScene Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetKeepLightInRenderScene.html)
