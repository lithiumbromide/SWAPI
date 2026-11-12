---
title: "GetBreakLineCount2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetBreakLineCount2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLineCount2.html"
---

# GetBreakLineCount2 Method (IView)

Gets the number of breaks lines and breaks in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBreakLineCount2( _
   ByRef Size As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Size As System.Integer
Dim value As System.Integer

value = instance.GetBreakLineCount2(Size)
```

### C#

```csharp
System.int GetBreakLineCount2(
   out System.int Size
)
```

### C++/CLI

```cpp
System.int GetBreakLineCount2(
   [Out] System.int Size
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Size`: Size of an array of doubles to allocate in [IView::GetBreakLineInfo2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetBreakLineInfo2.html) and [IView::IGetBreakLineInfo2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetBreakLineInfo2.html)

### Return Value

Number of breaks

## VBA Syntax

See [View::GetBreakLineCount2](ms-its:sldworksapivb6.chm::/sldworks~View~GetBreakLineCount2.html).

## Examples

[Get Break Line Data (VBA)](Get_Break_Line_Data_Example_VB.htm)
[Get Break Line Data (VB.NET)](Get_Break_Line_Data_Example_VBNET.htm)
[Get Break Line Data (C#)](Get_Break_Line_Data_Example_CSharp.htm)

## Remarks

A drawing view can have break lines without the break being applied. To determine whether a view is broken, use [IView::IsBroken](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IsBroken.html).

A break in a drawing view consists of a pair of lines. This method returns the number of breaks in the view. For example, this method returns 3 for a view that has three breaks in it, even though there are six lines on the display.

Call this method before calling [IView::IGetBreakLines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetBreakLines.html) to determine the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetBreakLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLines.html)
[IView::BreakLineGap Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~BreakLineGap.html)
[IView::InsertBreak Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBreak.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
