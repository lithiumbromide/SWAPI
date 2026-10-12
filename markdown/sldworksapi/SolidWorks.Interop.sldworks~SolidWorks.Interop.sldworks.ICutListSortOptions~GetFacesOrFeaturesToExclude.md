---
title: "GetFacesOrFeaturesToExclude Method (ICutListSortOptions)"
project: "SOLIDWORKS API Help"
interface: "ICutListSortOptions"
member: "GetFacesOrFeaturesToExclude"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions~GetFacesOrFeaturesToExclude.html"
---

# GetFacesOrFeaturesToExclude Method (ICutListSortOptions)

Gets the faces or features to exclude from cut list sorting.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFacesOrFeaturesToExclude() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICutListSortOptions
Dim value As System.Object

value = instance.GetFacesOrFeaturesToExclude()
```

### C#

```csharp
System.object GetFacesOrFeaturesToExclude()
```

### C++/CLI

```cpp
System.Object^ GetFacesOrFeaturesToExclude();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html) or [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html) to exclude

## VBA Syntax

See [CutListSortOptions::GetFacesOrFeaturesToExclude](ms-its:sldworksapivb6.chm::/sldworks~CutListSortOptions~GetFacesOrFeaturesToExclude.html).

## See Also

[ICutListSortOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions.html)
[ICutListSortOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions_members.html)
[ICutListSortOptions::SetFacesOrFeaturesToExclude Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions~SetFacesOrFeaturesToExclude.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
