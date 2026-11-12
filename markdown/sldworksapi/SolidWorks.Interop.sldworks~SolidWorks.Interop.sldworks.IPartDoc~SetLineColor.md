---
title: "SetLineColor Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "SetLineColor"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetLineColor.html"
---

# SetLineColor Method (IPartDoc)

Sets the color for the lines in the part document.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetLineColor( _
   ByVal Color As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Color As System.Integer

instance.SetLineColor(Color)
```

### C#

```csharp
void SetLineColor(
   System.int Color
)
```

### C++/CLI

```cpp
void SetLineColor(
   System.int Color
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Color`: Color definition as a COLORREF

## VBA Syntax

See [PartDoc::SetLineColor](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~SetLineColor.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::SetLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetLineStyle.html)
[IPartDoc::SetLineWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetLineWidth.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
