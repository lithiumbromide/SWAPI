---
title: "Mark Property (ISelectData)"
project: "SOLIDWORKS API Help"
interface: "ISelectData"
member: "Mark"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~Mark.html"
---

# Mark Property (ISelectData)

Gets or sets the value to use to mark the selected object.

## Syntax

### Visual Basic (Declaration)

```vb
Property Mark As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectData
Dim value As System.Integer

instance.Mark = value

value = instance.Mark
```

### C#

```csharp
System.int Mark {get; set;}
```

### C++/CLI

```cpp
property System.int Mark {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value for the mark

## VBA Syntax

See [SelectData::Mark](ms-its:sldworksapivb6.chm::/sldworks~SelectData~Mark.html).

## Examples

[Edit Mate (VBA)](Edit_Mate_Example_VB.htm)
[Insert Coordinate System at Center of Mass (VBA)](Insert_Coordinate_System_at_Center_of_Mass_Example_VB.htm)
[Move Bodies (C#)](Move_Bodies_Example_CSharp.htm)
[Move Bodies (VB.NET)](Move_Bodies_Example_VBNET.htm)
[Move Bodies (VBA)](Move_Bodies_Example_VB.htm)
[Get and Fill Gaps in Body (C#)](Get_and_Fill_Gaps_in_Body_Example_CSharp.htm)
[Get and Fill Gaps in Body (VB.NET)](Get_and_Fill_Gaps_in_Body_Example_VBNET.htm)
[Get and Fill Gaps in Body (VBA)](Get_and_Fill_Gaps_in_Body_Example_VB.htm)

## See Also

[ISelectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.html)
[ISelectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
