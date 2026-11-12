---
title: "GetFirstWeldBead Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetFirstWeldBead"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstWeldBead.html"
---

# GetFirstWeldBead Method (IView)

Gets the first weld bead annotation in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstWeldBead() As WeldBead
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As WeldBead

value = instance.GetFirstWeldBead()
```

### C#

```csharp
WeldBead GetFirstWeldBead()
```

### C++/CLI

```cpp
WeldBead^ GetFirstWeldBead();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [weld bead](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldBead.html)

## VBA Syntax

See [View::GetFirstWeldBead](ms-its:sldworksapivb6.chm::/sldworks~View~GetFirstWeldBead.html).

## Examples

[Get Weld Bead Symbol Data (VBA)](Get_Weld_Bead_End_Treatment_Symbol_Data_Example_VB.htm)
[Get Weld Bead Symbol Data (VB.NET)](Get_Weld_Bead_End_Treatment_Symbol_Data_Example_VBNET.htm)
[Get Weld Bead Symbol Data (C#)](Get_Weld_Bead_End_Treatment_Symbol_Data_Example_CSharp.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IWeldBead::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead~GetNext.html)
[IView::IGetWeldBeads Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetWeldBeads.html)
[IView::GetWeldBeads Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWeldBeads.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
