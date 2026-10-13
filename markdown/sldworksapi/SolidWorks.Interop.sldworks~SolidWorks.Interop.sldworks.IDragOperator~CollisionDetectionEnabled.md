---
title: "CollisionDetectionEnabled Property (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "CollisionDetectionEnabled"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~CollisionDetectionEnabled.html"
---

# CollisionDetectionEnabled Property (IDragOperator)

Gets or sets the collision detection setting.

## Syntax

### Visual Basic (Declaration)

```vb
Property CollisionDetectionEnabled As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim value As System.Boolean

instance.CollisionDetectionEnabled = value

value = instance.CollisionDetectionEnabled
```

### C#

```csharp
System.bool CollisionDetectionEnabled {get; set;}
```

### C++/CLI

```cpp
property System.bool CollisionDetectionEnabled {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if collision detection is enabled, false if it is disabled

## VBA Syntax

See [DragOperator::CollisionDetectionEnabled](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~CollisionDetectionEnabled.html).

## Examples

[Rotate Assembly Component on Axis Using IDragOperator::Drag (VBA)](Rotate_Assembly_Component_on_Axis_Example_VB.htm)
[Rotate Assembly Component on Axis Using IDragOperator::Drag (VB.NET)](Rotate_Assembly_Component_on_Axis_Example_VBNET.htm)
[Rotate Assembly Component on Axis Using IDragOperator::Drag (C#)](Rotate_Assembly_Component_on_Axis_Example_CSharp.htm)

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)
[IDragOperator::CollisionDetection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~CollisionDetection.html)
[IDragOperator:Drag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~Drag.html)
[IDragOperator:DragAsUI Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DragAsUI.html)
[IDragOperator:DynamicClearanceEnabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DynamicClearanceEnabled.html)
[IDragOperator::ICollisionDetection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~ICollisionDetection.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
