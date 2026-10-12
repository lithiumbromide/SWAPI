---
title: "FeatureByName Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "FeatureByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~FeatureByName.html"
---

# FeatureByName Method (IDrawingDoc)

Gets the specified feature in the drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureByName( _
   ByVal Name As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Name As System.String
Dim value As System.Object

value = instance.FeatureByName(Name)
```

### C#

```csharp
System.object FeatureByName(
   System.string Name
)
```

### C++/CLI

```cpp
System.Object^ FeatureByName(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of the feature

### Return Value

Feature

## VBA Syntax

See [DrawingDoc::FeatureByName](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~FeatureByName.html).

## Examples

[Create and Name Planes (VBA)](Create_and_Name_Plane_Example_VB.htm)
[Get and Set Table Anchor of Hole Table (C#)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_CSharp.htm)
[Get and Set Table Anchor of Hole Table (VB.NET)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_VBNET.htm)
[Get and Set Table Anchor of Hole Table (VBA)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_VB.htm)

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::IFeatureByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IFeatureByName.html)
