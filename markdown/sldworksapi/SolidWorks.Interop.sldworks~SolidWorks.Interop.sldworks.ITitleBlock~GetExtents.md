---
title: "GetExtents Method (ITitleBlock)"
project: "SOLIDWORKS API Help"
interface: "ITitleBlock"
member: "GetExtents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock~GetExtents.html"
---

# GetExtents Method (ITitleBlock)

Gets the coordinates on the drawing sheet format that define the extents of the title block.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetExtents( _
   ByRef XUpperLeft As System.Double, _
   ByRef YUpperLeft As System.Double, _
   ByRef XLowerRight As System.Double, _
   ByRef YLowerRight As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ITitleBlock
Dim XUpperLeft As System.Double
Dim YUpperLeft As System.Double
Dim XLowerRight As System.Double
Dim YLowerRight As System.Double

instance.GetExtents(XUpperLeft, YUpperLeft, XLowerRight, YLowerRight)
```

### C#

```csharp
void GetExtents(
   out System.double XUpperLeft,
   out System.double YUpperLeft,
   out System.double XLowerRight,
   out System.double YLowerRight
)
```

### C++/CLI

```cpp
void GetExtents(
   [Out] System.double XUpperLeft,
   [Out] System.double YUpperLeft,
   [Out] System.double XLowerRight,
   [Out] System.double YLowerRight
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XUpperLeft`: X upper-left coordinate
- `YUpperLeft`: Y upper-left coordinate
- `XLowerRight`: X lower-right coordinate
- `YLowerRight`: Y lower-right coordinate

## VBA Syntax

See [TitleBlock::GetExtents](ms-its:sldworksapivb6.chm::/sldworks~TitleBlock~GetExtents.html).

## See Also

[ITitleBlock Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock.html)
[ITitleBlock Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock_members.html)
[ITitleBlock::SetExtents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock~SetExtents.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
