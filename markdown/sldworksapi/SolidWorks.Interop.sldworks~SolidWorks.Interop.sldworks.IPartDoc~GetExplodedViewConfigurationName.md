---
title: "GetExplodedViewConfigurationName Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "GetExplodedViewConfigurationName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetExplodedViewConfigurationName.html"
---

# GetExplodedViewConfigurationName Method (IPartDoc)

Gets the name of the configuration for the specified explode view of this multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExplodedViewConfigurationName( _
   ByVal ExplodedViewName As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim ExplodedViewName As System.String
Dim value As System.String

value = instance.GetExplodedViewConfigurationName(ExplodedViewName)
```

### C#

```csharp
System.string GetExplodedViewConfigurationName(
   System.string ExplodedViewName
)
```

### C++/CLI

```cpp
System.String^ GetExplodedViewConfigurationName(
   System.String^ ExplodedViewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ExplodedViewName`: Name of the explode view whose configuration to get

### Return Value

Name of the configuration for ExplodedViewName

## VBA Syntax

See [PartDoc::GetExplodedViewConfigurationName](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~GetExplodedViewConfigurationName.html).

## Examples

See the [IPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.html) example.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::GetExplodedViewNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetExplodedViewNames.html)
[IPartDoc::ShowExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ShowExploded.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
