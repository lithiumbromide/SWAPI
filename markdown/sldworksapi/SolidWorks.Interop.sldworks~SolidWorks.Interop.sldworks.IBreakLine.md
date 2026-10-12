---
title: "IBreakLine Interface"
project: "SOLIDWORKS API Help"
interface: "IBreakLine"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine.html"
---

# IBreakLine Interface

Allows access to information about a break line in a [drawing view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html).

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IBreakLine
```

### Visual Basic (Usage)

```vb
Dim instance As IBreakLine
```

### C#

```csharp
public interface IBreakLine
```

### C++/CLI

```cpp
public interface class IBreakLine
```

## VBA Syntax

See [BreakLine](ms-its:sldworksapivb6.chm::/sldworks~BreakLine.html).

## Examples

[Create Break View (C#)](Create_Broken_View_Example_CSharp.htm)
[Create Break View (VB.NET)](Create_Broken_View_Example_VBNET.htm)
[Create Break View (VBA)](Create_Broken_View_Example_VB.htm)

## Remarks

A break line is represented graphically in a SOLIDWORKS drawing by a pair of lines in the drawing view.

## Accessors

[IView::GetBreakLines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetBreakLines.html) and [IView::IGetBreakLines Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetBreakLines.html)

[IView::InsertBreak Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~InsertBreak.html)

## Access Diagram

[BreakLine](SWObjectModel.pdf#BreakLine)

## See Also

[IBreakLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IDrawingDoc::BreakView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~BreakView.html)
