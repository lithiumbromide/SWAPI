---
title: "SaveAs3 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SaveAs3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SaveAs3.html"
---

# SaveAs3 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SaveAs3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SaveAs3.html).

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
Dim instance As IModelDoc
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

See [ModelDoc::SaveAs3](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SaveAs3.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
