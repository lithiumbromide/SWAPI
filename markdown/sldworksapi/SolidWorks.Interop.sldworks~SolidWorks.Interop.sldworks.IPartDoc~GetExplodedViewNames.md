---
title: "GetExplodedViewNames Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "GetExplodedViewNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetExplodedViewNames.html"
---

# GetExplodedViewNames Method (IPartDoc)

Gets the names of all the explode views in the specified configuration of this multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExplodedViewNames( _
   ByVal ConfigurationName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim ConfigurationName As System.String
Dim value As System.Object

value = instance.GetExplodedViewNames(ConfigurationName)
```

### C#

```csharp
System.object GetExplodedViewNames(
   System.string ConfigurationName
)
```

### C++/CLI

```cpp
System.Object^ GetExplodedViewNames(
   System.String^ ConfigurationName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigurationName`: Name of the configuration

### Return Value

Array of strings of the names of the explode views for ConfigurationName

## VBA Syntax

See [PartDoc::GetExplodedViewNames](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~GetExplodedViewNames.html).

## Examples

See the [IPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.html) example.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::GetExplodedViewConfigurationName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetExplodedViewConfigurationName.html)
[IPartDoc::ShowExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ShowExploded.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
