---
title: "InsertPattern Method (IDimXpertPart)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPart"
member: "InsertPattern"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertPattern.html"
---

# InsertPattern Method (IDimXpertPart)

Inserts a linked, manual, or collection pattern using the selected faces.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertPattern( _
   ByVal Option As DimXpertDimensionOption, _
   ByVal PatternType As System.Integer, _
   ByVal FindAll As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertPart
Dim Option As DimXpertDimensionOption
Dim PatternType As System.Integer
Dim FindAll As System.Boolean
Dim value As System.Boolean

value = instance.InsertPattern(Option, PatternType, FindAll)
```

### C#

```csharp
System.bool InsertPattern(
   DimXpertDimensionOption Option,
   System.int PatternType,
   System.bool FindAll
)
```

### C++/CLI

```cpp
System.bool InsertPattern(
   DimXpertDimensionOption^ Option,
   System.int PatternType,
   System.bool FindAll
)
```

### Parameters

- `Option`: [IDimXpertDimensionOption](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDimensionOption.html)
- `PatternType`: 0 = linked

  1 = manual

  2 = collection
- `FindAll`: True to select similar faces for PatternTypes 1 and 2, false to not. (see **Remarks**)

### Return Value

False

## VBA Syntax

See [DimXpertPart::InsertPattern](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertPart~InsertPattern.html).

## Examples

[Get and Set Pattern (C#)](Get_and_Set_Pattern_Example_CSharp.htm)
[Get and Set Pattern (VB.NET)](Get_and_Set_Pattern_Example_VBNET.htm)
[Get and Set Pattern (VBA)](Get_and_Set_Pattern_Example_VB.htm)

## Remarks

Before calling this method:

1. Call [IDimXpertPart::GetDimOption](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPart~GetDimOption.html) to get an instance of IDimXpertDimensionOption.
2. Set [IDimXpertDimensionOption::FeatureSelectorOptions](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDimensionOption~FeatureSelectorOptions.html) to swDimXpertFeatureSelectorOption_Default to enable the FindAll property. If IDimXpertDimensionOption::FeatureSelectorOptions is set to anything other than the default, the FindAll setting is not in force.)
3. Populate Option with the instance of IDimXpertDimensionOption.
4. Select the features according to PatternType:

  1. If PatternType is linked, then select one feature to automatically select all features of the pattern.
  2. If PatternType is manual or collection and FindAll is set to true, then select one feature to automatically select all similar features on the face.
5. Set the selection mark for each selected feature to a unique value that is greater than 50.

## See Also

[IDimXpertPart Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart.html)
[IDimXpertPart Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart_members.html)
[IDimXpertPart::AutoDimensionScheme Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~AutoDimensionScheme.html)
[IDimXpertPart::InsertBasicDimension Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertBasicDimension.html)
[IDimXpertPart::InsertDatum Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertDatum.html)
[IDimXpertPart::InsertLocationDimension Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertLocationDimension.html)
[IDimXpertPart::InsertSizeDimension Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertSizeDimension.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
