---
title: "IsDetachedDrawing Method (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "IsDetachedDrawing"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~IsDetachedDrawing.html"
---

# IsDetachedDrawing Method (ISwDMDocument)

Gets whether this file is a detached drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsDetachedDrawing() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
Dim value As System.Boolean

value = instance.IsDetachedDrawing()
```

### C#

```csharp
System.bool IsDetachedDrawing()
```

### C++/CLI

```cpp
System.bool IsDetachedDrawing();
```

## VBA Syntax

See [SwDMDocument::IsDetachedDrawing](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~IsDetachedDrawing.html).

## Examples

[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)

## Remarks

True if the file is detached drawing, false if not

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
