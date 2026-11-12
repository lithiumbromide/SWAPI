---
title: "OnListboxRMBUp Method (IPropertyManagerPage2Handler9)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler9"
member: "OnListboxRMBUp"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9~OnListboxRMBUp.html"
---

# OnListboxRMBUp Method (IPropertyManagerPage2Handler9)

Called when the right-mouse button is released in a list box on this PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Sub OnListboxRMBUp( _
   ByVal Id As System.Integer, _
   ByVal PosX As System.Integer, _
   ByVal PosY As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler9
Dim Id As System.Integer
Dim PosX As System.Integer
Dim PosY As System.Integer

instance.OnListboxRMBUp(Id, PosX, PosY)
```

### C#

```csharp
void OnListboxRMBUp(
   System.int Id,
   System.int PosX,
   System.int PosY
)
```

### C++/CLI

```cpp
void OnListboxRMBUp(
   System.int Id,
   System.int PosX,
   System.int PosY
)
```

### Parameters

- `Id`: ID of the list box
- `PosX`: X coordinate of the right-mouse button menu
- `PosY`: Y coordinate of the right-mouse button menu

## VBA Syntax

See [PropertyManagerPage2Handler9::OnListboxRMBUp](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler9~OnListboxRMBUp.html).

## Examples

See the [IPropertyManagerPage2Handler9](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html) examples.

## See Also

[IPropertyManagerPage2Handler9 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html)
[IPropertyManagerPage2Handler9 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
