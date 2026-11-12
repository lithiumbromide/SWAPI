---
title: "SetAutomaticCutList Method (IBodyFolder)"
project: "SOLIDWORKS API Help"
interface: "IBodyFolder"
member: "SetAutomaticCutList"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~SetAutomaticCutList.html"
---

# SetAutomaticCutList Method (IBodyFolder)

Sets whether to automatically generate a cut list when the first weldment feature is inserted in a part.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetAutomaticCutList( _
   ByVal CutList As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBodyFolder
Dim CutList As System.Boolean
Dim value As System.Boolean

value = instance.SetAutomaticCutList(CutList)
```

### C#

```csharp
System.bool SetAutomaticCutList(
   System.bool CutList
)
```

### C++/CLI

```cpp
System.bool SetAutomaticCutList(
   System.bool CutList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CutList`: True to automatically generate a cut list, false to not

### Return Value

True if enabled, false if not (see **Remarks**)

## VBA Syntax

See [BodyFolder::SetAutomaticCutList](ms-its:sldworksapivb6.chm::/sldworks~BodyFolder~SetAutomaticCutList.html).

## Examples

See the [IBodyFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.html) examples.

## Remarks

Use [IBodyFolder::GetAutomaticCutList](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBodyFolder~GetAutomaticCutList.html) to find out if automatic generation of a cut list is enabled.

This method returns false if:

- the part does not contain a weldment feature. Use [IPartDoc::IsWeldment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~IsWeldment.html) to find out
  if the part contains this feature.
- a cut list folder already exists in the part. You must delete the cut list before
  you can enable automatic generation.

## See Also

[IBodyFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.html)
[IBodyFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder_members.html)
[IBodyFolder::UpdateCutList Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~UpdateCutList.html)
[IBodyFolder::GetCutListType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetCutListType.html)

## Availability

SOLIDWORKS 2006 SP2, Revision Number 14
