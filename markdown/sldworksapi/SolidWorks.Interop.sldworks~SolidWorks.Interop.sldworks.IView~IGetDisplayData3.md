---
title: "IGetDisplayData3 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetDisplayData3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDisplayData3.html"
---

# IGetDisplayData3 Method (IView)

Gets the the [IDisplayData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData.html) object for this drawing view containing only those model items that are visible in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDisplayData3() As DisplayData
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As DisplayData

value = instance.IGetDisplayData3()
```

### C#

```csharp
DisplayData IGetDisplayData3()
```

### C++/CLI

```cpp
DisplayData^ IGetDisplayData3();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IDisplayData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData.html) object

## VBA Syntax

See [View::IGetDisplayData3](ms-its:sldworksapivb6.chm::/sldworks~View~IGetDisplayData3.html).

## Remarks

The data kept with the [IDisplayData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData.html) object is strictly for display purposes and allows you to recreate unintelligent geometry. It does not provide associations or detailed information about the geometry.

This method supersedes the now obsolete [IView::IGetDisplayData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetDisplayData2.html) and should be used in its place. The previous version of this method returned model items that were not imported to the drawing view and, therefore, not visible in the drawing view.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDisplayData3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayData3.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
