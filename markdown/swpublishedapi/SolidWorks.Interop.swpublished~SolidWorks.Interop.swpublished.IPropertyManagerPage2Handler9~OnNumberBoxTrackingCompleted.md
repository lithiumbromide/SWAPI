---
title: "OnNumberBoxTrackingCompleted Method (IPropertyManagerPage2Handler9)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler9"
member: "OnNumberBoxTrackingCompleted"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9~OnNumberBoxTrackingCompleted.html"
---

# OnNumberBoxTrackingCompleted Method (IPropertyManagerPage2Handler9)

Called when a user finishes changing the value in the number box on a PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnNumberBoxTrackingCompleted( _
   ByVal Id As System.Integer, _
   ByVal Value As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler9
Dim Id As System.Integer
Dim Value As System.Double

instance.OnNumberBoxTrackingCompleted(Id, Value)
```

### C#

```csharp
void OnNumberBoxTrackingCompleted(
   System.int Id,
   System.double Value
)
```

### C++/CLI

```cpp
void OnNumberBoxTrackingCompleted(
   System.int Id,
   System.double Value
)
```

### Parameters

- `Id`: ID of the number box
- `Value`: Value in the number box

## VBA Syntax

See [PropertyManagerPage2Handler9::OnNumberboxTrackingCompleted](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler9~OnNumberboxTrackingCompleted.html).

## Examples

See the [IPropertyManagerPage2Handler9](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html) examples.

## Remarks

This method receives a notification when dragging or spinning of the slider is completed.

## See Also

[IPropertyManagerPage2Handler9 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html)
[IPropertyManagerPage2Handler9 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9_members.html)
[IPropertyManagerPage2Handler9::OnNumberboxChanged Method](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9~OnNumberboxChanged.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
