---
title: "IsBendLine Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "IsBendLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IsBendLine.html"
---

# IsBendLine Method (ISketchSegment)

Gets whether the sketch segment is a bendline.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsBendLine() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
Dim value As System.Boolean

value = instance.IsBendLine()
```

### C#

```csharp
System.bool IsBendLine()
```

### C++/CLI

```cpp
System.bool IsBendLine();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the sketch segment is a bendline, false if not

## VBA Syntax

See [SketchSegment::IsBendLine](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~IsBendLine.html).

## Examples

[Get Tangent Edges of Bendlines (VB.NET)](Get_Tangent_Edges_of_Bendlines_Example_VBNET.htm)
[Get Tangent Edges of Bendlines (VBA)](Get_Tangent_Edges_of_Bendlines_Example_VB.htm)
[Get Tangent Edges of Bendlines (C#)](Get_Tangent_Edges_of_Bendlines_Example_CSharp.htm)

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)
[IView::GetBendLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendLineCount.html)
[IView::GetBendLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendLines.html)
[IView::IGetBendLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBendLines.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
