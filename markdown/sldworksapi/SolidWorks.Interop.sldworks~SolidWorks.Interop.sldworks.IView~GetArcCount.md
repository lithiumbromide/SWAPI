---
title: "GetArcCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetArcCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetArcCount.html"
---

# GetArcCount Method (IView)

Gets the number of arcs in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArcCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetArcCount()
```

### C#

```csharp
System.int GetArcCount()
```

### C++/CLI

```cpp
System.int GetArcCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of arcs

## VBA Syntax

See [View::GetArcCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetArcCount.html).

## Examples

[Get Polylines Information (VBA)](Get_Polylines_Information_Example_VB.htm)

## Remarks

Call this method before [IView::GetArcs4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetArcs4.html) to determine the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetArcs4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetArcs4.html)
