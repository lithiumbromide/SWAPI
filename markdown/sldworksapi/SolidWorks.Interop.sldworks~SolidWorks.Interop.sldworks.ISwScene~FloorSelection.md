---
title: "FloorSelection Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "FloorSelection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorSelection.html"
---

# FloorSelection Property (ISwScene)

Gets or sets the floor appearance of this scene.

## Syntax

### Visual Basic (Declaration)

```vb
Property FloorSelection As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Object

instance.FloorSelection = value

value = instance.FloorSelection
```

### C#

```csharp
System.object FloorSelection {get; set;}
```

### C++/CLI

```cpp
property System.Object^ FloorSelection {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IAppearanceSetting](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting.html)

## VBA Syntax

See [SwScene::FloorSelection](ms-its:sldworksapivb6.chm::/sldworks~SwScene~FloorSelection.html).

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
