---
title: "UpdateCutList Method (IBodyFolder)"
project: "SOLIDWORKS API Help"
interface: "IBodyFolder"
member: "UpdateCutList"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~UpdateCutList.html"
---

# UpdateCutList Method (IBodyFolder)

Updates an automatically generated cut list.

## Syntax

### Visual Basic (Declaration)

```vb
Function UpdateCutList() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBodyFolder
Dim value As System.Boolean

value = instance.UpdateCutList()
```

### C#

```csharp
System.bool UpdateCutList()
```

### C++/CLI

```cpp
System.bool UpdateCutList();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the automatically generated cut list is successfully updated, false if not or because the document does not contain an automatically generated cut list

## VBA Syntax

See [BodyFolder::UpdateCutList](ms-its:sldworksapivb6.chm::/sldworks~BodyFolder~UpdateCutList.html).

## Remarks

You must specify when to update an automatically generated cut list in a part document. However, an automatically generated cut list in a drawing is automatically updated when you open a drawing that references the cut list.

To find out if the part contains a weldment feature, use [IPartDoc::IsWeldment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~IsWeldment.html). If it does, then use [IBodyFolder::GetAutomaticCutList](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBodyFolder~GetAutomaticCutList.html) to find out if automatic generation of a cut list is enabled.

## See Also

[IBodyFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.html)
[IBodyFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder_members.html)
[IBodyFolder::SetAutomaticCutList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~SetAutomaticCutList.html)
[IBodyFolder::GetCutListType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetCutListType.html)

## Availability

SOLIDWORKS 2006 SP2, Revision Number 14
