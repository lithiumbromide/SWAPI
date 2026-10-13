---
title: "ICollisionDetection Method (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "ICollisionDetection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~ICollisionDetection.html"
---

# ICollisionDetection Method (IDragOperator)

Sets the collision detection parameters.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICollisionDetection( _
   ByVal Count As System.Integer, _
   ByRef ComponentArray As Component2, _
   ByVal PartOnly As System.Boolean, _
   ByVal StopAt As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim Count As System.Integer
Dim ComponentArray As Component2
Dim PartOnly As System.Boolean
Dim StopAt As System.Boolean
Dim value As System.Boolean

value = instance.ICollisionDetection(Count, ComponentArray, PartOnly, StopAt)
```

### C#

```csharp
System.bool ICollisionDetection(
   System.int Count,
   ref Component2 ComponentArray,
   System.bool PartOnly,
   System.bool StopAt
)
```

### C++/CLI

```cpp
System.bool ICollisionDetection(
   System.int Count,
   Component2^% ComponentArray,
   System.bool PartOnly,
   System.bool StopAt
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of components for collision detection
- `ComponentArray`: Array of [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) for collision detection
- `PartOnly`: True checks for collisions with only the components that you selected to move, false check for collisions in all affected components
- `StopAt`: True stops the motion of the component when it touches any other entity, false does not

### Return Value

True if successful, false if not

## VBA Syntax

See [DragOperator::ICollisionDetection](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~ICollisionDetection.html).

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)
[IDragOperator::CollisionDetection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~CollisionDetection.html)
[IDragOperator::CollisionDetectionEnabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~CollisionDetectionEnabled.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
