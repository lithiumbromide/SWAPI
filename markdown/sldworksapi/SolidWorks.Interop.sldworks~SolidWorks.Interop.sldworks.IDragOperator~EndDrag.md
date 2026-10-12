---
title: "EndDrag Method (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "EndDrag"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~EndDrag.html"
---

# EndDrag Method (IDragOperator)

Terminates the drag operation.

## Syntax

### Visual Basic (Declaration)

```vb
Function EndDrag() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim value As System.Boolean

value = instance.EndDrag()
```

### C#

```csharp
System.bool EndDrag()
```

### C++/CLI

```cpp
System.bool EndDrag();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the drag operation ended successfully, false if not

## VBA Syntax

See [DragOperator::EndDrag](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~EndDrag.html).

## Examples

[Rotate Assembly Component on Axis Using IDragOperator::Drag (VBA)](Rotate_Assembly_Component_on_Axis_Example_VB.htm)
[Rotate Assembly Component on Axis Using IDragOperator::Drag (VB.NET)](Rotate_Assembly_Component_on_Axis_Example_VBNET.htm)
[Rotate Assembly Component on Axis Using IDragOperator::Drag (C#)](Rotate_Assembly_Component_on_Axis_Example_CSharp.htm)
[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (VBA)](Rotate_Assembly_Component_on_Axis_Example2_VB.htm)
[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (VB.NET)](Rotate_Assembly_Component_on_Axis_Example2_VBNET.htm)
[Rotate Assembly Component on Axis Using IDragOperator::DragAsUI (C#)](Rotate_Assembly_Component_on_Axis_Example2_CSharp.htm)

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)
[IDragOperator::BeginDrag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~BeginDrag.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
