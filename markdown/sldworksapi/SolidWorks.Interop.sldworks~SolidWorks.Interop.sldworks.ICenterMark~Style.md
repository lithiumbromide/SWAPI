---
title: "Style Property (ICenterMark)"
project: "SOLIDWORKS API Help"
interface: "ICenterMark"
member: "Style"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~Style.html"
---

# Style Property (ICenterMark)

Gets the style of this center mark.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Style As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterMark
Dim value As System.Integer

value = instance.Style
```

### C#

```csharp
System.int Style {get;}
```

### C++/CLI

```cpp
property System.int Style {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Center mark style as defined in [swCenterMarkStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCenterMarkStyle_e.html)

## VBA Syntax

See [CenterMark::Style](ms-its:sldworksapivb6.chm::/sldworks~CenterMark~Style.html).

## Examples

[List Center Marks in Drawing (VBA)](List_Center_Marks_in_Drawing_Example_VB.htm)
[Get and Set Center Mark Set (C#)](Get_and_Set_Center_Marks_Set_Example_CSharp.htm)
[Get and Set Center Mark Set (VB.NET)](Get_and_Set_Center_Marks_Set_Example_VBNET.htm)
[Get and Set Center Mark Set (VBA)](Get_and_Set_Center_Marks_Set_Example_VBA.htm)

## See Also

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
