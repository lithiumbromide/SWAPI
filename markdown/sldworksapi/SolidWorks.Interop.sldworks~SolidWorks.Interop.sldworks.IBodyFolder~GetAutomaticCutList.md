---
title: "GetAutomaticCutList Method (IBodyFolder)"
project: "SOLIDWORKS API Help"
interface: "IBodyFolder"
member: "GetAutomaticCutList"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetAutomaticCutList.html"
---

# GetAutomaticCutList Method (IBodyFolder)

Gets whether to automatically generate a cut list when the first weldment feature is inserted in a part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAutomaticCutList() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBodyFolder
Dim value As System.Boolean

value = instance.GetAutomaticCutList()
```

### C#

```csharp
System.bool GetAutomaticCutList()
```

### C++/CLI

```cpp
System.bool GetAutomaticCutList();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True to automatically generate a cut list, false to not

## VBA Syntax

See [BodyFolder::GetAutomaticCutList](ms-its:sldworksapivb6.chm::/sldworks~BodyFolder~GetAutomaticCutList.html).

## Examples

See the [IBodyFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.html) examples.

## Remarks

By default, a cut list is automatically generated in new weldment parts. Use [IBodyFolder::SetAutomaticCutList](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBodyFolder~SetAutomaticCutList.html) to change the default. Use [IPartDoc::IsWeldment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~IsWeldment.html) to get whether the part contains a weldment feature.

## See Also

[IBodyFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.html)
[IBodyFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder_members.html)
[IBodyFolder::UpdateCutList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~UpdateCutList.html)
[IBodyFolder::GetCutListType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetCutListType.html)
[IBodyFolder::GetCutListSortOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetCutListSortOptions.html)

## Availability

SOLIDWORKS 2006 SP2, Revision Number 14
