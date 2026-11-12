---
title: "IGetConfigurationByName Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IGetConfigurationByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IGetConfigurationByName.html"
---

# IGetConfigurationByName Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IGetConfigurationByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetConfigurationByName.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetConfigurationByName( _
   ByVal Name As System.String _
) As Configuration
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Name As System.String
Dim value As Configuration

value = instance.IGetConfigurationByName(Name)
```

### C#

```csharp
Configuration IGetConfigurationByName(
   System.string Name
)
```

### C++/CLI

```cpp
Configuration^ IGetConfigurationByName(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`:

## VBA Syntax

See [ModelDoc::IGetConfigurationByName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IGetConfigurationByName.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
