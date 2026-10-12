---
title: "GetUseParentDisplayMode Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetUseParentDisplayMode"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetUseParentDisplayMode.html"
---

# GetUseParentDisplayMode Method (IView)

Gets whether the view is using its parent settings or if it is using its own local settings.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUseParentDisplayMode() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

value = instance.GetUseParentDisplayMode()
```

### C#

```csharp
System.bool GetUseParentDisplayMode()
```

### C++/CLI

```cpp
System.bool GetUseParentDisplayMode();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if view is using its parent settings, false if using its own local settings

## VBA Syntax

See [View::GetUseParentDisplayMode](ms-its:sldworksapivb6.chm::/sldworks~View~GetUseParentDisplayMode.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDisplayMode2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayMode2.html)
[IView::SetDisplayMode3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayMode3.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
