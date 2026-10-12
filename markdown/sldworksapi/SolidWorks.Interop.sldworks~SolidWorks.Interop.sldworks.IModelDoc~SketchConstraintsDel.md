---
title: "SketchConstraintsDel Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SketchConstraintsDel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SketchConstraintsDel.html"
---

# SketchConstraintsDel Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SketchConstraintsDel](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SketchConstraintsDel.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SketchConstraintsDel( _
   ByVal ConstrInd As System.Integer, _
   ByVal IdStr As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim ConstrInd As System.Integer
Dim IdStr As System.String

instance.SketchConstraintsDel(ConstrInd, IdStr)
```

### C#

```csharp
void SketchConstraintsDel(
   System.int ConstrInd,
   System.string IdStr
)
```

### C++/CLI

```cpp
void SketchConstraintsDel(
   System.int ConstrInd,
   System.String^ IdStr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConstrInd`:
- `IdStr`:

## VBA Syntax

See [ModelDoc::SketchConstraintsDel](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SketchConstraintsDel.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
