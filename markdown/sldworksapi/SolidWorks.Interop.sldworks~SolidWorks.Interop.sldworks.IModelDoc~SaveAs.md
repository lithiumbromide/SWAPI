---
title: "SaveAs Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SaveAs"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SaveAs.html"
---

# SaveAs Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SaveAs](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SaveAs.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveAs( _
   ByVal NewName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim NewName As System.String
Dim value As System.Boolean

value = instance.SaveAs(NewName)
```

### C#

```csharp
System.bool SaveAs(
   System.string NewName
)
```

### C++/CLI

```cpp
System.bool SaveAs(
   System.String^ NewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NewName`:

## VBA Syntax

See [ModelDoc::SaveAs](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SaveAs.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
