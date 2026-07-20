---
title: "GetFloorAppearance Method (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "GetFloorAppearance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~GetFloorAppearance.html"
---

# GetFloorAppearance Method (ISwScene)

Gets the floor appearance of this scene.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFloorAppearance() As RenderMaterial
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As RenderMaterial

value = instance.GetFloorAppearance()
```

### C#

```csharp
RenderMaterial GetFloorAppearance()
```

### C++/CLI

```cpp
RenderMaterial^ GetFloorAppearance();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

[IRenderMaterial](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)

## VBA Syntax

See

[SwScene::GetFloorAppearance](ms-its:sldworksapivb6.chm::/sldworks~SwScene~GetFloorAppearance.html)

.

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)

[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2025 FCS, Revision Number 33
