---
title: "FixedReference Property (ISheetMetalFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalFeatureData"
member: "FixedReference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~FixedReference.html"
---

# FixedReference Property (ISheetMetalFeatureData)

Gets or sets the fixed face or edge for this sheet metal feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FixedReference As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalFeatureData
Dim value As System.Object

instance.FixedReference = value

value = instance.FixedReference
```

### C#

```csharp
System.object FixedReference {get; set;}
```

### C++/CLI

```cpp
property System.Object^ FixedReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fixed reference entity (edge or face)

## VBA Syntax

See [SheetMetalFeatureData::FixedReference](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalFeatureData~FixedReference.html).

## Examples

[Get Fixed Face of Sheet Metal Part (VBA)](Get_Fixed_Face_of_Sheet_Metal_Part_Example_VB.htm)

## Remarks

To access the fixed reference of a sheet metal feature in sheet metal models created in SOLIDWORKS 2013 or later, follow the examples of [IModelDocExtension::GetTemplateSheetMetal](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetTemplateSheetMetal.html).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.html)

## Availability

SOLIDWORKS 2001 SP1, Revision Number 9.1
