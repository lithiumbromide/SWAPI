---
title: "SetExtendedLength Method (ICenterMark)"
project: "SOLIDWORKS API Help"
interface: "ICenterMark"
member: "SetExtendedLength"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~SetExtendedLength.html"
---

# SetExtendedLength Method (ICenterMark)

Sets the extended length of this center mark.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetExtendedLength( _
   ByVal GroupID As System.Integer, _
   ByVal HandleID As System.Integer, _
   ByVal ExtendedLength As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterMark
Dim GroupID As System.Integer
Dim HandleID As System.Integer
Dim ExtendedLength As System.Double
Dim value As System.Boolean

value = instance.SetExtendedLength(GroupID, HandleID, ExtendedLength)
```

### C#

```csharp
System.bool SetExtendedLength(
   System.int GroupID,
   System.int HandleID,
   System.double ExtendedLength
)
```

### C++/CLI

```cpp
System.bool SetExtendedLength(
   System.int GroupID,
   System.int HandleID,
   System.double ExtendedLength
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `GroupID`: Instance of center mark (see Remarks)
- `HandleID`: Center mark handle ID as defined by [swCenterMarkHandle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCenterMarkHandle_e.html)
- `ExtendedLength`: Extended length of HandleID

### Return Value

True if the extended length of the specified center mark is set, false if not

## VBA Syntax

See [CenterMark::SetExtendedLength](ms-its:sldworksapivb6.chm::/sldworks~CenterMark~SetExtendedLength.html).

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
[ICenterMark::GetExtendedLength Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GetExtendedLength.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
