---
title: "CenterLineFont Property (ICenterMark)"
project: "SOLIDWORKS API Help"
interface: "ICenterMark"
member: "CenterLineFont"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~CenterLineFont.html"
---

# CenterLineFont Property (ICenterMark)

Gets or sets whether the centerline font is used for the lines in this center mark.

## Syntax

### Visual Basic (Declaration)

```vb
Property CenterLineFont As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterMark
Dim value As System.Boolean

instance.CenterLineFont = value

value = instance.CenterLineFont
```

### C#

```csharp
System.bool CenterLineFont {get; set;}
```

### C++/CLI

```cpp
property System.bool CenterLineFont {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if centerline font is used for the lines in center marks, false if not

## VBA Syntax

See [CenterMark::CenterLineFont](ms-its:sldworksapivb6.chm::/sldworks~CenterMark~CenterLineFont.html).

## Examples

[List Center Marks in Drawing (VBA)](List_Center_Marks_in_Drawing_Example_VB.htm)

## See Also

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
