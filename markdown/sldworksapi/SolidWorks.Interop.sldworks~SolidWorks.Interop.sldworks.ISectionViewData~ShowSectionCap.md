---
title: "ShowSectionCap Property (ISectionViewData)"
project: "SOLIDWORKS API Help"
interface: "ISectionViewData"
member: "ShowSectionCap"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ShowSectionCap.html"
---

# ShowSectionCap Property (ISectionViewData)

Gets or sets whether to cap the section views.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShowSectionCap As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISectionViewData
Dim value As System.Boolean

instance.ShowSectionCap = value

value = instance.ShowSectionCap
```

### C#

```csharp
System.bool ShowSectionCap {get; set;}
```

### C++/CLI

```cpp
property System.bool ShowSectionCap {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to cap the section views, false to see inside the model (see **Remarks**)

## VBA Syntax

See [SectionViewData::ShowSectionCap](ms-its:sldworksapivb6.chm::/sldworks~SectionViewData~ShowSectionCap.html).

## Examples

[Create Section View in Model (C#)](Create_Section_View_in_Model_Example_CSharp.htm)
[Create Section View in Model (VB.NET)](Create_Section_View_in_Model_Example_VBNET.htm)
[Create Section View in Model (VBA)](Create_Section_View_in_Model_Example_VB.htm)
[Get Section View Data (C#)](Get_Section_View_Data_Example_CSharp.htm)
[Get Section View Data (VB.NET)](Get_Section_View_Data_Example_VBNET.htm)
[Get Section View Data (VBA)](Get_Section_View_Data_Example_VB.htm)

## Remarks

After setting this property to true, specify whether to color the caps by setting [ISectionViewData::KeepCapColor](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISectionViewData~KeepCapColor.html).

## See Also

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.html)
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
