---
title: "SelectByName Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SelectByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SelectByName.html"
---

# SelectByName Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SelectByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SelectByName.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SelectByName( _
   ByVal Flags As System.Integer, _
   ByVal IdStr As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Flags As System.Integer
Dim IdStr As System.String

instance.SelectByName(Flags, IdStr)
```

### C#

```csharp
void SelectByName(
   System.int Flags,
   System.string IdStr
)
```

### C++/CLI

```cpp
void SelectByName(
   System.int Flags,
   System.String^ IdStr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Flags`:
- `IdStr`:

## VBA Syntax

See [ModelDoc::SelectByName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SelectByName.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
