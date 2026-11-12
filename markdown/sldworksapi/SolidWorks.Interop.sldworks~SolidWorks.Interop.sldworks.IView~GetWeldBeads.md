---
title: "GetWeldBeads Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetWeldBeads"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWeldBeads.html"
---

# GetWeldBeads Method (IView)

Gets all of the weld beads on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetWeldBeads() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetWeldBeads()
```

### C#

```csharp
System.object GetWeldBeads()
```

### C++/CLI

```cpp
System.Object^ GetWeldBeads();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [weld beads](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldBead.html)

## VBA Syntax

See [View::GetWeldBeads](ms-its:sldworksapivb6.chm::/sldworks~View~GetWeldBeads.html).

## Examples

[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)
[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)

## Remarks

Use this method to obtain the array of weld beads all at once instead of calling [IView::GetFirstWeldBead](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstWeldBead.html) and then repeatedly calling [IWeldBead::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldBead~GetNext.html) to obtain the weld beads.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetWeldBeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWeldBeadCount.html)
[IView::IGetWeldBeads Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetWeldBeads.html)
[IView::GetFirstWeldBead Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstWeldBead.html)
[IWeldBead::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead~GetNext.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
