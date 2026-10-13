---
title: "FloorReflections Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "FloorReflections"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorReflections.html"
---

# FloorReflections Property (ISwScene)

Gets or sets whether to show reflections of the model on the scene floor.

## Syntax

### Visual Basic (Declaration)

```vb
Property FloorReflections As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Boolean

instance.FloorReflections = value

value = instance.FloorReflections
```

### C#

```csharp
System.bool FloorReflections {get; set;}
```

### C++/CLI

```cpp
property System.bool FloorReflections {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to show reflections, false to not

## VBA Syntax

See [SwScene::FloorReflections](ms-its:sldworksapivb6.chm::/sldworks~SwScene~FloorReflections.html).

## Examples

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html) examples.

## Remarks

This property is valid only if [ISwScene::FloorShadows](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorShadows.html) is set to true.

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
