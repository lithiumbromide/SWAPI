---
title: "SplitOpenSegment Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SplitOpenSegment"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SplitOpenSegment.html"
---

# SplitOpenSegment Method (IModelDoc2)

Obsolete. Superseded by [ISketchManager::SplitOpenSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~SplitOpenSegment.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SplitOpenSegment( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double

instance.SplitOpenSegment(X, Y, Z)
```

### C#

```csharp
void SplitOpenSegment(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
void SplitOpenSegment(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X value of the point that splits the sketch segment in two
- `Y`: Y value of the point that splits the sketch segment in two
- `Z`: Z value of the point that splits the sketch segment in two

## VBA Syntax

See [ModelDoc2::SplitOpenSegment](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SplitOpenSegment.html).

## Remarks

The selected sketch segment must be an open entity; for example, the start and end points cannot be the same.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[IModelDoc2::SplitClosedSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SplitClosedSegment.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
