---
title: "OnSliderPositionChanged Method (IPropertyManagerPage2Handler5)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler5"
member: "OnSliderPositionChanged"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5~OnSliderPositionChanged.html"
---

# OnSliderPositionChanged Method (IPropertyManagerPage2Handler5)

Obsoleted. Superseded by [IPropertyManagerPage2Handler6::OnSliderPositionChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler6~OnSliderPositionChanged.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnSliderPositionChanged( _
   ByVal Id As System.Integer, _
   ByVal Value As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler5
Dim Id As System.Integer
Dim Value As System.Double

instance.OnSliderPositionChanged(Id, Value)
```

### C#

```csharp
void OnSliderPositionChanged(
   System.int Id,
   System.double Value
)
```

### C++/CLI

```cpp
void OnSliderPositionChanged(
   System.int Id,
   System.double Value
)
```

### Parameters

- `Id`: ID of slider control
- `Value`: Value indicating the new position of the slider

## VBA Syntax

See [PropertyManagerPage2Handler5::OnSliderPositionChanged](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler5~OnSliderPositionChanged.html).

## Remarks

Although Value is declared as a double, the value of a slider is always a long. When this method is called, Value can be cast to a long.

If [IPropertyManagerPageSlider::Style](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSlider~Style.html) is set to swPropMgrPageSliderStyle_NotifyWhileTracking, then you can use:

- IPropertyManagerPage2Handler5::OnSliderPositionChanged to receive notifications every time the position of the slider changes because the slider is being dragged.

  NOTE: This might result in numerous calls to the handler, which is fine if the add-in responds quickly to each call. However, if the add-in responds slowly, then a performance bottleneck might occur.
- [IPropertyManagerPage2Handler5::OnSliderTrackingCompleted](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler5~OnSliderTrackingCompleted.html) to receive one notification when dragging of the slider is completed.

## See Also

[IPropertyManagerPage2Handler5 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5.html)
[IPropertyManagerPage2Handler5 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler5_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
