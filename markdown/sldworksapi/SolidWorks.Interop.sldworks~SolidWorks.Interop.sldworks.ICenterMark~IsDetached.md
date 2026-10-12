---
title: "IsDetached Method (ICenterMark)"
project: "SOLIDWORKS API Help"
interface: "ICenterMark"
member: "IsDetached"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsDetached.html"
---

# IsDetached Method (ICenterMark)

Gets whether the specified center mark is detached.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsDetached( _
   ByVal Index As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterMark
Dim Index As System.Integer
Dim value As System.Boolean

value = instance.IsDetached(Index)
```

### C#

```csharp
System.bool IsDetached(
   System.int Index
)
```

### C++/CLI

```cpp
System.bool IsDetached(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of center mark (see **Remarks**)

### Return Value

True if the center mark specified by Index is detached, false if not

## VBA Syntax

See [CenterMark::IsDetached](ms-its:sldworksapivb6.chm::/sldworks~CenterMark~IsDetached.html).

## Examples

[Get and Set Center Mark Set (C#)](Get_and_Set_Center_Marks_Set_Example_CSharp.htm)
[Get and Set Center Mark Set (VB.NET)](Get_and_Set_Center_Marks_Set_Example_VBNET.htm)
[Get and Set Center Mark Set (VBA)](Get_and_Set_Center_Marks_Set_Example_VBA.htm)

## Remarks

This method is available to center marks in a center mark set and center marks in an array of center marks.

Use:

- [ICenterMark::IsGrouped](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsGrouped.html) to determine if the center mark is in a center mark set (i.e., a linear or circular pattern).
- [ICenterMark::GroupCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GroupCount.html) to get a valid value for Index for a center mark in a center mark set.

Use [ICenterMark::ReattachToCenterMarkGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~ReattachToCenterMarkGroup.html) to reattach a detached center mark in a center mark set. You cannot reattach a detached center mark that is not in a center mark set.

## See Also

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.html)
[ICenterMark::IsGrouped Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsGrouped.html)
[ICenterMark::GroupCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GroupCount.html)
[ICenterMark::HasDetachCenterMark Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~HasDetachCenterMark.html)
[ICenterMark::ReattachToCenterMarkGroup Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~ReattachToCenterMarkGroup.html)
[ICenterMark::AddToCenterMarkGroup Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~AddToCenterMarkGroup.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
