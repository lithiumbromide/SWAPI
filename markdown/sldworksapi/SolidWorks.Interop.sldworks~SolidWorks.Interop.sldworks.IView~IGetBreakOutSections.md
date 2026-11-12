---
title: "IGetBreakOutSections Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetBreakOutSections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBreakOutSections.html"
---

# IGetBreakOutSections Method (IView)

Gets all of the broken-out sections in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBreakOutSections( _
   ByVal Count As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Count As System.Integer
Dim value As Feature

value = instance.IGetBreakOutSections(Count)
```

### C#

```csharp
Feature IGetBreakOutSections(
   System.int Count
)
```

### C++/CLI

```cpp
Feature^ IGetBreakOutSections(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of broken-out sections in this view

### Return Value

- In-process, unmanaged C++: Pointer to an array of broken-out section [features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IView::GetBreakOutSectionCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetBreakOutSectionCount.html) to get the value for Count.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetBreakOutSections Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakOutSections.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
