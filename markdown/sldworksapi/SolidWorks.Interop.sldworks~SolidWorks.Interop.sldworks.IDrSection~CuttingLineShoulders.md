---
title: "CuttingLineShoulders Property (IDrSection)"
project: "SOLIDWORKS API Help"
interface: "IDrSection"
member: "CuttingLineShoulders"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~CuttingLineShoulders.html"
---

# CuttingLineShoulders Property (IDrSection)

Gets or sets whether to hide cutting line shoulders in this section view.

## Syntax

### Visual Basic (Declaration)

```vb
Property CuttingLineShoulders As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrSection
Dim value As System.Boolean

instance.CuttingLineShoulders = value

value = instance.CuttingLineShoulders
```

### C#

```csharp
System.bool CuttingLineShoulders {get; set;}
```

### C++/CLI

```cpp
property System.bool CuttingLineShoulders {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to hide cutting line shoulders, false to not

## VBA Syntax

See [DrSection::CuttingLineShoulders](ms-its:sldworksapivb6.chm::/sldworks~DrSection~CuttingLineShoulders.html).

## Examples

[Get and Set Whether to Hide Cutting Line Shoulders (C#)](Get_and_Set_Whether_to_Hide_Cutting_Line_Shoulders_Example_CSharp.htm)
[Get and Set Whether to Hide Cutting Line Shoulders (VB.NET)](Get_and_Set_Whether_to_Hide_Cutting_Line_Shoulders_Example_VBNET.htm)
[Get and Set Whether to Hide Cutting Line Shoulders (VBA)](Get_and_Set_Whether_to_Hide_Cutting_Line_Shoulders_Example_VB.htm)

## See Also

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.html)
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
