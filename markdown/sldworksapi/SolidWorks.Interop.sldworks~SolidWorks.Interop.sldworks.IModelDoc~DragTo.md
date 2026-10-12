---
title: "DragTo Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "DragTo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~DragTo.html"
---

# DragTo Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::DragTo](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~DragTo.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub DragTo( _
   ByVal Flags As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Flags As System.Integer
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double

instance.DragTo(Flags, X, Y, Z)
```

### C#

```csharp
void DragTo(
   System.int Flags,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
void DragTo(
   System.int Flags,
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Flags`:
- `X`:
- `Y`:
- `Z`:

## VBA Syntax

See [ModelDoc::DragTo](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~DragTo.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
