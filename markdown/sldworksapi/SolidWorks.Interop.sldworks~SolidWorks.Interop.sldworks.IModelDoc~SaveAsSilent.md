---
title: "SaveAsSilent Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SaveAsSilent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SaveAsSilent.html"
---

# SaveAsSilent Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SaveAsSilent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SaveAsSilent.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveAsSilent( _
   ByVal NewName As System.String, _
   ByVal SaveAsCopy As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim NewName As System.String
Dim SaveAsCopy As System.Boolean
Dim value As System.Integer

value = instance.SaveAsSilent(NewName, SaveAsCopy)
```

### C#

```csharp
System.int SaveAsSilent(
   System.string NewName,
   System.bool SaveAsCopy
)
```

### C++/CLI

```cpp
System.int SaveAsSilent(
   System.String^ NewName,
   System.bool SaveAsCopy
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NewName`:
- `SaveAsCopy`:

## VBA Syntax

See [ModelDoc::SaveAsSilent](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SaveAsSilent.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
