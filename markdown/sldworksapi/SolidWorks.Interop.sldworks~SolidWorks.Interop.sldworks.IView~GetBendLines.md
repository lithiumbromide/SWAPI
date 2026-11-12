---
title: "GetBendLines Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetBendLines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendLines.html"
---

# GetBendLines Method (IView)

Gets the bendlines in a [flat-pattern drawing view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IsFlatPatternView.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBendLines() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetBendLines()
```

### C#

```csharp
System.object GetBendLines()
```

### C++/CLI

```cpp
System.Object^ GetBendLines();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [bendlines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) in the flat-pattern drawing view

## VBA Syntax

See [View::GetBendLines](ms-its:sldworksapivb6.chm::/sldworks~View~GetBendLines.html).

## Examples

[Get Tangent Edges of Bendlines (VB.NET)](Get_Tangent_Edges_of_Bendlines_Example_VBNET.htm)
[Get Tangent Edges of Bendlines (VBA)](Get_Tangent_Edges_of_Bendlines_Example_VB.htm)
[Get Tangent Edges of Bendlines (C#)](Get_Tangent_Edges_of_Bendlines_Example_CSharp.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IVew::GetBendLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendLineCount.html)
[IVew::IGetBendLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBendLines.html)
[ISketchSegment::IsBendLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IsBendLine.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
