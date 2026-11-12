---
title: "GetPosition Method (ICenterMark)"
project: "SOLIDWORKS API Help"
interface: "ICenterMark"
member: "GetPosition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GetPosition.html"
---

# GetPosition Method (ICenterMark)

Gets the x, y, and z coordinates for the specified center mark.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPosition( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterMark
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetPosition(Index)
```

### C#

```csharp
System.object GetPosition(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetPosition(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the center mark (see **Remarks**)

### Return Value

Array of three doubles of the x, y, and z coordinates of the center mark specified by Index

## VBA Syntax

See [CenterMark::GetPosition](ms-its:sldworksapivb6.chm::/sldworks~CenterMark~GetPosition.html).

## Examples

[Get and Set Center Mark Set (C#)](Get_and_Set_Center_Marks_Set_Example_CSharp.htm)
[Get and Set Center Mark Set (VB.NET)](Get_and_Set_Center_Marks_Set_Example_VBNET.htm)
[Get and Set Center Mark Set (VBA)](Get_and_Set_Center_Marks_Set_Example_VBA.htm)

## Remarks

This method is available to center marks in a center mark set and center marks in an array of center marks.

Use:

- [ICenterMark::IsGrouped](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsGrouped.html) to determine if the center mark is in a center mark set (i.e., a linear or circular pattern)
- [ICenterMark::GroupCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GroupCount.html) to get a valid value for Index for a center mark in a center mark set.

## See Also

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
