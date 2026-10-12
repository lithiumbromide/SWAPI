---
title: "EditRedo Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "EditRedo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~EditRedo.html"
---

# EditRedo Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::EditRedo](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRedo.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub EditRedo( _
   ByVal NSteps As System.UInteger _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim NSteps As System.UInteger

instance.EditRedo(NSteps)
```

### C#

```csharp
void EditRedo(
   System.uint NSteps
)
```

### C++/CLI

```cpp
void EditRedo(
   System.uint NSteps
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NSteps`:

## VBA Syntax

See [ModelDoc::EditRedo](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~EditRedo.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
