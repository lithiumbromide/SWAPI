---
title: "SecondOffset Property (ISectionViewData)"
project: "SOLIDWORKS API Help"
interface: "ISectionViewData"
member: "SecondOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SecondOffset.html"
---

# SecondOffset Property (ISectionViewData)

Gets or sets the second offset distance of the section view for this part or assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Property SecondOffset As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISectionViewData
Dim value As System.Double

instance.SecondOffset = value

value = instance.SecondOffset
```

### C#

```csharp
System.double SecondOffset {get; set;}
```

### C++/CLI

```cpp
property System.double SecondOffset {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Second offset distance

## VBA Syntax

See [SectionViewData::SecondOffset](ms-its:sldworksapivb6.chm::/sldworks~SectionViewData~SecondOffset.html).

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
[ISectionViewData::ThirdOffset Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ThirdOffset.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
