---
title: "GetDisplay Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "GetDisplay"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetDisplay.html"
---

# GetDisplay Method (IDetailCircle)

Gets the type of circle or profile used to create the detail.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplay() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim value As System.Integer

value = instance.GetDisplay()
```

### C#

```csharp
System.int GetDisplay()
```

### C++/CLI

```cpp
System.int GetDisplay();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Profile type as defined in [swDetCircleShowType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDetCircleShowType_e.html)

## VBA Syntax

See [DetailCircle::GetDisplay](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~GetDisplay.html).

## Examples

[Create Detail Circle and Detail View (C#)](Create_Detail_Circle_and_Detail_View_Example_CSharp.htm)
[Create Detail Circle and Detail View (VB.NET)](Create_Detail_Circle_and_Detail_View_Example_VBNET.htm)
[Create Detail Circle and Detail View (VBA)](Create_Detail_Circle_and_Detail_View_Example_VB.htm)

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)
[IDetailCircle::SetDisplay Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetDisplay.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
