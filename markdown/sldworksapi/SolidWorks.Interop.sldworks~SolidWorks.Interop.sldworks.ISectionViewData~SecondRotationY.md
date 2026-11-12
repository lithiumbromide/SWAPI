---
title: "SecondRotationY Property (ISectionViewData)"
project: "SOLIDWORKS API Help"
interface: "ISectionViewData"
member: "SecondRotationY"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SecondRotationY.html"
---

# SecondRotationY Property (ISectionViewData)

Gets or sets the second y rotation of the section view in the part or assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Property SecondRotationY As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISectionViewData
Dim value As System.Double

instance.SecondRotationY = value

value = instance.SecondRotationY
```

### C#

```csharp
System.double SecondRotationY {get; set;}
```

### C++/CLI

```cpp
property System.double SecondRotationY {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Second y rotation of the section view

## VBA Syntax

See [SectionViewData::SecondRotationY](ms-its:sldworksapivb6.chm::/sldworks~SectionViewData~SecondRotationY.html).

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
[ISectionViewData::FirstRotationX Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~FirstRotationX.html)
[ISectionViewData::FirstRotationY Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~FirstRotationY.html)
[ISectionViewData::SecondRotationX Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SecondRotationX.html)
[ISectionViewData::ThirdRotationX Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ThirdRotationX.html)
[ISectionViewData::ThirdRotationY Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ThirdRotationY.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
