---
title: "Title Property (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "Title"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Title.html"
---

# Title Property (ITableAnnotation)

Gets or sets the title for this table.

## Syntax

### Visual Basic (Declaration)

```vb
Property Title As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim value As System.String

instance.Title = value

value = instance.Title
```

### C#

```csharp
System.string Title {get; set;}
```

### C++/CLI

```cpp
property System.String^ Title {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Text for title of table

## VBA Syntax

See [TableAnnotation::Title](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~Title.html).

## Examples

[Get Components for Each BOM Table Row (VBA)](Get_Components_in_Each_BOM_Table_Row_VB.htm)
[Export BOMs to XML (C#)](Export_BOMs_to_XML_Example_CSharp.htm)
[Export BOMs to XML (VB.NET)](Export_BOMs_to_XML_Example_VBNET.htm)
[Export BOMs to XML (VBA)](Export_BOMs_to_XML_Example_VB.htm)

## Remarks

You can set the title of the table even if the title is not currently visible. See [ITableAnnotation::TitleVisible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation~TitleVisible.html) for details.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
