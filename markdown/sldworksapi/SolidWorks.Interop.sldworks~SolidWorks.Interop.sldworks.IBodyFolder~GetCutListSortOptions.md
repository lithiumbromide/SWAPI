---
title: "GetCutListSortOptions Method (IBodyFolder)"
project: "SOLIDWORKS API Help"
interface: "IBodyFolder"
member: "GetCutListSortOptions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetCutListSortOptions.html"
---

# GetCutListSortOptions Method (IBodyFolder)

Gets the cut list sort options.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCutListSortOptions() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBodyFolder
Dim value As System.Object

value = instance.GetCutListSortOptions()
```

### C#

```csharp
System.object GetCutListSortOptions()
```

### C++/CLI

```cpp
System.Object^ GetCutListSortOptions();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[ICutListSortOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions.html); Null if [IBodyFolder::GetAutomaticCutList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetAutomaticCutList.html) returns false

## VBA Syntax

See ms-its:sldworksapivb6.chm::/sldworks~BodyFolder~GetBodyCount.html[BodyFolder::GetCutListSortOptions](ms-its:sldworksapivb6.chm::/sldworks~BodyFolder~GetCutListSortOptions.html).

## Examples

See the [IBodyFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.html) examples.

## See Also

[IBodyFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.html)
[IBodyFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder_members.html)
[IBodyFolder::SortCutList Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~SortCutList.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
