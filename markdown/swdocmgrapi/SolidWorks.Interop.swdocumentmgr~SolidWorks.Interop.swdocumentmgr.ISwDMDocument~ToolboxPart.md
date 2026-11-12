---
title: "ToolboxPart Property (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "ToolboxPart"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~ToolboxPart.html"
---

# ToolboxPart Property (ISwDMDocument)

Gets or sets whether this file is a SOLIDWORKS Toolbox file.

## Syntax

### Visual Basic (Declaration)

```vb
Property ToolboxPart As SwDmToolboxPartType
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
Dim value As SwDmToolboxPartType

instance.ToolboxPart = value

value = instance.ToolboxPart
```

### C#

```csharp
SwDmToolboxPartType ToolboxPart {get; set;}
```

### C++/CLI

```cpp
property SwDmToolboxPartType ToolboxPart {
   SwDmToolboxPartType get();
   void set (    SwDmToolboxPartType value);
}
```

### Property Value

Type of SOLIDWORKS Toolbox part as defined by [SwDmToolboxPartType](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmToolboxPartType.html)

## VBA Syntax

See [SwDMDocument::ToolboxPart](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~ToolboxPart.html).

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
