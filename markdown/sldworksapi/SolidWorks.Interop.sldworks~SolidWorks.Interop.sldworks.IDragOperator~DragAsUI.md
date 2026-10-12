---
title: "DragAsUI Method (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "DragAsUI"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DragAsUI.html"
---

# DragAsUI Method (IDragOperator)

Sets the transform matrix for this drag operation.

## Syntax

### Visual Basic (Declaration)

```vb
Function DragAsUI( _
   ByVal PXform As MathTransform _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim PXform As MathTransform
Dim value As System.Boolean

value = instance.DragAsUI(PXform)
```

### C#

```csharp
System.bool DragAsUI(
   MathTransform PXform
)
```

### C++/CLI

```cpp
System.bool DragAsUI(
   MathTransform^ PXform
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PXform`: Pointer to [IMathTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) that specifies the desired motion for this step

### Return Value

True if the move was successful, false if not (see **Remarks**)

## VBA Syntax

See [DragOperator::DragAsUI](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~DragAsUI.html).

## Examples

[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (VBA)](Rotate_Assembly_Component_on_Axis_Example2_VB.htm)
[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (VB.NET)](Rotate_Assembly_Component_on_Axis_Example2_VBNET.htm)
[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (C#)](Rotate_Assembly_Component_on_Axis_Example2_CSharp.htm)

## Remarks

This method returns false if the drag cannot be performed. This typically occurs because of a collision.

This method does not set [IDragOperator::DragCorrected](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragOperator~DragCorrected.html).

This method is not as precise as the [IDragOperator::Drag](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragOperator~Drag.html) or [IDragOperator::IDrag](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragOperator~IDrag.html) method. IDragOperator::DragAsUI is more like an interactive drag operation performed in the SOLIDWORKS 2001Plus software. This method may give better graphics performance than IDragOperator::Drag.

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)
[IDragOperator::CollisionDetection Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~CollisionDetection.html)
[IDragOperator::DynamicClearanceEnabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DynamicClearanceEnabled.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
