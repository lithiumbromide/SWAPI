---
title: "IsMarkupModified Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "IsMarkupModified"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~IsMarkupModified.html"
---

# IsMarkupModified Property (IEModelViewControl)

Gets whether the markup file was modified.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsMarkupModified As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.Boolean

value = instance.IsMarkupModified
```

### C#

```csharp
System.bool IsMarkupModified {get;}
```

### C++/CLI

```cpp
property System.bool IsMarkupModified {
   System.bool get();
}
```

### Property Value

True if markup file was modified, false if not

## VBA Syntax

See [EModelViewControl::IsMarkupModified](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~IsMarkupModified.html).

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::OpenMarkupFile Method](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~OpenMarkupFile.html)

## Availability

eDrawings API 2005 SP0
