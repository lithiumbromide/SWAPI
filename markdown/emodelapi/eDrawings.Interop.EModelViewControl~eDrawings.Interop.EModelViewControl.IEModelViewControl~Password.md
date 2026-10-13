---
title: "Password Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "Password"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~Password.html"
---

# Password Property (IEModelViewControl)

Sets the password needed to open a model downloaded from a server that requires authentication.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property Password As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl

instance.Password = value
```

### C#

```csharp
System.string Password {set;}
```

### C++/CLI

```cpp
property System.String^ Password {
   void set (    System.String^ value);
}
```

### Property Value

Password needed to open a model downloaded from a server that requires authentication

## VBA Syntax

See [EModelViewControl::Password](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~Password.html).

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::OpenDoc Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~OpenDoc.html)
[IEModelViewControl::OpenMarkupFile Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~OpenMarkupFile.html)
[IEModelViewControl::UserName Property](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~UserName.html)

## Availability

eDrawings API 2005 SP0
