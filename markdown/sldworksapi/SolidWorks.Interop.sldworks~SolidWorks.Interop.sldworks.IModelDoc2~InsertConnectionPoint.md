---
title: "InsertConnectionPoint Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertConnectionPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertConnectionPoint.html"
---

# InsertConnectionPoint Method (IModelDoc2)

Adds a connection point based on the selected point and selected planar item.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertConnectionPoint()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.InsertConnectionPoint()
```

### C#

```csharp
void InsertConnectionPoint()
```

### C++/CLI

```cpp
void InsertConnectionPoint();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::InsertConnectionPoint](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertConnectionPoint.html).

## Remarks

If the selection set is not complete, then the Insert Connection Point dialog is displayed.

The connection point is the point on the fitting that defines where the connection to other pipe items begins or ends.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
