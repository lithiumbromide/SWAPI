---
title: "OnSliderTrackingCompleted Method (IPropertyManagerPage2Handler7)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler7"
member: "OnSliderTrackingCompleted"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7~OnSliderTrackingCompleted.html"
---

# OnSliderTrackingCompleted Method (IPropertyManagerPage2Handler7)

Obsoleted. Superseded by [IPropertyManagerPage2Handler8::OnSliderTrackingCompleted](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnSliderTrackingCompleted.html).

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
Dim instance As IPropertyManagerPage2Handler7
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

- `Id`: ID of slider control
- `Value`: Value indicating the new position of the slider

## VBA Syntax

See [PropertyManagerPage2Handler7::OnSliderTrackingCompleted](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler7~OnSliderTrackingCompleted.html).

## Remarks

Although Value is declared as a double, the value of a slider is always a long. When this method is called, Value can be cast to a long.

If [IPropertyManagerPageSlider::Style](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSlider~Style.html) is set to swPropMgrPageSliderStyle_NotifyWhileTracking, then you can use:

- IPropertyManagerPage2Handler7::OnSliderTrackingCompleted to receive one notification when dragging of the slider is completed.

- [IPropertyManagerPage2Handler7::OnSliderPositionChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler7~OnSliderPositionChanged.html) to receive notifications every time the position of the slider changes because the slider is being dragged.

  NOTE: This might result in numerous calls to the handler, which is fine if the add-in responds quickly to each call. However, if the add-in responds slowly, then a performance bottleneck might occur.

## See Also

[IPropertyManagerPage2Handler7 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7.html)
[IPropertyManagerPage2Handler7 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler7_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
