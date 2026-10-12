---
title: "SecondRotationX Property (ISectionViewData)"
project: "SOLIDWORKS API Help"
interface: "ISectionViewData"
member: "SecondRotationX"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SecondRotationX.html"
---

# SecondRotationX Property (ISectionViewData)

Gets or sets the second x rotation of the section view in the part or assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Property SecondRotationX As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISectionViewData
Dim value As System.Double

instance.SecondRotationX = value

value = instance.SecondRotationX
```

### C#

```csharp
System.double SecondRotationX {get; set;}
```

### C++/CLI

```cpp
property System.double SecondRotationX {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Second x rotation of the section view

## VBA Syntax

See [SectionViewData::SecondRotationX](ms-its:sldworksapivb6.chm::/sldworks~SectionViewData~SecondRotationX.html).

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
[ISectionViewData::SecondRotationY Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SecondRotationY.html)
[ISectionViewData::ThirdRotationX Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ThirdRotationX.html)
[ISectionViewData::ThirdRotationY Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ThirdRotationY.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
