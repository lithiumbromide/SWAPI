---
title: "GetTableAnnotationCount Method (IGeneralTableFeature)"
project: "SOLIDWORKS API Help"
interface: "IGeneralTableFeature"
member: "GetTableAnnotationCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature~GetTableAnnotationCount.html"
---

# GetTableAnnotationCount Method (IGeneralTableFeature)

Gets the number of table annotations for this general table feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTableAnnotationCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IGeneralTableFeature
Dim value As System.Integer

value = instance.GetTableAnnotationCount()
```

### C#

```csharp
System.int GetTableAnnotationCount()
```

### C++/CLI

```cpp
System.int GetTableAnnotationCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of table annotations

## VBA Syntax

See [GeneralTableFeature::GetTableAnnotationCount](ms-its:sldworksapivb6.chm::/sldworks~GeneralTableFeature~GetTableAnnotationCount.html).

## Examples

[Hide and Show Row (VBA)](Hide_and_Show_Row_Example_VB.htm)
[Get General Table Feature (C#)](Get_General_Table_Feature_Example_CSharp.htm)
[Get General Table Feature (VB.NET)](Get_General_Table_Feature_Example_VBNET.htm)
[Get General Table Feature (VBA)](Get_General_Table_Feature_Example_VB.htm)

## Remarks

Call this method before calling [IGeneralTableFeature::IGetTableAnnotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGeneralTableFeature~IGetTableAnnotations.html) to get the size of the array.

## See Also

[IGeneralTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature.html)
[IGeneralTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature_members.html)
[IGeneralTableFeature::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature~GetTableAnnotations.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
