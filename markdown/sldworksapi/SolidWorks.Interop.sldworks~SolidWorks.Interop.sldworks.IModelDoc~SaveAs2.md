---
title: "SaveAs2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SaveAs2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SaveAs2.html"
---

# SaveAs2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SaveAs2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SaveAs2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveAs2( _
   ByVal NewName As System.String, _
   ByVal SaveAsVersion As System.Integer, _
   ByVal SaveAsCopy As System.Boolean, _
   ByVal Silent As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim NewName As System.String
Dim SaveAsVersion As System.Integer
Dim SaveAsCopy As System.Boolean
Dim Silent As System.Boolean
Dim value As System.Integer

value = instance.SaveAs2(NewName, SaveAsVersion, SaveAsCopy, Silent)
```

### C#

```csharp
System.int SaveAs2(
   System.string NewName,
   System.int SaveAsVersion,
   System.bool SaveAsCopy,
   System.bool Silent
)
```

### C++/CLI

```cpp
System.int SaveAs2(
   System.String^ NewName,
   System.int SaveAsVersion,
   System.bool SaveAsCopy,
   System.bool Silent
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NewName`:
- `SaveAsVersion`:
- `SaveAsCopy`:
- `Silent`:

## VBA Syntax

See [ModelDoc::SaveAs2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SaveAs2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
