---
title: "GetLabelPosition Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "GetLabelPosition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetLabelPosition.html"
---

# GetLabelPosition Method (IDetailCircle)

Gets the position of the label of this detail circle.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetLabelPosition( _
   ByRef XPosition As System.Double, _
   ByRef YPosition As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim XPosition As System.Double
Dim YPosition As System.Double

instance.GetLabelPosition(XPosition, YPosition)
```

### C#

```csharp
void GetLabelPosition(
   out System.double XPosition,
   out System.double YPosition
)
```

### C++/CLI

```cpp
void GetLabelPosition(
   [Out] System.double XPosition,
   [Out] System.double YPosition
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XPosition`: x coordinate of the label
- `YPosition`: y coordinate of the label

## VBA Syntax

See [DetailCircle::GetLabelPostion](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~GetLabelPosition.html).

## Examples

[Create Detail Circle and Detail View (VBA)](Create_Detail_Circle_and_Detail_View_Example_VB.htm)
[Create Detail Circle and Detail View (VB.NET)](Create_Detail_Circle_and_Detail_View_Example_VBNET.htm)
[Create Detail Circle and Detail View (C#)](Create_Detail_Circle_and_Detail_View_Example_CSharp.htm)

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)
[IDetailCircle::SetLabelPosition Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetLabelPosition.html)
[IDetailCircle::GetLabel Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetLabel.html)

## Availability

SOLIDWORKS 2014 SP3, Revision Number 22.3
