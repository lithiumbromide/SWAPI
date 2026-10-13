---
title: "SaveAs Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SaveAs"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SaveAs.html"
---

# SaveAs Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::SaveAs](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SaveAs.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveAs( _
   ByVal NewName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
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

See [ModelDoc2::SaveAs](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SaveAs.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
