---
title: "HasDetachCenterMark Method (ICenterMark)"
project: "SOLIDWORKS API Help"
interface: "ICenterMark"
member: "HasDetachCenterMark"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~HasDetachCenterMark.html"
---

# HasDetachCenterMark Method (ICenterMark)

Gets whether the selected center mark set contains any detached center marks.

## Syntax

### Visual Basic (Declaration)

```vb
Function HasDetachCenterMark() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterMark
Dim value As System.Boolean

value = instance.HasDetachCenterMark()
```

### C#

```csharp
System.bool HasDetachCenterMark()
```

### C++/CLI

```cpp
System.bool HasDetachCenterMark();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the selected center mark set contains any detached center marks, false if not

## VBA Syntax

See [CenterMark::HasDetachCenterMark](ms-its:sldworksapivb6.chm::/sldworks~CenterMark~HasDetachCenterMark.html).

## Examples

[Get and Set Center Mark Set (C#)](Get_and_Set_Center_Marks_Set_Example_CSharp.htm)
[Get and Set Center Mark Set (VB.NET)](Get_and_Set_Center_Marks_Set_Example_VBNET.htm)
[Get and Set Center Mark Set (VBA)](Get_and_Set_Center_Marks_Set_Example_VBA.htm)

## Remarks

You must select the center mark set before calling this method. To determine if a center mark is in a center mark set (i.e., a linear or circular pattern), use [ICenterMark::IsGrouped](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsGrouped.html).

## See Also

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.html)
[ICenterMark::IsGrouped Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsGrouped.html)
[ICenterMark::GroupCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GroupCount.html)
[ICenterMark::IsDetached Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsDetached.html)
[ICenterMark::ReattachToCenterMarkGroup Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~ReattachToCenterMarkGroup.html)
[ICenterMark::AddToCenterMarkGroup Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~AddToCenterMarkGroup.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
