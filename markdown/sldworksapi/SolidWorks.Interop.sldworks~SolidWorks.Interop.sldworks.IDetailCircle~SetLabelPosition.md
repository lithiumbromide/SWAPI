---
title: "SetLabelPosition Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "SetLabelPosition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetLabelPosition.html"
---

# SetLabelPosition Method (IDetailCircle)

Sets the position of the label for this detail circle.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetLabelPosition( _
   ByVal XPosition As System.Double, _
   ByVal YPosition As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim XPosition As System.Double
Dim YPosition As System.Double

instance.SetLabelPosition(XPosition, YPosition)
```

### C#

```csharp
void SetLabelPosition(
   System.double XPosition,
   System.double YPosition
)
```

### C++/CLI

```cpp
void SetLabelPosition(
   System.double XPosition,
   System.double YPosition
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XPosition`: x coordinate of the label
- `YPosition`: y coordinate of the label

## VBA Syntax

See [DetailCircle::SetLabelPostion](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~SetLabelPosition.html).

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)
[IDetailCircle::GetLabelPosition Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetLabelPosition.html)
[IDetailCircle::SetLabel Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetLabel.html)

## Availability

SOLIDWORKS 2014 SP3, Revision Number 22.3
