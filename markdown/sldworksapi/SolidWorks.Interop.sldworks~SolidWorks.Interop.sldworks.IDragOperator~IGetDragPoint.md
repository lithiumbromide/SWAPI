---
title: "IGetDragPoint Method (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "IGetDragPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IGetDragPoint.html"
---

# IGetDragPoint Method (IDragOperator)

Gets the drag point.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDragPoint( _
   ByRef Point As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim Point As System.Double
Dim value As System.Boolean

value = instance.IGetDragPoint(Point)
```

### C#

```csharp
System.bool IGetDragPoint(
   out System.double Point
)
```

### C++/CLI

```cpp
System.bool IGetDragPoint(
   [Out] System.double Point
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Point`: Array containing the X, Y, Z coordinates of the drag point

### Return Value

True if successful, false if not

## VBA Syntax

See [DragOperator::IGetDragPoint](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~IGetDragPoint.html).

## Remarks

Unless set to another value by [IDragOperator::ISetDragPoint,](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragOperator~ISetDragPoint.html) this value is the origin of the component.

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)
[IDragOperator::GetDragPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~GetDragPoint.html)
[IDragOperator::SetDragPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~SetDragPoint.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
