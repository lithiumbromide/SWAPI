---
title: "SetExtents Method (ITitleBlock)"
project: "SOLIDWORKS API Help"
interface: "ITitleBlock"
member: "SetExtents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock~SetExtents.html"
---

# SetExtents Method (ITitleBlock)

Sets the coordinates on the drawing sheet format that define the extens of the title blcok.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetExtents( _
   ByVal XUpperLeft As System.Double, _
   ByVal YUpperLeft As System.Double, _
   ByVal XLowerRight As System.Double, _
   ByVal YLowerRight As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ITitleBlock
Dim XUpperLeft As System.Double
Dim YUpperLeft As System.Double
Dim XLowerRight As System.Double
Dim YLowerRight As System.Double

instance.SetExtents(XUpperLeft, YUpperLeft, XLowerRight, YLowerRight)
```

### C#

```csharp
void SetExtents(
   System.double XUpperLeft,
   System.double YUpperLeft,
   System.double XLowerRight,
   System.double YLowerRight
)
```

### C++/CLI

```cpp
void SetExtents(
   System.double XUpperLeft,
   System.double YUpperLeft,
   System.double XLowerRight,
   System.double YLowerRight
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XUpperLeft`: X upper-left coordinate
- `YUpperLeft`: Y upper-left coordinate
- `XLowerRight`: X lower-right coordinate
- `YLowerRight`: Y lower-right coordinate

## VBA Syntax

See [TitleBlock::SetExtents](ms-its:sldworksapivb6.chm::/sldworks~TitleBlock~SetExtents.html).

## See Also

[ITitleBlock Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock.html)
[ITitleBlock Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock_members.html)
[ITitleBlock::GetExtents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock~GetExtents.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
