---
title: "GetCenterLines Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetCenterLines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterLines.html"
---

# GetCenterLines Method (IView)

Gets all of the centerline annotations on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCenterLines() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetCenterLines()
```

### C#

```csharp
System.object GetCenterLines()
```

### C++/CLI

```cpp
System.Object^ GetCenterLines();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [centerlines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterLine.html)

## VBA Syntax

See [View::GetCenterLines](ms-its:sldworksapivb6.chm::/sldworks~View~GetCenterLines.html).

## Examples

[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)
[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)

## Remarks

Use this method to obtain the array of centerlines all at once instead of calling [IView::GetFirstCenterLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstCenterLine.html) and then repeatedly calling [ICenterLine::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterLine~GetNext.html) to obtain the remaining centerlines in the drawing view.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetCenterLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterLineCount.html)
[IView::IGetCenterLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetCenterLines.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
