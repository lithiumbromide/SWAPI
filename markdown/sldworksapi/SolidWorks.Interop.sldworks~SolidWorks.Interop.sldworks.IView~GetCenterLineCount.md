---
title: "GetCenterLineCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetCenterLineCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterLineCount.html"
---

# GetCenterLineCount Method (IView)

Gets the number of centerlines on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCenterLineCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetCenterLineCount()
```

### C#

```csharp
System.int GetCenterLineCount()
```

### C++/CLI

```cpp
System.int GetCenterLineCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of centerlines

## VBA Syntax

See [View::GetCenterLineCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetCenterLineCount.html).

## Remarks

Call this method before calling [IView::IGetCenterLines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetCenterLines.html) to determine the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetCenterLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterLines.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
