---
title: "SetLineWidth Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "SetLineWidth"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetLineWidth.html"
---

# SetLineWidth Method (IPartDoc)

Sets the thickness or weight for the lines in the part document.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetLineWidth( _
   ByVal Width As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Width As System.Integer

instance.SetLineWidth(Width)
```

### C#

```csharp
void SetLineWidth(
   System.int Width
)
```

### C++/CLI

```cpp
void SetLineWidth(
   System.int Width
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Width`: Line thickness or weight as defined in [swLineWeights_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html)

## VBA Syntax

See [PartDoc::SetLineWidth](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~SetLineWidth.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::SetLineColor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetLineColor.html)
[IPartDoc::SetLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetLineStyle.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
