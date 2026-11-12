---
title: "IGetConfigurationNames Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IGetConfigurationNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IGetConfigurationNames.html"
---

# IGetConfigurationNames Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IGetConfigurationNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetConfigurationNames.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetConfigurationNames( _
   ByRef Count As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Count As System.Integer
Dim value As System.String

value = instance.IGetConfigurationNames(Count)
```

### C#

```csharp
System.string IGetConfigurationNames(
   out System.int Count
)
```

### C++/CLI

```cpp
System.String^ IGetConfigurationNames(
   [Out] System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`:

## VBA Syntax

See [ModelDoc::IGetConfigurationNames](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IGetConfigurationNames.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
