---
title: "AlignDimensions Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "AlignDimensions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AlignDimensions.html"
---

# AlignDimensions Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::AlignDimensions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~AlignDimensions.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub AlignDimensions()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.AlignDimensions()
```

### C#

```csharp
void AlignDimensions()
```

### C++/CLI

```cpp
void AlignDimensions();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::AlignDimensions](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~AlignDimensions.html).

## Remarks

This method attempts to sort the selected dimensions into three groups: linear, ordinate, and angular. Within the linear group, it sorts by measured direction. Each of these dimensions are then aligned with the other like dimensions. These are then updated and dragged together.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::AlignOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AlignOrdinate.html)
[IModelDoc2::AlignParallelDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AlignParallelDimensions.html)
[IModelDoc2::BreakDimensionAlignment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~BreakDimensionAlignment.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
