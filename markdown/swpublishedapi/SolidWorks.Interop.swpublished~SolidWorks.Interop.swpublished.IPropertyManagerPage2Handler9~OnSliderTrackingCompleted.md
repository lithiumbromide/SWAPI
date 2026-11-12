---
title: "OnSliderTrackingCompleted Method (IPropertyManagerPage2Handler9)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler9"
member: "OnSliderTrackingCompleted"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9~OnSliderTrackingCompleted.html"
---

# OnSliderTrackingCompleted Method (IPropertyManagerPage2Handler9)

Called when a user finishes dragging a [slider control](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSlider.html) on this PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnSliderTrackingCompleted( _
   ByVal Id As System.Integer, _
   ByVal Value As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler9
Dim Id As System.Integer
Dim Value As System.Double

instance.OnSliderTrackingCompleted(Id, Value)
```

### C#

```csharp
void OnSliderTrackingCompleted(
   System.int Id,
   System.double Value
)
```

### C++/CLI

```cpp
void OnSliderTrackingCompleted(
   System.int Id,
   System.double Value
)
```

### Parameters

- `Id`: ID of the slider control
- `Value`: Value indicating the new position of the slider

## VBA Syntax

See [PropertyManagerPage2Handler9::OnSliderTrackingCompleted](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler9~OnSliderTrackingCompleted.html).

## Examples

See the [IPropertyManagerPage2Handler9](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html) examples.

## Remarks

Although Value is declared as a double, the value of a slider is always a long. When this method is called, Value can be cast to a long.

If [IPropertyManagerPageSlider::Style](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSlider~Style.html) is set to swPropMgrPageSliderStyle_NotifyWhileTracking, then you can use:

- IPropertyManagerPage2Handler9::OnSliderTrackingCompleted to receive one notification when dragging of the slider is completed.

- [IPropertyManagerPage2Handler9::OnSliderPositionChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnSliderPositionChanged.html) to receive notifications every time the position of the slider changes because the slider is being dragged.

  NOTE: This might result in numerous calls to the handler, which is fine if the add-in responds quickly to each call. However, if the add-in responds slowly, then a performance bottleneck might occur.

## See Also

[IPropertyManagerPage2Handler9 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html)
[IPropertyManagerPage2Handler9 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
