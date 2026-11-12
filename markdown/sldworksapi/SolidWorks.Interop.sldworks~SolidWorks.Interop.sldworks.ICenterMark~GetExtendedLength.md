---
title: "GetExtendedLength Method (ICenterMark)"
project: "SOLIDWORKS API Help"
interface: "ICenterMark"
member: "GetExtendedLength"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GetExtendedLength.html"
---

# GetExtendedLength Method (ICenterMark)

Gets the extended length of the specified arm (handle) of this center mark.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExtendedLength( _
   ByVal GroupID As System.Integer, _
   ByVal HandleID As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterMark
Dim GroupID As System.Integer
Dim HandleID As System.Integer
Dim value As System.Double

value = instance.GetExtendedLength(GroupID, HandleID)
```

### C#

```csharp
System.double GetExtendedLength(
   System.int GroupID,
   System.int HandleID
)
```

### C++/CLI

```cpp
System.double GetExtendedLength(
   System.int GroupID,
   System.int HandleID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `GroupID`: Center mark instance (see Remarks)
- `HandleID`: Center mark handle ID as defined in [swCenterMarkHandle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCenterMarkHandle_e.html)

### Return Value

Extended length of the HandleID

## VBA Syntax

See [CenterMark::GetExtendedLength](ms-its:sldworksapivb6.chm::/sldworks~CenterMark~GetExtendedLength.html).

## Examples

[Extend Arms of Center Mark (VBA)](Extend_Arms_of_Center_Mark_Examples_VB.htm)
[Get and Set Center Mark Set (C#)](Get_and_Set_Center_Marks_Set_Example_CSharp.htm)
[Get and Set Center Mark Set (VB.NET)](Get_and_Set_Center_Marks_Set_Example_VBNET.htm)
[Get and Set Center Mark Set (VBA)](Get_and_Set_Center_Marks_Set_Example_VBA.htm)

## Remarks

If the center mark is in a center mark set (i.e., a linear or circular pattern), then use [ICenterMark::GroupCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterMark~GroupCount.html) to get the range of valid values for the GroupID parameter. You can use a value from 0 to ICenterMark::GroupCount for the GroupID parameter. To determine if a center mark is in a center mark set, use [ICenterMark::IsGrouped](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterMark~IsGrouped.html).

## See Also

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.html)
[ICenterMark::SetExtendedLength Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~SetExtendedLength.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
