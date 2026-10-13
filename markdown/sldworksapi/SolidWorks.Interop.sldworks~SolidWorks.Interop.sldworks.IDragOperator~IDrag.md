---
title: "IDrag Method (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "IDrag"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IDrag.html"
---

# IDrag Method (IDragOperator)

Sets the transform matrix for this drag operation.

## Syntax

### Visual Basic (Declaration)

```vb
Function IDrag( _
   ByVal PXform As MathTransform _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim PXform As MathTransform
Dim value As System.Boolean

value = instance.IDrag(PXform)
```

### C#

```csharp
System.bool IDrag(
   MathTransform PXform
)
```

### C++/CLI

```cpp
System.bool IDrag(
   MathTransform^ PXform
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PXform`: Pointer to an [IMathTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) that specifies the desired motion for this step

### Return Value

True if the move was successful, false if not (see **Remarks**)

## VBA Syntax

See [DragOperator::IDrag](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~IDrag.html).

## Remarks

This method is more precise than the [IDragOperator::DragAsUI](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragOperator~DragAsUI.html) method. IDragOperator::DragAsUI is more like an interactive drag operation performed in the SOLIDWORKS 2001Plus software and it may give better graphics performance than IDragOperator::Drag.

You will see an improvement in performance when this method is used in the default state. If [collision detection](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragOperator~CollisionDetectionEnabled.html) or [clearance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragOperator~DynamicClearanceEnabled.html) is enabled, then the original mode is used. This method is more efficient than making multiple calls to [IComponent2::SetTransformAndSolve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~SetTransformAndSolve2.html) because this method reuses the solver.

Use [IDragOperator::UseAbsoluteTransforms](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragOperator~UseAbsoluteTransform.html) to set the transforms type to absolute or relative.

If the desired orientation set by this method was not honored and remedial action occurred, then the [IDragOperation::DragCorrected](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragOperator~DragCorrected.html) property is set.

This method returns false if the drag cannot be performed. This typically occurs because of a collision.

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)
[IDragOperator::Drag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~Drag.html)
[IDragOperator::CollisionDetectionEnabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~CollisionDetectionEnabled.html)
[IDragOperator::DynamicClearanceEnabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DynamicClearanceEnabled.html)
[IDragOperator::UseAbsoluteTransform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~UseAbsoluteTransform.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
