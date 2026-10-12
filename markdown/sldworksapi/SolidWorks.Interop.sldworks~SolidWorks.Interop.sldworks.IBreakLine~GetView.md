---
title: "GetView Method (IBreakLine)"
project: "SOLIDWORKS API Help"
interface: "IBreakLine"
member: "GetView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~GetView.html"
---

# GetView Method (IBreakLine)

Gets the drawing view for this break line.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetView() As View
```

### Visual Basic (Usage)

```vb
Dim instance As IBreakLine
Dim value As View

value = instance.GetView()
```

### C#

```csharp
View GetView()
```

### C++/CLI

```cpp
View^ GetView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [IView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) object

## VBA Syntax

See [BreakLine::GetView](ms-its:sldworksapivb6.chm::/sldworks~BreakLine~GetView.html).

## Remarks

A drawing view can have several breaks. To get all of the breaks in a drawing view, use [IView::GetBreakLines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetBreakLines.html).

## See Also

[IBreakLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine.html)
[IBreakLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
