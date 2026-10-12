---
title: "GetScene Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "GetScene"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetScene.html"
---

# GetScene Method (IConfiguration)

Gets the ISwScene object for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetScene() As SWScene
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As SWScene

value = instance.GetScene()
```

### C#

```csharp
SWScene GetScene()
```

### C++/CLI

```cpp
SWScene^ GetScene();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)

## VBA Syntax

See [Configuration::GetScene](ms-its:sldworksapivb6.chm::/sldworks~Configuration~GetScene.html).

## Examples

[Get and Set Scene Properties (VBA)](Get_and_Set_Scene_Properties_Example_VB.htm)
[Get and Set Scene Properties (VB.NET)](Get_and_Set_Scene_Properties_Example_VBNET.htm)
[Get and Set Scene Properties (C#)](Get_and_Set_Scene_Properties_Example_CSharp.htm)

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IModelDocExtension::InsertScene Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertScene.html)
[IModelDocExtension::DeleteScene Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteScene.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
