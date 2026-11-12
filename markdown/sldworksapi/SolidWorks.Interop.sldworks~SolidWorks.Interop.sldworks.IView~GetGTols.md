---
title: "GetGTols Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetGTols"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetGTols.html"
---

# GetGTols Method (IView)

Gets all of the geometric tolerances on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGTols() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetGTols()
```

### C#

```csharp
System.object GetGTols()
```

### C++/CLI

```cpp
System.Object^ GetGTols();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [geometric tolerances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol.html)

## VBA Syntax

See [View::GetGTols](ms-its:sldworksapivb6.chm::/sldworks~View~GetGTols.html).

## Examples

[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)
[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)

## Remarks

Use this method to obtain the array of geometric tolerances all at once instead of calling [IView::GetFirstGTOL](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstGTOL.html) and then repeatedly calling [IGtol::GetNextGTOL](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~GetNextGTOL.html) to obtain the remaining geometric tolerances in the drawing view.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetGTolCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetGTolCount.html)
[IView::IGetGTols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetGTols.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
