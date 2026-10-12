---
title: "ISetDragPoint Method (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "ISetDragPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~ISetDragPoint.html"
---

# ISetDragPoint Method (IDragOperator)

Sets the drag point.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetDragPoint( _
   ByRef Point As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim Point As System.Double
Dim value As System.Boolean

value = instance.ISetDragPoint(Point)
```

### C#

```csharp
System.bool ISetDragPoint(
   ref System.double Point
)
```

### C++/CLI

```cpp
System.bool ISetDragPoint(
   System.double% Point
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Point`: Array containing the X, Y, Z coordinate of the drag point

### Return Value

True if successful, false if not

## VBA Syntax

See [DragOperator::ISetDragPoint](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~ISetDragPoint.html).

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)
[IDragOperator::GetDragPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~GetDragPoint.html)
[IDragOperator::IGetDragPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IGetDragPoint.html)
[IDragOperator::SetDragPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~SetDragPoint.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
