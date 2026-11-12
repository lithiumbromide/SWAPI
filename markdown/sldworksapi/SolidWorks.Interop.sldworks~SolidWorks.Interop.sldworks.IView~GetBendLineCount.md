---
title: "GetBendLineCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetBendLineCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendLineCount.html"
---

# GetBendLineCount Method (IView)

Gets the number of bendlines in a [flat-pattern drawing view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IsFlatPatternView.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBendLineCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetBendLineCount()
```

### C#

```csharp
System.int GetBendLineCount()
```

### C++/CLI

```cpp
System.int GetBendLineCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of bendlines in a flat-pattern drawing view

## VBA Syntax

See [View::GetBendLineCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetBendLineCount.html).

## Examples

[Get Tangent Edges of Bendlines (VB.NET)](Get_Tangent_Edges_of_Bendlines_Example_VBNET.htm)
[Get Tangent Edges of Bendlines (VBA)](Get_Tangent_Edges_of_Bendlines_Example_VB.htm)
[Get Tangent Edges of Bendlines (C#)](Get_Tangent_Edges_of_Bendlines_Example_CSharp.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetBendLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBendLines.html)
[IView::IGetBendLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBendLines.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
