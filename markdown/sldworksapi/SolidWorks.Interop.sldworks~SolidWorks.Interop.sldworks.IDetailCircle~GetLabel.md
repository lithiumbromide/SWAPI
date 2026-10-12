---
title: "GetLabel Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "GetLabel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetLabel.html"
---

# GetLabel Method (IDetailCircle)

Gets the label for this detail circle.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLabel() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim value As System.String

value = instance.GetLabel()
```

### C#

```csharp
System.string GetLabel()
```

### C++/CLI

```cpp
System.String^ GetLabel();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Label for this detail circle

## VBA Syntax

See [DetailCircle::GetLabel](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~GetLabel.html).

## Examples

[Create Detail Circle and Detail View (C#)](Create_Detail_Circle_and_Detail_View_Example_CSharp.htm)
[Create Detail Circle and Detail View (VB.NET)](Create_Detail_Circle_and_Detail_View_Example_VBNET.htm)
[Create Detail Circle and Detail View (VBA)](Create_Detail_Circle_and_Detail_View_Example_VB.htm)

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)
[IDetailCircle::SetLabel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetLabel.html)
[IDetailCircle::GetLabelPosition Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetLabelPosition.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
