---
title: "GetStyle Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "GetStyle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetStyle.html"
---

# GetStyle Method (IDetailCircle)

Gets the style of this detail circle.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStyle() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim value As System.Integer

value = instance.GetStyle()
```

### C#

```csharp
System.int GetStyle()
```

### C++/CLI

```cpp
System.int GetStyle();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Detail circle style as defined in [swDetViewStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDetViewStyle_e.html)

## VBA Syntax

See [DetailCircle::GetStyle](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~GetStyle.html).

## Examples

[Create Detail Circle and Detail View (C#)](Create_Detail_Circle_and_Detail_View_Example_CSharp.htm)
[Create Detail Circle and Detail View (VB.NET)](Create_Detail_Circle_and_Detail_View_Example_VBNET.htm)
[Create Detail Circle and Detail View (VBA)](Create_Detail_Circle_and_Detail_View_Example_VB.htm)

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)
[IDetailCircle::SetStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetStyle.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
