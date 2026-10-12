---
title: "GetGTolCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetGTolCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetGTolCount.html"
---

# GetGTolCount Method (IView)

Gets the number of geometric tolerances in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGTolCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetGTolCount()
```

### C#

```csharp
System.int GetGTolCount()
```

### C++/CLI

```cpp
System.int GetGTolCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of geometric tolerances

## VBA Syntax

See [View::GetGTolCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetGTolCount.html)

## Examples

[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)
[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)

## Remarks

Call this method before calling [IView::IGetGTols](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetGTols.html) to determine the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetGTols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetGTols.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
