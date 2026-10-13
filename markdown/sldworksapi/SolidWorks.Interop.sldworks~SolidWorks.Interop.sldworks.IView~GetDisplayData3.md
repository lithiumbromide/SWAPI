---
title: "GetDisplayData3 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDisplayData3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayData3.html"
---

# GetDisplayData3 Method (IView)

Obsolete. Superseded by [IView::GetDisplayData4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayData4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayData3() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetDisplayData3()
```

### C#

```csharp
System.object GetDisplayData3()
```

### C++/CLI

```cpp
System.Object^ GetDisplayData3();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IDisplayData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData.html) object

## VBA Syntax

See [View::GetDisplayData3](ms-its:sldworksapivb6.chm::/sldworks~View~GetDisplayData3.html).

## Remarks

The data kept with the [IDisplayData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData.html) object is strictly for display purposes and allows you to recreate unintelligent geometry. It does not provide associations or detailed information about the geometry.

This method supersedes the now obsolete [IView::GetDisplayData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetDisplayData2.html) and should be used in its place. The previous version of this method returned model items that were not imported to the drawing view and, therefore, not visible in the drawing view.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IGetDisplayData3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDisplayData3.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
