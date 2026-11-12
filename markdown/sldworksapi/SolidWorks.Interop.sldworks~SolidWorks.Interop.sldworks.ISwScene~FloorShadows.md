---
title: "FloorShadows Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "FloorShadows"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorShadows.html"
---

# FloorShadows Property (ISwScene)

Gets or sets whether to show shadows cast by the model on the scene floor.

## Syntax

### Visual Basic (Declaration)

```vb
Property FloorShadows As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Boolean

instance.FloorShadows = value

value = instance.FloorShadows
```

### C#

```csharp
System.bool FloorShadows {get; set;}
```

### C++/CLI

```cpp
property System.bool FloorShadows {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to show shadows cast by the model, false to not

## VBA Syntax

See [SwScene::FloorShadows](ms-its:sldworksapivb6.chm::/sldworks~SwScene~FloorShadows.html).

## Examples

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html) examples.

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
