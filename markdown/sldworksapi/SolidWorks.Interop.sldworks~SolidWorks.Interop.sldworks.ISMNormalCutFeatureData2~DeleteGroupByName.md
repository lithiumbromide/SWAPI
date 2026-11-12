---
title: "DeleteGroupByName Method (ISMNormalCutFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISMNormalCutFeatureData2"
member: "DeleteGroupByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~DeleteGroupByName.html"
---

# DeleteGroupByName Method (ISMNormalCutFeatureData2)

Deletes the specified face group.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteGroupByName( _
   ByVal GroupName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISMNormalCutFeatureData2
Dim GroupName As System.String
Dim value As System.Boolean

value = instance.DeleteGroupByName(GroupName)
```

### C#

```csharp
System.bool DeleteGroupByName(
   System.string GroupName
)
```

### C++/CLI

```cpp
System.bool DeleteGroupByName(
   System.String^ GroupName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `GroupName`: Name of face group to delete

### Return Value

True if deletion successful, false if not

## VBA Syntax

See [SMNormalCutFeatureData2::DeleteGroupByName](ms-its:sldworksapivb6.chm::/sldworks~SMNormalCutFeatureData2~DeleteGroupByName.html).

## Remarks

Use [ISMNormalCutFeatureData2::GetGroupNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~GetGroupNames.html) to populate GroupName.

You cannot delete a group, if it is the only group that exists.

## See Also

[ISMNormalCutFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.html)
[ISMNormalCutFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
