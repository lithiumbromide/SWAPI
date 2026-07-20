---
title: "AddOrEditFloorAppearance Method (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "AddOrEditFloorAppearance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~AddOrEditFloorAppearance.html"
---

# AddOrEditFloorAppearance Method (ISwScene)

Adds or modifies the floor appearance of this scene.

## Syntax

### Visual Basic (Declaration)

```vb
Sub AddOrEditFloorAppearance( _
   ByVal Appearance As RenderMaterial _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim Appearance As RenderMaterial

instance.AddOrEditFloorAppearance(Appearance)
```

### C#

```csharp
void AddOrEditFloorAppearance(
   RenderMaterial Appearance
)
```

### C++/CLI

```cpp
void AddOrEditFloorAppearance(
   RenderMaterial^ Appearance
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Appearance`: [IRenderMaterial](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)

## VBA Syntax

See

[SwScene::AddOrEditFloorAppearance](ms-its:sldworksapivb6.chm::/sldworks~SwScene~AddOrEditFloorAppearance.html)

.

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)

[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2025 FCS, Revision Number 33
