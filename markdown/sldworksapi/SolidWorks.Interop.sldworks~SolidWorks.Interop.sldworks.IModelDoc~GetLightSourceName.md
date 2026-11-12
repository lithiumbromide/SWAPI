---
title: "GetLightSourceName Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GetLightSourceName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetLightSourceName.html"
---

# GetLightSourceName Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GetLightSourceName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetLightSourceName.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLightSourceName( _
   ByVal ID As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim ID As System.Integer
Dim value As System.String

value = instance.GetLightSourceName(ID)
```

### C#

```csharp
System.string GetLightSourceName(
   System.int ID
)
```

### C++/CLI

```cpp
System.String^ GetLightSourceName(
   System.int ID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`:

## VBA Syntax

See [ModelDoc::GetLightSourceName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GetLightSourceName.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
