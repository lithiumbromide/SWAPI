---
title: "IsLightweight Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IsLightweight"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsLightweight.html"
---

# IsLightweight Method (IView)

Gets whether the drawing view is lightweight.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsLightweight() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

value = instance.IsLightweight()
```

### C#

```csharp
System.bool IsLightweight()
```

### C++/CLI

```cpp
System.bool IsLightweight();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if lightweight, false if not

## VBA Syntax

See [View::IsLightweight](ms-its:sldworksapivb6.chm::/sldworks~View~IsLightweight.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::SetLightweightToResolved Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetLightweightToResolved.html)
[IView::SetResolvedToLightweight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetResolvedToLightweight.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
