---
title: "GetTableAnnotations Method (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "GetTableAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetTableAnnotations.html"
---

# GetTableAnnotations Method (IBomFeature)

Gets the BOM table annotations for this BOM table feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTableAnnotations() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim value As System.Object

value = instance.GetTableAnnotations()
```

### C#

```csharp
System.object GetTableAnnotations()
```

### C++/CLI

```cpp
System.Object^ GetTableAnnotations();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IBOMTableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation.html) objects

## VBA Syntax

See [BomFeature::GetTableAnnotations](ms-its:sldworksapivb6.chm::/sldworks~BomFeature~GetTableAnnotations.html).

## Examples

[Export BOMs to XML (C#)](Export_BOMs_to_XML_Example_CSharp.htm)
[Export BOMs to XML (VB.NET)](Export_BOMs_to_XML_Example_VBNET.htm)
[Export BOMs to XML (VBA)](Export_BOMs_to_XML_Example_VB.htm)
[Get Components in Each BOM Table Row (C#)](Get_Components_in_Each_BOM_Table_Row_Example_CSharp.htm)
[Get Components in Each BOM Table Row (VB.NET)](Get_Components_in_Each_BOM_Table_Row_Example_VBNET.htm)
[Get Components in Each BOM Table Row (VBA)](Get_Components_in_Each_BOM_Table_Row_VB.htm)

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)
[IBomFeature::GetTableAnnotationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetTableAnnotationCount.html)
[IBomFeature::IGetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~IGetTableAnnotations.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12
