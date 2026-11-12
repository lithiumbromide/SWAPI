---
title: "BackgroundImage Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "BackgroundImage"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundImage.html"
---

# BackgroundImage Property (ISwScene)

Gets or sets the background image for this scene.

## Syntax

### Visual Basic (Declaration)

```vb
Property BackgroundImage As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.String

instance.BackgroundImage = value

value = instance.BackgroundImage
```

### C#

```csharp
System.string BackgroundImage {get; set;}
```

### C++/CLI

```cpp
property System.String^ BackgroundImage {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fully qualified path to a background image file

## VBA Syntax

See [SwScene::BackgroundImage](ms-its:sldworksapivb6.chm::/sldworks~SwScene~BackgroundImage.html).

## Examples

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html) examples.

## Remarks

This property is valid only if [ISwScene::BackgroundType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~BackgroundType.html) is [swSceneBackgroundType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSceneBackgroundType_e.html).swBackgroundType_Image.

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)
[IModelDoc2::InsertBkgImage Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertBkgImage.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
