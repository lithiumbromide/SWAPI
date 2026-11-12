---
title: "GroupCount Property (ICenterMark)"
project: "SOLIDWORKS API Help"
interface: "ICenterMark"
member: "GroupCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GroupCount.html"
---

# GroupCount Property (ICenterMark)

Gets the number of center marks in a center mark set.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property GroupCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterMark
Dim value As System.Integer

value = instance.GroupCount
```

### C#

```csharp
System.int GroupCount {get;}
```

### C++/CLI

```cpp
property System.int GroupCount {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of center marks in a center mark set

## VBA Syntax

See [CenterMark::GroupCount](ms-its:sldworksapivb6.chm::/sldworks~CenterMark~GroupCount.html).

## Examples

[Get and Set Center Mark Set (C#)](Get_and_Set_Center_Marks_Set_Example_CSharp.htm)
[Get and Set Center Mark Set (VB.NET)](Get_and_Set_Center_Marks_Set_Example_VBNET.htm)
[Get and Set Center Mark Set (VBA)](Get_and_Set_Center_Marks_Set_Example_VBA.htm)

## Remarks

If the center mark is in a center mark set (i.e., a linear or circular pattern), then:

- you can only change the length of the arms of any of the center marks in that pattern; you cannot change any other properties of those center marks. Call [ICenterMark::IsGrouped](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterMark~IsGrouped.html) to determine if a center mark is in a center mark set.
- use this property to get a range of valid values for [ICenterMark::GetExtendedLength](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterMark~GetExtendedLength.html)'s and [ICenterMark::SetExtendedLength](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterMark~SetExtendedLength.html)'s GroupID parameter. You can use a value from 0 to the number of center marks in a center mark set for the GroupID parameter.

## See Also

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
