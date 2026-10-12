---
title: "OnSliderTrackingCompleted Method (IPropertyManagerPage2Handler8)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler8"
member: "OnSliderTrackingCompleted"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8~OnSliderTrackingCompleted.html"
---

# OnSliderTrackingCompleted Method (IPropertyManagerPage2Handler8)

Obsolete. Superseded by [IPropertyManagerPage2Handler9::OnSliderTrackingCompleted](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnSliderTrackingCompleted.html).

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
Dim instance As IPropertyManagerPage2Handler8
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

- `Id`: ID of this slider control
- `Value`: Value indicating the new position of the slider

## VBA Syntax

See [PropertyManagerPage2Handler8::OnSliderTrackingCompleted](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler8~OnSliderTrackingCompleted.html).

## Remarks

Although Value is declared as a double, the value of a slider is always a long. When this method is called, Value can be cast to a long.

If [IPropertyManagerPageSlider::Style](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageSlider~Style.html) is set to swPropMgrPageSliderStyle_NotifyWhileTracking, then you can use:

- IPropertyManagerPage2Handler8::OnSliderTrackingCompleted to receive one notification when dragging of the slider is completed.

- [IPropertyManagerPage2Handler8::OnSliderPositionChanged](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler8~OnSliderPositionChanged.html) to receive notifications every time the position of the slider changes because the slider is being dragged.

  NOTE: This might result in numerous calls to the handler, which is fine if the add-in responds quickly to each call. However, if the add-in responds slowly, then a performance bottleneck might occur.

## See Also

[IPropertyManagerPage2Handler8 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8.html)
[IPropertyManagerPage2Handler8 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
