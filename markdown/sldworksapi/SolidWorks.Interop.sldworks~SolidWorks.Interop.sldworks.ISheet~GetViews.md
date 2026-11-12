---
title: "GetViews Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "GetViews"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetViews.html"
---

# GetViews Method (ISheet)

Gets the drawing views on this sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetViews() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim value As System.Object

value = instance.GetViews()
```

### C#

```csharp
System.object GetViews()
```

### C++/CLI

```cpp
System.Object^ GetViews();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of drawing [views](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) on this sheet

## VBA Syntax

See [Sheet::GetViews](ms-its:sldworksapivb6.chm::/Sldworks~Sheet~GetViews.html).

## Examples

[Get and Set Table Anchor of Hole Table (C#)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_CSharp.htm)
[Get and Set Table Anchor of Hole Table (VB.NET)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_VBNET.htm)
[Get and Set Table Anchor of Hole Table (VBA)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_VB.htm)

## Remarks

If this sheet is:

- Active, this method returns the drawing views, standard orientation views selected when the view was created, and any named views.
- Not active, this method returns only the drawing views.

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
