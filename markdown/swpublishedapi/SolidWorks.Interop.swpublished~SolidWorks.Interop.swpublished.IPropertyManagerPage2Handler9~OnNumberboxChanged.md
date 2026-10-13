---
title: "OnNumberboxChanged Method (IPropertyManagerPage2Handler9)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler9"
member: "OnNumberboxChanged"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9~OnNumberboxChanged.html"
---

# OnNumberboxChanged Method (IPropertyManagerPage2Handler9)

Called when a user changes the value in the number box on a PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnNumberboxChanged( _
   ByVal Id As System.Integer, _
   ByVal Value As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler9
Dim Id As System.Integer
Dim Value As System.Double

instance.OnNumberboxChanged(Id, Value)
```

### C#

```csharp
void OnNumberboxChanged(
   System.int Id,
   System.double Value
)
```

### C++/CLI

```cpp
void OnNumberboxChanged(
   System.int Id,
   System.double Value
)
```

### Parameters

- `Id`: ID of the number box
- `Value`: Value in the number box

## VBA Syntax

See [PropertyManagerPage2Handler9::OnNumberboxChanged](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler9~OnNumberboxChanged.html).

## Examples

See the [IPropertyManagerPage2Handler9](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html) examples.

## Remarks

By default, this method receives a notification every time the value in the number box changes while the slider is being dragged or spun. Numerous notifications result in numerous calls to the handler, which is okay if your application responds quickly to each call. However, if your application responds slowly, then a performance bottleneck might occur.

Set [IPropertyManagerPageNumberbox::Style](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageNumberbox~Style.html) to [swPropMgrPageNumberBoxStyle_e.swPropMgrPageNumberBoxStyle_SupressNotifyWhileTracking](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropMgrPageNumberBoxStyle_e.html) to receive only one notification while the slider is being dragged or spun. [IPropertyManagerPage2Handler9::OnNumberboxTrackingCompleted](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnNumberBoxTrackingCompleted.html) receives a notification when dragging or spinning of the slider is completed.

## See Also

[IPropertyManagerPage2Handler9 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html)
[IPropertyManagerPage2Handler9 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
