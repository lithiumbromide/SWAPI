---
title: "OnListboxRMBUp Method (IPropertyManagerPage2Handler8)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler8"
member: "OnListboxRMBUp"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8~OnListboxRMBUp.html"
---

# OnListboxRMBUp Method (IPropertyManagerPage2Handler8)

Obsolete. Superseded by [IPropertyManagerPage2Handler9::OnListboxRMBUp](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.IPropertyManagerPage2Handler9~OnListboxRMBUp.html).

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
Dim instance As IPropertyManagerPage2Handler8
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
- `PosX`: X coordinate of the right mouse button menu
- `PosY`: Y coordinate of the right mouse button menu

## VBA Syntax

See [PropertyManagerPage2Handler8::OnListboxRMBUp](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler8~OnListboxRMBUp.html).

## See Also

[IPropertyManagerPage2Handler8 Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8.html)
[IPropertyManagerPage2Handler8 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler8_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
