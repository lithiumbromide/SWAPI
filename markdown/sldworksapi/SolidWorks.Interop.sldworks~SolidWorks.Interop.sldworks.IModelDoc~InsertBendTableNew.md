---
title: "InsertBendTableNew Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertBendTableNew"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertBendTableNew.html"
---

# InsertBendTableNew Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertBendTableNew](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertBendTableNew.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertBendTableNew( _
   ByVal FileName As System.String, _
   ByVal Units As System.String, _
   ByVal Type As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim FileName As System.String
Dim Units As System.String
Dim Type As System.String
Dim value As System.Boolean

value = instance.InsertBendTableNew(FileName, Units, Type)
```

### C#

```csharp
System.bool InsertBendTableNew(
   System.string FileName,
   System.string Units,
   System.string Type
)
```

### C++/CLI

```cpp
System.bool InsertBendTableNew(
   System.String^ FileName,
   System.String^ Units,
   System.String^ Type
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`:
- `Units`:
- `Type`:

## VBA Syntax

See [ModelDoc::InsertBendTableNew](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertBendTableNew.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
