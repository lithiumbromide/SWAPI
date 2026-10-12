---
title: "SetDragPoint Method (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "SetDragPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~SetDragPoint.html"
---

# SetDragPoint Method (IDragOperator)

Sets the drag point.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDragPoint( _
   ByVal Point As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim Point As System.Object
Dim value As System.Boolean

value = instance.SetDragPoint(Point)
```

### C#

```csharp
System.bool SetDragPoint(
   System.object Point
)
```

### C++/CLI

```cpp
System.bool SetDragPoint(
   System.Object^ Point
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Point`: Array of size 3 containing the X, Y, Z coordinate of the drag point

### Return Value

True if successful, false if not

## VBA Syntax

See [DragOperator::SetDragPoint](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~SetDragPoint.html).

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)
[IDragOperator::GetDragPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~GetDragPoint.html)
[IDragOperator::IGetDragPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IGetDragPoint.html)
[IDragOperator::ISetDragPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~ISetDragPoint.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
