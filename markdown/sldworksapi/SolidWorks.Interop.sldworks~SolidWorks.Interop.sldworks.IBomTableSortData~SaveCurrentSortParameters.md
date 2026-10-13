---
title: "SaveCurrentSortParameters Property (IBomTableSortData)"
project: "SOLIDWORKS API Help"
interface: "IBomTableSortData"
member: "SaveCurrentSortParameters"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData~SaveCurrentSortParameters.html"
---

# SaveCurrentSortParameters Property (IBomTableSortData)

Gets and sets whether to save the current sort settings in the BOM table in the drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Property SaveCurrentSortParameters As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableSortData
Dim value As System.Boolean

instance.SaveCurrentSortParameters = value

value = instance.SaveCurrentSortParameters
```

### C#

```csharp
System.bool SaveCurrentSortParameters {get; set;}
```

### C++/CLI

```cpp
property System.bool SaveCurrentSortParameters {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to save the current sort settings in the BOM table, false to not

## VBA Syntax

See [BomTableSortData::SaveCurrentSortParameters](ms-its:sldworksapivb6.chm::/sldworks~BomTableSortData~SaveCurrentSortParameters.html).

## Examples

See the [IBomTableSortData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.html) examples.

## Remarks

After setting this property to true, you must call [IBomTableAnnotation::Sort](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation~Sort.html) to actually save the sort settings in the BOM table in the drawing. Thereafter, instead of setting all of the sorting parameters every time you instantiate a new IBomTableAnnotation for this table, you can simply call [IBomTableAnnotation::ApplySavedSortScheme](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation~ApplySavedSortScheme.html) to re-sort the table using the sort settings saved in the BOM table.

## See Also

[IBomTableSortData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.html)
[IBomTableSortData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
