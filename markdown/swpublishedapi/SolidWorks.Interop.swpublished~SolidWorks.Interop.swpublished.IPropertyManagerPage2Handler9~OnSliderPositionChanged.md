---
title: "OnSliderPositionChanged Method (IPropertyManagerPage2Handler9)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler9"
member: "OnSliderPositionChanged"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9~OnSliderPositionChanged.html"
---

# OnSliderPositionChanged Method (IPropertyManagerPage2Handler9)

Called whenever the user changes the position of a [slider control](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSlider.html) on this PropertyManager page.

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
Dim instance As IPropertyManagerPage2Handler9
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

- `Id`: ID of the slider control
- `Value`: Value indicating the new position of the slider

### Return Value

Although Value is declared as a double, the value of a slider is always a long. When this method is called, Value can be cast to a long.

If [IPropertyManagerPageSlider::Style](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSlider~Style.html) is set to swPropMgrPageSliderStyle_NotifyWhileTracking, then you can use:

- IPropertyManagerPage2Handler9::OnSliderPositionChanged to receive notifications every time the position of the slider changes because the slider is being dragged.

  NOTE: This might result in numerous calls to the handler, which is fine if the add-in responds quickly to each call. However, if the add-in responds slowly, then a performance bottleneck might occur.
- [IPropertyManagerPage2Handler9::OnSliderTrackingCompleted](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnSliderTrackingCompleted.html) to receive one notification when dragging of the slider is completed.

## VBA Syntax

See [PropertyManagerPage2Handler9::OnSliderPositionChanged](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler9~OnSliderPositionChanged.html).

## Examples

See the [IPropertyManagerPage2Handler9](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html) examples.

## See Also

[IPropertyManagerPage2Handler9 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html)
[IPropertyManagerPage2Handler9 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
