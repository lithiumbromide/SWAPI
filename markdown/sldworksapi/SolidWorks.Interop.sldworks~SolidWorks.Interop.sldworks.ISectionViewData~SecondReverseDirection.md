---
title: "SecondReverseDirection Property (ISectionViewData)"
project: "SOLIDWORKS API Help"
interface: "ISectionViewData"
member: "SecondReverseDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SecondReverseDirection.html"
---

# SecondReverseDirection Property (ISectionViewData)

Gets or sets whether to reverse the second direction of the section view for this part or assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Property SecondReverseDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISectionViewData
Dim value As System.Boolean

instance.SecondReverseDirection = value

value = instance.SecondReverseDirection
```

### C#

```csharp
System.bool SecondReverseDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool SecondReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the second direction of the section view, false to not

## VBA Syntax

See [SectionViewData::SecondReverseDirection](ms-its:sldworksapivb6.chm::/sldworks~SectionViewData~SecondReverseDirection.html).

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
[ISectionViewData::FirstReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~FirstReverseDirection.html)
[ISectionViewData::ThirdReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ThirdReverseDirection.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
