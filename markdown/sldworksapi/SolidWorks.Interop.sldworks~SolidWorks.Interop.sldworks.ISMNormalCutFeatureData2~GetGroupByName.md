---
title: "GetGroupByName Method (ISMNormalCutFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISMNormalCutFeatureData2"
member: "GetGroupByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~GetGroupByName.html"
---

# GetGroupByName Method (ISMNormalCutFeatureData2)

Gets the specified face group.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGroupByName( _
   ByVal GroupName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISMNormalCutFeatureData2
Dim GroupName As System.String
Dim value As System.Object

value = instance.GetGroupByName(GroupName)
```

### C#

```csharp
System.object GetGroupByName(
   System.string GroupName
)
```

### C++/CLI

```cpp
System.Object^ GetGroupByName(
   System.String^ GroupName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `GroupName`: Name of face group to retrieve

### Return Value

[ISMNormalCutGroupData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutGroupData.html)

## VBA Syntax

See [SMNormalCutFeatureData2::GetGroupByName](ms-its:sldworksapivb6.chm::/sldworks~SMNormalCutFeatureData2~GetGroupByName.html).

## Examples

See the [ISMNormalCutFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.html) example.

## Remarks

Use [ISMNormalCutFeatureData2::GetGroupNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~GetGroupNames.html) to populate GroupName.

## See Also

[ISMNormalCutFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.html)
[ISMNormalCutFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
