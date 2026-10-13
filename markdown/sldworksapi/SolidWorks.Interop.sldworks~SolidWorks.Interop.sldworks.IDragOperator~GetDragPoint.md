---
title: "GetDragPoint Method (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "GetDragPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~GetDragPoint.html"
---

# GetDragPoint Method (IDragOperator)

Gets the drag point.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDragPoint( _
   ByRef Point As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim Point As System.Object
Dim value As System.Boolean

value = instance.GetDragPoint(Point)
```

### C#

```csharp
System.bool GetDragPoint(
   out System.object Point
)
```

### C++/CLI

```cpp
System.bool GetDragPoint(
   [Out] System.Object^ Point
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Point`: Array containing the X, Y, Z coordinates of the drag point

### Return Value

True if successful, false if not

## VBA Syntax

See [DragOperator::GetDragPoint](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~GetDragPoint.html).

## Remarks

Unless set to another value by [IDragOperator::SetDragPoint,](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragOperator~ISetDragPoint.html) this value is the origin of the component.

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)
[IDragOperator::IGetDragPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IGetDragPoint.html)
[IDragOperator::ISetDragPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~ISetDragPoint.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
