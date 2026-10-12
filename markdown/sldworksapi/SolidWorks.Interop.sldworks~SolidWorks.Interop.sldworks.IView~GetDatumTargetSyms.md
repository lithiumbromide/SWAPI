---
title: "GetDatumTargetSyms Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDatumTargetSyms"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumTargetSyms.html"
---

# GetDatumTargetSyms Method (IView)

Gets all of the datum target symbols on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDatumTargetSyms() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetDatumTargetSyms()
```

### C#

```csharp
System.object GetDatumTargetSyms()
```

### C++/CLI

```cpp
System.Object^ GetDatumTargetSyms();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [datum target symbols](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTargetSym.html)

## VBA Syntax

See [View::GetDatumTargetSyms](ms-its:sldworksapivb6.chm::/sldworks~View~GetDatumTargetSyms.html).

## Examples

[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)
[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)
[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)

## Remarks

Use this method to obtain the array of datum target symbols all at once instead of calling [IView::GetFirstDatumTargetSym](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstDatumTargetSym.html) and then repeatedly calling [IDatumTargetSym::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTargetSym~GetNext.html) to obtain the remaining datum target symbols on this drawing view.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDatumTargetSymCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumTargetSymCount.html)
[IView::IGetDatumTargetSyms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDatumTargetSyms.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
