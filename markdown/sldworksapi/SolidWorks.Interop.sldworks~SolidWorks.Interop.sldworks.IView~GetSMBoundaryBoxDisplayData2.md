---
title: "GetSMBoundaryBoxDisplayData2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetSMBoundaryBoxDisplayData2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSMBoundaryBoxDisplayData2.html"
---

# GetSMBoundaryBoxDisplayData2 Method (IView)

Gets the boundary-box sketch display data of a flat-pattern drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSMBoundaryBoxDisplayData2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetSMBoundaryBoxDisplayData2()
```

### C#

```csharp
System.object GetSMBoundaryBoxDisplayData2()
```

### C++/CLI

```cpp
System.Object^ GetSMBoundaryBoxDisplayData2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Display data](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData.html) of boundary-box sketch of a flat-pattern drawing view

## VBA Syntax

See [View::GetSMBoundaryBoxDisplayData2](ms-its:sldworksapivb6.chm::/sldworks~View~GetSMBoundaryBoxDisplayData2.html).

## Examples

[Get Number of Lines in Flat-pattern Drawing View's Boundary-box Sketch (VBA)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_VB.htm)
[Get Number of Lines in Flat-pattern Drawing View's Boundary-box Sketch (VB.NET)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_VBNET.htm)
[Get Number of Lines in Flat-pattern Drawing View's Boundary-box Sketch (C#)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_CSharp.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
