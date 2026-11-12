---
title: "FileName Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "FileName"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~FileName.html"
---

# FileName Property (IEModelViewControl)

Gets the path and name of the file to open or the file name of the currently displayed file.

## Syntax

### Visual Basic (Declaration)

```vb
Property FileName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim value As System.String

instance.FileName = value

value = instance.FileName
```

### C#

```csharp
System.string FileName {get; set;}
```

### C++/CLI

```cpp
property System.String^ FileName {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Fully qualified path and file name (see Remarks)

## VBA Syntax

See [EModelViewControl::FileName](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~FileName.html).

## Remarks

Syntax for specifying the file name:

| Access | Example |
| --- | --- |
| Windows local file | C:\temp\myAssembly.easm |
| Windows network path | //myServer//mySharedFolder//myDrawing.edrw (Assume that the folder is shared and note the use of the forward slashes) |
| URL | Supported: http://myHost/MyFolder/MyPart.eprt Not supported: file:///C:/temp\myDwg.dwg |

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2005 SP0
