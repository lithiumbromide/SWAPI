---
title: "ShowExploded Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "ShowExploded"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ShowExploded.html"
---

# ShowExploded Method (IPartDoc)

Displays the specified explode view for this multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowExploded( _
   ByVal ShowIt As System.Boolean, _
   ByVal ExplodeViewName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim ShowIt As System.Boolean
Dim ExplodeViewName As System.String
Dim value As System.Boolean

value = instance.ShowExploded(ShowIt, ExplodeViewName)
```

### C#

```csharp
System.bool ShowExploded(
   System.bool ShowIt,
   System.string ExplodeViewName
)
```

### C++/CLI

```cpp
System.bool ShowExploded(
   System.bool ShowIt,
   System.String^ ExplodeViewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ShowIt`: True to show ExplodeViewName in its exploded state, false to show it in its collapsed state
- `ExplodeViewName`: Name of the explode view to show

### Return Value

True if the explode view displays correctly, false if not

## VBA Syntax

See [PartDoc::ShowExploded](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~ShowExploded.html).

## Examples

See the [IPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.html) example.

## Remarks

This method only works with explode views in the current, active configuration.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::GetExplodedViewConfigurationName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetExplodedViewConfigurationName.html)
[IPartDoc::GetExplodedViewNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetExplodedViewNames.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
