---
title: "GetTableAnnotations Method (IGeneralTableFeature)"
project: "SOLIDWORKS API Help"
interface: "IGeneralTableFeature"
member: "GetTableAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature~GetTableAnnotations.html"
---

# GetTableAnnotations Method (IGeneralTableFeature)

Gets the table annotations for this general table feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTableAnnotations() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IGeneralTableFeature
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

Array of [general table annotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGeneralTableAnnotation.html)

## VBA Syntax

See [GeneralTableFeature::GetTableAnnotations](ms-its:sldworksapivb6.chm::/sldworks~GeneralTableFeature~GetTableAnnotations.html).

## Examples

[Hide and Show Row (VBA)](Hide_and_Show_Row_Example_VB.htm)
[Get General Table Feature (C#)](Get_General_Table_Feature_Example_CSharp.htm)
[Get General Table Feature (VB.NET)](Get_General_Table_Feature_Example_VBNET.htm)
[Get General Table Feature (VBA)](Get_General_Table_Feature_Example_VB.htm)

## See Also

[IGeneralTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature.html)
[IGeneralTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature_members.html)
[IGeneralTableFeature::IGetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature~IGetTableAnnotations.html)
[IGeneralTableFeature::GetTableAnnotationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature~GetTableAnnotationCount.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
