---
title: "GetType Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetType.html"
---

# GetType Method (IModelDoc2)

Gets the type of the document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Integer

value = instance.GetType()
```

### C#

```csharp
System.int GetType()
```

### C++/CLI

```cpp
System.int GetType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Type of this document as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

## VBA Syntax

See [ModelDoc2::GetType](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetType.html).

## Examples

[Display of Item in FeatureManager Design Tree (C++)](Display_of_Item_in_Feature_Manager_Example_CPlusPlus_COM.htm)
[Get Edge Data By Name (C++)](Get_Edge_Data_By_Name_Example_CPlusPlus_COM.htm)
[Get Named Entities (C++)](Get_Named_Entities_Example_CPlusPlus_COM.htm)
[Get Display Dimensions, GTols, and Surface-finish Symbols (VBA)](Get_Display_Dimensions,_Gtols,_and_Surface-Finish_Symbols_Example_VB.htm)
[Get Material Properties (VBA)](Get_Material_Properties_Example_VB.htm)
[Get Names of Bodies in Multibody Part (VBA)](Get_Names_of_Bodies_in_MultiBody_Part_Example_VB.htm)
[Select Bodies (VBA)](Select_Bodies_Example_VB.htm)
[Suppress or Unsuppress Feature (VBA)](Feature_Suppression_Example_VB.htm)
[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)
[Get and Set Table Anchor of Hole Table (C#)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_CSharp.htm)
[Get and Set Table Anchor of Hole Table (VB.NET)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_VBNET.htm)
[Get and Set Table Anchor of Hole Table (VBA)](Get_and_Set_Table_Anchor_of_Hole_Table_Example_VB.htm)
[Get Names of Configurations Using Variant (C++)](ConfigurationTraversalCPP.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
