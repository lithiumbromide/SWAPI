---
title: "GetWitnessEntitiesCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetWitnessEntitiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWitnessEntitiesCount.html"
---

# GetWitnessEntitiesCount Method (IView)

Gets the number of virtual sharp witness lines in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetWitnessEntitiesCount( _
   ByRef Size As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Size As System.Integer
Dim value As System.Integer

value = instance.GetWitnessEntitiesCount(Size)
```

### C#

```csharp
System.int GetWitnessEntitiesCount(
   out System.int Size
)
```

### C++/CLI

```cpp
System.int GetWitnessEntitiesCount(
   [Out] System.int Size
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Size`: Size of the virtual sharp witness line data array (see **Remarks**)

### Return Value

Number of virtual sharp witness lines in this drawing view

## VBA Syntax

See [View::GetWitnessEntitiesCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetWitnessEntitiesCount.html).

## Examples

[Get Virtual Sharp Witness Line Data (VBA)](Get_Virtual_Sharp_Witness_Line_Data_Example_VB.htm)
[Get Virtual Sharp Witness Line Data (VB.NET)](Get_Virtual_Sharp_Witness_Line_Data_Example_VBNET.htm)
[Get Virtual Sharp Witness Line Data (C#)](Get_Virtual_Sharp_Witness_Line_Data_Example_CSharp.htm)

## Remarks

Call this method to get the sizes of the arrays returned by [IView::GetWitnessGeomInfo](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetWitnessGeomInfo.html) and [IView::IGetWitnessGeomInfo](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetWitnessGeomInfo.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
