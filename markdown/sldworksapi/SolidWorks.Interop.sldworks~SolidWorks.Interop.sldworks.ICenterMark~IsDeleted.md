---
title: "IsDeleted Method (ICenterMark)"
project: "SOLIDWORKS API Help"
interface: "ICenterMark"
member: "IsDeleted"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsDeleted.html"
---

# IsDeleted Method (ICenterMark)

Gets whether the specified center mark is deleted in this center mark set.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsDeleted( _
   ByVal Index As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterMark
Dim Index As System.Integer
Dim value As System.Boolean

value = instance.IsDeleted(Index)
```

### C#

```csharp
System.bool IsDeleted(
   System.int Index
)
```

### C++/CLI

```cpp
System.bool IsDeleted(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the center mark in the center mark set (see **Remarks**)

### Return Value

True if the specified center mark in this center mark set is deleted, false if not

## VBA Syntax

See [CenterMark::IsDeleted](ms-its:sldworksapivb6.chm::/sldworks~CenterMark~IsDeleted.html).

## Examples

[Get and Set Center Mark Set (C#)](Get_and_Set_Center_Marks_Set_Example_CSharp.htm)
[Get and Set Center Mark Set (VB.NET)](Get_and_Set_Center_Marks_Set_Example_VBNET.htm)
[Get and Set Center Mark Set (VBA)](Get_and_Set_Center_Marks_Set_Example_VBA.htm)

## Remarks

You can use a value from 0 to the [number of center marks in a center mark set](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GroupCount.html) for the Index parameter.

## See Also

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
