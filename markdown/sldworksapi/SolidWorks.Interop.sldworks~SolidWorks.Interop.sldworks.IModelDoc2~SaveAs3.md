---
title: "SaveAs3 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SaveAs3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SaveAs3.html"
---

# SaveAs3 Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::SaveAs](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SaveAs.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveAs3( _
   ByVal NewName As System.String, _
   ByVal SaveAsVersion As System.Integer, _
   ByVal Options As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim NewName As System.String
Dim SaveAsVersion As System.Integer
Dim Options As System.Integer
Dim value As System.Integer

value = instance.SaveAs3(NewName, SaveAsVersion, Options)
```

### C#

```csharp
System.int SaveAs3(
   System.string NewName,
   System.int SaveAsVersion,
   System.int Options
)
```

### C++/CLI

```cpp
System.int SaveAs3(
   System.String^ NewName,
   System.int SaveAsVersion,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NewName`:
- `SaveAsVersion`:
- `Options`:

## VBA Syntax

See [ModelDoc2::SaveAs3](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SaveAs3.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
