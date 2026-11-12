---
title: "GetDatumTargetSymCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDatumTargetSymCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumTargetSymCount.html"
---

# GetDatumTargetSymCount Method (IView)

Gets the number of datum target symbols on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDatumTargetSymCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetDatumTargetSymCount()
```

### C#

```csharp
System.int GetDatumTargetSymCount()
```

### C++/CLI

```cpp
System.int GetDatumTargetSymCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of datum target symbols

## VBA Syntax

See [View::GetDatumTargetSymCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetDatumTargetSymCount.html).

## Examples

[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)
[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)

## Remarks

Call this method before calling [IView::IGetDatumTargetSyms](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetDatumTargetSyms.html) to determine the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDatumTargetSyms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDatumTargetSyms.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
