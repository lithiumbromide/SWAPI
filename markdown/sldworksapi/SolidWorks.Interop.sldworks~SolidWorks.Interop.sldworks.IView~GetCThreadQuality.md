---
title: "GetCThreadQuality Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetCThreadQuality"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCThreadQuality.html"
---

# GetCThreadQuality Method (IView)

Gets the cosmetic thread display quality in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCThreadQuality() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

value = instance.GetCThreadQuality()
```

### C#

```csharp
System.bool GetCThreadQuality()
```

### C++/CLI

```cpp
System.bool GetCThreadQuality();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if precision quality, false if draft quality

## VBA Syntax

See [View::GetCThreadQuality](ms-its:sldworksapivb6.chm::/sldworks~View~GetCThreadQuality.html).

## Examples

See the [IView::SetDisplayMode4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayMode4.html) examples.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::SetDisplayMode4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayMode4.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
