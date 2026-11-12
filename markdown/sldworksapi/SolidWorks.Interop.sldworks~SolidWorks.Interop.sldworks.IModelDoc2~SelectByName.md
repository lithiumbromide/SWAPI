---
title: "SelectByName Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SelectByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectByName.html"
---

# SelectByName Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html).

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
Dim instance As IModelDoc2
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

See [ModelDoc2::SelectByName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SelectByName.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
