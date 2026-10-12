---
title: "Toolbars Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "Toolbars"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~Toolbars.html"
---

# Toolbars Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::Toolbars](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~Toolbars.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub Toolbars( _
   ByVal M As System.Boolean, _
   ByVal Vw As System.Boolean, _
   ByVal SkMain As System.Boolean, _
   ByVal Sk As System.Boolean, _
   ByVal Feat As System.Boolean, _
   ByVal Constr As System.Boolean, _
   ByVal Macro As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim M As System.Boolean
Dim Vw As System.Boolean
Dim SkMain As System.Boolean
Dim Sk As System.Boolean
Dim Feat As System.Boolean
Dim Constr As System.Boolean
Dim Macro As System.Boolean

instance.Toolbars(M, Vw, SkMain, Sk, Feat, Constr, Macro)
```

### C#

```csharp
void Toolbars(
   System.bool M,
   System.bool Vw,
   System.bool SkMain,
   System.bool Sk,
   System.bool Feat,
   System.bool Constr,
   System.bool Macro
)
```

### C++/CLI

```cpp
void Toolbars(
   System.bool M,
   System.bool Vw,
   System.bool SkMain,
   System.bool Sk,
   System.bool Feat,
   System.bool Constr,
   System.bool Macro
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `M`:
- `Vw`:
- `SkMain`:
- `Sk`:
- `Feat`:
- `Constr`:
- `Macro`:

## VBA Syntax

See [ModelDoc::Toolbars](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~Toolbars.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
