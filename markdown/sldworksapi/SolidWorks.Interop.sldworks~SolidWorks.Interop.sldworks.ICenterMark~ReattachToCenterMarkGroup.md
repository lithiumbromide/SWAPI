---
title: "ReattachToCenterMarkGroup Method (ICenterMark)"
project: "SOLIDWORKS API Help"
interface: "ICenterMark"
member: "ReattachToCenterMarkGroup"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~ReattachToCenterMarkGroup.html"
---

# ReattachToCenterMarkGroup Method (ICenterMark)

Reattaches the specified center mark to the selected entity in a center mark set.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReattachToCenterMarkGroup( _
   ByVal Index As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterMark
Dim Index As System.Integer
Dim value As System.Boolean

value = instance.ReattachToCenterMarkGroup(Index)
```

### C#

```csharp
System.bool ReattachToCenterMarkGroup(
   System.int Index
)
```

### C++/CLI

```cpp
System.bool ReattachToCenterMarkGroup(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of center mark (see **Remarks**)

### Return Value

True if the center mark specified by Index is reattached to the selected entity in a center mark set, false if not

## VBA Syntax

See [CenterMark::ReattachToCenterMarkGroup](ms-its:sldworksapivb6.chm::/sldworks~CenterMark~ReattachToCenterMarkGroup.html).

## Remarks

You must pre-select an entity in an existing center mark set (i.e., a linear or circular pattern) for which to reattach the center mark. If the existing center mark set is a linear pattern, then the selected entity must be in that linear pattern, else this method fails. The same rule applies when reattaching an entity to an existing center mark set that is a circular pattern.

Use:

- [ICenterMark::IsGrouped](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsGrouped.html) to determine if the center mark is in a center mark set (i.e., a linear or circular pattern).
- [ICenterMark::GroupCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GroupCount.html) to get a valid value for Index for a center mark in a center mark set.

## See Also

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.html)
[ICenterMark::HasDetachCenterMark Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~HasDetachCenterMark.html)
[ICenterMark::IsDetached Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsDetached.html)
[ICenterMark::IsGrouped Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsGrouped.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
