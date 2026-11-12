---
title: "IsPerspectiveView Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IsPerspectiveView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsPerspectiveView.html"
---

# IsPerspectiveView Method (IView)

Gets whether this drawing view is showing a perspective view of the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsPerspectiveView() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

value = instance.IsPerspectiveView()
```

### C#

```csharp
System.bool IsPerspectiveView()
```

### C++/CLI

```cpp
System.bool IsPerspectiveView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if perspective view is shown, false if not

## VBA Syntax

See [View::IsPerspectiveView](ms-its:sldworksapivb6.chm::/sldworks~View~IsPerspectiveView.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
