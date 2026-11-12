---
title: "ThirdOffset Property (ISectionViewData)"
project: "SOLIDWORKS API Help"
interface: "ISectionViewData"
member: "ThirdOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ThirdOffset.html"
---

# ThirdOffset Property (ISectionViewData)

Gets or sets the third offset distance of the section view for this part or assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThirdOffset As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISectionViewData
Dim value As System.Double

instance.ThirdOffset = value

value = instance.ThirdOffset
```

### C#

```csharp
System.double ThirdOffset {get; set;}
```

### C++/CLI

```cpp
property System.double ThirdOffset {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Third offset distance

## VBA Syntax

See [SectionViewData::ThirdOffset](ms-its:sldworksapivb6.chm::/sldworks~SectionViewData~ThirdOffset.html).

## Examples

[Create Section View in Model (C#)](Create_Section_View_in_Model_Example_CSharp.htm)
[Create Section View in Model (VB.NET)](Create_Section_View_in_Model_Example_VBNET.htm)
[Create Section View in Model (VBA)](Create_Section_View_in_Model_Example_VB.htm)
[Get Section View Data (C#)](Get_Section_View_Data_Example_CSharp.htm)
[Get Section View Data (VB.NET)](Get_Section_View_Data_Example_VBNET.htm)
[Get Section View Data (VBA)](Get_Section_View_Data_Example_VB.htm)

## See Also

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.html)
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.html)
[ISectionViewData::FirstOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~FirstOffset.html)
[ISectionViewData::SecondOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SecondOffset.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
