---
title: "GraphicsRedrawEnabled Property (ICollisionDetectionManager)"
project: "SOLIDWORKS API Help"
interface: "ICollisionDetectionManager"
member: "GraphicsRedrawEnabled"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager~GraphicsRedrawEnabled.html"
---

# GraphicsRedrawEnabled Property (ICollisionDetectionManager)

Gets or sets whether to display components in their transformed positions.

## Syntax

### Visual Basic (Declaration)

```vb
Property GraphicsRedrawEnabled As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICollisionDetectionManager
Dim value As System.Boolean

instance.GraphicsRedrawEnabled = value

value = instance.GraphicsRedrawEnabled
```

### C#

```csharp
System.bool GraphicsRedrawEnabled {get; set;}
```

### C++/CLI

```cpp
property System.bool GraphicsRedrawEnabled {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to display components in their transformed positions, false to display components in their last known positions

## VBA Syntax

See [CollisionDetectionManager::GraphicsRedrawEnabled](ms-its:sldworksapivb6.chm::/sldworks~CollisionDetectionManager~GraphicsRedrawEnabled.html).

## Remarks

If this property is set to false, the graphics display update is drastically reduced. The client application may force the assembly to be redrawn by calling [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html).

Set this property to false for maximum performance.

## See Also

[ICollisionDetectionManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.html)
[ICollisionDetectionManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
