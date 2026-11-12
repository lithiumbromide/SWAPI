---
title: "GetWeldBeadCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetWeldBeadCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWeldBeadCount.html"
---

# GetWeldBeadCount Method (IView)

Gets the number of weld beads on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetWeldBeadCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetWeldBeadCount()
```

### C#

```csharp
System.int GetWeldBeadCount()
```

### C++/CLI

```cpp
System.int GetWeldBeadCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Total number of weld beads on this drawing view

## VBA Syntax

See [View::GetWeldBeadCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetWeldBeadCount.html).

## Remarks

Call this method before calling [IView::IGetWeldBeads](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetWeldBeads.html) to determine the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetWeldBeads Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWeldBeads.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
