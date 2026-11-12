---
title: "IGet3rdPartyStorage Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IGet3rdPartyStorage"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IGet3rdPartyStorage.html"
---

# IGet3rdPartyStorage Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IGet3rdPartyStorage](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGet3rdPartyStorage.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGet3rdPartyStorage( _
   ByVal StringIn As System.String, _
   ByVal IsStoring As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim StringIn As System.String
Dim IsStoring As System.Boolean
Dim value As System.Object

value = instance.IGet3rdPartyStorage(StringIn, IsStoring)
```

### C#

```csharp
System.object IGet3rdPartyStorage(
   System.string StringIn,
   System.bool IsStoring
)
```

### C++/CLI

```cpp
System.Object^ IGet3rdPartyStorage(
   System.String^ StringIn,
   System.bool IsStoring
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StringIn`:
- `IsStoring`:

## VBA Syntax

See [ModelDoc::IGet3rdPartyStorage](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IGet3rdPartyStorage.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
