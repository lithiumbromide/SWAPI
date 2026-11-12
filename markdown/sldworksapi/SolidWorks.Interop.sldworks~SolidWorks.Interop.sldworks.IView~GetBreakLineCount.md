---
title: "GetBreakLineCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetBreakLineCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLineCount.html"
---

# GetBreakLineCount Method (IView)

Obsolete. Superseded by [IView::GetBreakLineCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetBreakLineCount2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBreakLineCount( _
   ByRef Size As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Size As System.Integer
Dim value As System.Integer

value = instance.GetBreakLineCount(Size)
```

### C#

```csharp
System.int GetBreakLineCount(
   out System.int Size
)
```

### C++/CLI

```cpp
System.int GetBreakLineCount(
   [Out] System.int Size
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Size`: Size of an array of doubles to allocate in call to [IView::GetBreakLineInfo](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetBreakLineInfo.html) and [IView::IGetBreakLineInfo](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetBreakLineInfo.html)

### Return Value

Number of breaks

## VBA Syntax

See [View::GetBreakLineCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetBreakLineCount.html).

## Remarks

This method indicates the number of break lines in the view; it does not indicate if the view is broken.

A drawing view can have break lines without the break being applied. To determine whether a view is broken, use [IView::IsBroken](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IsBroken.html).

A break in a drawing view consists of a pair of lines. This method returns the number of breaks in the view, not the number of break lines. For example, this method returns 3 for a view that has three breaks in it, even though there are three pairs (or six lines) on the display.

Call this method before calling [IView::IGetBreakLines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetBreakLines.html) to determine the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetBreakLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLines.html)
[IView::BreakLineGap Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~BreakLineGap.html)
[IView::InsertBreak Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBreak.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
