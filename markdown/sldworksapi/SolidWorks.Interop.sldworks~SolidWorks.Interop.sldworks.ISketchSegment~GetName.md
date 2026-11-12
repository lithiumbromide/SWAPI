---
title: "GetName Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "GetName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetName.html"
---

# GetName Method (ISketchSegment)

Gets the name of this sketch segment.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
Dim value As System.String

value = instance.GetName()
```

### C#

```csharp
System.string GetName()
```

### C++/CLI

```cpp
System.String^ GetName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Sketch segment name

## VBA Syntax

See [SketchSegment::GetName](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~GetName.html).

## Examples

[Get Sketch Segment Names (C#)](Get_Sketch_Segment_Names_Example_CSharp.htm)
[Get Sketch Segment Names (VB.NET)](Get_Sketch_Segment_Names_Example_VBNET.htm)
[Get Sketch Segment Names (VBA)](Get_Sketch_Segment_Names_Example_VB.htm)

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
