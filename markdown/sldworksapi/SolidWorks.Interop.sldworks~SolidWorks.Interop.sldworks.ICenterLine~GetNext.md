---
title: "GetNext Method (ICenterLine)"
project: "SOLIDWORKS API Help"
interface: "ICenterLine"
member: "GetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine~GetNext.html"
---

# GetNext Method (ICenterLine)

Gets the next centerline in this [drawing view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNext() As Centerline
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterLine
Dim value As Centerline

value = instance.GetNext()
```

### C#

```csharp
Centerline GetNext()
```

### C++/CLI

```cpp
Centerline^ GetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Next [centerline](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterLine.html) in this drawing view

## VBA Syntax

See [CenterLine::GetNext](ms-its:sldworksapivb6.chm::/sldworks~CenterLine~GetNext.html).

## Examples

[Get Centerlines in Drawing (C#)](Get_Centerlines_in_Drawing_Example_CSharp.htm)
[Get Centerlines in Drawing (VB.NET)](Get_Centerlines_in_Drawing_Example_VBNET.htm)
[Get Centerlines in Drawing (VBA)](Get_Centerlines_in_Drawing_Example_VB.htm)

## See Also

[ICenterLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine.html)
[ICenterLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine_members.html)
[IView::GetFirstCenterLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCenterLine.html)

## Availability

SOLIDWORKS 2003 SP1, Revision Number 11.1
