---
title: "SetLineStyle Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "SetLineStyle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetLineStyle.html"
---

# SetLineStyle Method (IPartDoc)

Sets the style or font for the lines in the part document.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetLineStyle( _
   ByVal StyleName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim StyleName As System.String

instance.SetLineStyle(StyleName)
```

### C#

```csharp
void SetLineStyle(
   System.string StyleName
)
```

### C++/CLI

```cpp
void SetLineStyle(
   System.String^ StyleName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StyleName`: Style or font for the line as defined in [swLineStyles_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineStyles_e.html)

## VBA Syntax

See [PartDoc::SetLineStyle](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~SetLineStyle.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::SetLineWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetLineWidth.html)
[IPartDoc::SetLineColor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetLineColor.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
