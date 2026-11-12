---
title: "IsGrouped Property (ICenterMark)"
project: "SOLIDWORKS API Help"
interface: "ICenterMark"
member: "IsGrouped"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~IsGrouped.html"
---

# IsGrouped Property (ICenterMark)

Gets whether a center mark is in a center mark set.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsGrouped As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterMark
Dim value As System.Boolean

value = instance.IsGrouped
```

### C#

```csharp
System.bool IsGrouped {get;}
```

### C++/CLI

```cpp
property System.bool IsGrouped {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the center mark is in a center mark set, false if not

## VBA Syntax

See [CenterMark::IsGrouped](ms-its:sldworksapivb6.chm::/sldworks~CenterMark~IsGrouped.html).

## Examples

[Get and Set Center Mark Set (C#)](Get_and_Set_Center_Marks_Set_Example_CSharp.htm)
[Get and Set Center Mark Set (VB.NET)](Get_and_Set_Center_Marks_Set_Example_VBNET.htm)
[Get and Set Center Mark Set (VBA)](Get_and_Set_Center_Marks_Set_Example_VBA.htm)

## See Also

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.html)
[ICenterMark::GroupCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~GroupCount.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
