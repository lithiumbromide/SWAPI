---
title: "GetExplodedViewCount Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "GetExplodedViewCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetExplodedViewCount.html"
---

# GetExplodedViewCount Method (IPartDoc)

Gets the number of explode views in the specified configuration of this multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExplodedViewCount( _
   ByVal ConfigurationName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim ConfigurationName As System.String
Dim value As System.Integer

value = instance.GetExplodedViewCount(ConfigurationName)
```

### C#

```csharp
System.int GetExplodedViewCount(
   System.string ConfigurationName
)
```

### C++/CLI

```cpp
System.int GetExplodedViewCount(
   System.String^ ConfigurationName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigurationName`: Name of the configuration

### Return Value

Number of explode views in the specified configuration

## VBA Syntax

See [PartDoc::GetExplodedViewCount](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~GetExplodedViewCount.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::ShowExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ShowExploded.html)
[IPartDoc::GetExplodedViewNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetExplodedViewNames.html)
[IPartDoc::GetExplodedViewConfigurationName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetExplodedViewConfigurationName.html)
[IPartDoc::CreateExplodedView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateExplodedView.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
