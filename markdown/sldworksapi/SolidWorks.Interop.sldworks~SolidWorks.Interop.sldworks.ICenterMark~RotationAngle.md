---
title: "RotationAngle Property (ICenterMark)"
project: "SOLIDWORKS API Help"
interface: "ICenterMark"
member: "RotationAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~RotationAngle.html"
---

# RotationAngle Property (ICenterMark)

Gets or sets the angle for this center mark.

## Syntax

### Visual Basic (Declaration)

```vb
Property RotationAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterMark
Dim value As System.Double

instance.RotationAngle = value

value = instance.RotationAngle
```

### C#

```csharp
System.double RotationAngle {get; set;}
```

### C++/CLI

```cpp
property System.double RotationAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Angle

## VBA Syntax

See [CenterMark::RotationAngle](ms-its:sldworksapivb6.chm::/sldworks~CenterMark~RotationAngle.html).

## Examples

[List Center Marks in Drawing (VBA)](List_Center_Marks_in_Drawing_Example_VB.htm)

## See Also

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
