---
title: "DisplayWhenAdded Property (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "DisplayWhenAdded"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~DisplayWhenAdded.html"
---

# DisplayWhenAdded Property (ISketchManager)

Gets or sets whether new sketch entities are immediately displayed when created.

## Syntax

### Visual Basic (Declaration)

```vb
Property DisplayWhenAdded As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim value As System.Boolean

instance.DisplayWhenAdded = value

value = instance.DisplayWhenAdded
```

### C#

```csharp
System.bool DisplayWhenAdded {get; set;}
```

### C++/CLI

```cpp
property System.bool DisplayWhenAdded {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display new sketch entities when added, false to not

## VBA Syntax

See [SketchManager::DisplayWhenAdded](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~DisplayWhenAdded.html).

## Remarks

The sketch entities appear on the screen after performing [IModelView::GraphicsRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GraphicsRedraw.html) or [IModelView::IGraphicsRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~IGraphicsRedraw.html) or [IModelDoc2::EditRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRebuild3.html) is performed. Also, [ISketchManager::AddToDB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~AddToDB.html) must be true to use this method's settings.

This display setting remains even after your program run has ended. Therefore, it is recommended that you reset this parameter to TRUE at the end of your program. For example, if you have ended your program and the display is set to FALSE, then the user would have difficulty performing selections and newly created entities would not be seen until a redraw or a rebuild.

NOTES:

- IModelView::GraphicsRedraw and IModelView::IGraphicsRedraw are much faster than IModelDoc2::EditRebuild3.
- ISketchManager::AddToDB and ISketchManager::DisplayWhenAdded also increase performance during sketch entity creation.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
