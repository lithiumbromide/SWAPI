---
title: "SetToolbarVisibility Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SetToolbarVisibility"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetToolbarVisibility.html"
---

# SetToolbarVisibility Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SetToolbarVisibility](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetToolbarVisibility.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetToolbarVisibility( _
   ByVal Toolbar As System.Integer, _
   ByVal Visibility As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Toolbar As System.Integer
Dim Visibility As System.Boolean

instance.SetToolbarVisibility(Toolbar, Visibility)
```

### C#

```csharp
void SetToolbarVisibility(
   System.int Toolbar,
   System.bool Visibility
)
```

### C++/CLI

```cpp
void SetToolbarVisibility(
   System.int Toolbar,
   System.bool Visibility
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Toolbar`:
- `Visibility`:

## VBA Syntax

See [ModelDoc::SetToolbarVisibility](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SetToolbarVisibility.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
