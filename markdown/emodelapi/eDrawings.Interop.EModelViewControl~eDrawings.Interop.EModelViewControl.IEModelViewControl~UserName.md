---
title: "UserName Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "UserName"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~UserName.html"
---

# UserName Property (IEModelViewControl)

Sets the user name needed to open a model downloaded from a server that requires authentication.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property UserName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl

instance.UserName = value
```

### C#

```csharp
System.string UserName {set;}
```

### C++/CLI

```cpp
property System.String^ UserName {
   void set (    System.String^ value);
}
```

### Property Value

User name

## VBA Syntax

See [EModelViewControl::UserName](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~UserName.html).

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::OpenDoc Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~OpenDoc.html)
[IEModelViewControl::OpenMarkupFile Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~OpenMarkupFile.html)
[IEModelViewControl::Password Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~Password.html)

## Availability

eDrawings API 2005 SP0
