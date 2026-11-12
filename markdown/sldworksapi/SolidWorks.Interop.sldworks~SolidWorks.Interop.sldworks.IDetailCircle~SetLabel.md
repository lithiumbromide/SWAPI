---
title: "SetLabel Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "SetLabel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetLabel.html"
---

# SetLabel Method (IDetailCircle)

Sets the label for this detail circle.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLabel( _
   ByVal Label As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim Label As System.String
Dim value As System.Boolean

value = instance.SetLabel(Label)
```

### C#

```csharp
System.bool SetLabel(
   System.string Label
)
```

### C++/CLI

```cpp
System.bool SetLabel(
   System.String^ Label
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Label`: Label for this detail view

### Return Value

True if label is set, false if not

## VBA Syntax

See [DetailCircle::SetLabel](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~SetLabel.html).

## Remarks

Setting the detail circle label also updates the detail view label.

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)
[IDetailCircle::GetLabel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetLabel.html)
[IDrawingDoc::CreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDetailViewAt3.html)
[IDrawingDoc::ICreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDetailViewAt3.html)
[IDetailCircle::SetLabelPosition Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetLabelPosition.html)

## Availability

SOLIDWORKS 2004 SP1, Revision Number 12.1
