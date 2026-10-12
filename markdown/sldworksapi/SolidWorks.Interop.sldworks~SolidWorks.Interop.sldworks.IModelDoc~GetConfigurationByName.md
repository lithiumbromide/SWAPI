---
title: "GetConfigurationByName Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GetConfigurationByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetConfigurationByName.html"
---

# GetConfigurationByName Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GetConfigurationByName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetConfigurationByName.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConfigurationByName( _
   ByVal Name As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Name As System.String
Dim value As System.Object

value = instance.GetConfigurationByName(Name)
```

### C#

```csharp
System.object GetConfigurationByName(
   System.string Name
)
```

### C++/CLI

```cpp
System.Object^ GetConfigurationByName(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`:

## VBA Syntax

See [ModelDoc::GetConfigurationByName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GetConfigurationByName.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
