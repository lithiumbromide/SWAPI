---
title: "BreakLineGap Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "BreakLineGap"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~BreakLineGap.html"
---

# BreakLineGap Property (IView)

Gets or sets the width of the gap for a break line.

## Syntax

### Visual Basic (Declaration)

```vb
Property BreakLineGap As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Double

instance.BreakLineGap = value

value = instance.BreakLineGap
```

### C#

```csharp
System.double BreakLineGap {get; set;}
```

### C++/CLI

```cpp
property System.double BreakLineGap {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value for gap

## VBA Syntax

See [View::BreakLineGap](ms-its:sldworksapivb6.chm::/sldworks~View~BreakLineGap.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[GetBreakLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLineCount.html)
[IView::GetBreakLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLineInfo.html)
[IView::GetBreakLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLines.html)
[IView::IGetBreakLineInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBreakLineInfo.html)
[IView::IGetBreakLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBreakLines.html)
[IView::InsertBreak Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBreak.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
