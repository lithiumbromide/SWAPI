---
title: "CollisionDetection Method (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "CollisionDetection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~CollisionDetection.html"
---

# CollisionDetection Method (IDragOperator)

Sets the collision detection parameters.

## Syntax

### Visual Basic (Declaration)

```vb
Function CollisionDetection( _
   ByVal EntityArray As System.Object, _
   ByVal PartOnly As System.Boolean, _
   ByVal StopAt As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim EntityArray As System.Object
Dim PartOnly As System.Boolean
Dim StopAt As System.Boolean
Dim value As System.Boolean

value = instance.CollisionDetection(EntityArray, PartOnly, StopAt)
```

### C#

```csharp
System.bool CollisionDetection(
   System.object EntityArray,
   System.bool PartOnly,
   System.bool StopAt
)
```

### C++/CLI

```cpp
System.bool CollisionDetection(
   System.Object^ EntityArray,
   System.bool PartOnly,
   System.bool StopAt
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntityArray`: Array of [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) for collision detection
- `PartOnly`: True checks for collisions with only the components that you selected to move, false check for collisions in all affected components
- `StopAt`: True stops the motion of the component when it touches any other entity, false does not

### Return Value

True if successful, false if not

## VBA Syntax

See [DragOperator::CollisionDetection](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~CollisionDetection.html).

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)
[IDragOperator::CollisionDetectionEnabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~CollisionDetectionEnabled.html)
[IDragOperator::ICollisionDetection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~ICollisionDetection.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
