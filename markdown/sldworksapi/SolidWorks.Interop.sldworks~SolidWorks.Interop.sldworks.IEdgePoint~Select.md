---
title: "Select Method (IEdgePoint)"
project: "SOLIDWORKS API Help"
interface: "IEdgePoint"
member: "Select"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint~Select.html"
---

# Select Method (IEdgePoint)

Selects a midpoint on an [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) or an endpoint or midpoint on a [reference curve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IReferenceCurve.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function Select( _
   ByVal BAppend As System.Boolean, _
   ByVal SelMark As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgePoint
Dim BAppend As System.Boolean
Dim SelMark As System.Integer
Dim value As System.Boolean

value = instance.Select(BAppend, SelMark)
```

### C#

```csharp
System.bool Select(
   System.bool BAppend,
   System.int SelMark
)
```

### C++/CLI

```cpp
System.bool Select(
   System.bool BAppend,
   System.int SelMark
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BAppend`: True to add this selection to the current selection, false to replace the current selection list with this selection
- `SelMark`: Selection mark to assign to this midpoint or endpoint

### Return Value

True if an endpoint or midpoint is selected, false if not

## VBA Syntax

See [EdgePoint::Select](ms-its:sldworksapivb6.chm::/sldworks~EdgePoint~Select.html).

## See Also

[IEdgePoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint.html)
[IEdgePoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
