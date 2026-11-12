---
title: "IsBroken Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IsBroken"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsBroken.html"
---

# IsBroken Method (IView)

Gets whether the drawing view is displayed with a break.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsBroken() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

value = instance.IsBroken()
```

### C#

```csharp
System.bool IsBroken()
```

### C++/CLI

```cpp
System.bool IsBroken();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the view is displayed with a break, false if not

## VBA Syntax

See [View::IsBroken](ms-its:sldworksapivb6.chm::/sldworks~View~IsBroken.html).

## Remarks

This method indicates if the view is displayed broken, not if the view has break lines.

A drawing view can have break lines without the break being applied. To determine if a view has break lines, use [IView::GetBreakLineCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetBreakLineCount.html) or [IView::GetBreakLines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetBreakLines.html) or [IView::IGetBreakLines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetBreakLines.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IGetBreakLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBreakLineInfo.html)
[IView::GetBreakLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLineCount.html)
[IView::GetBreakLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLineInfo.html)
[IView::BreakLineGap Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~BreakLineGap.html)
[IView::InsertBreak Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBreak.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
