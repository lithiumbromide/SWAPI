---
title: "GetModelPathNamesCount Method (IBomTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IBomTableAnnotation"
member: "GetModelPathNamesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetModelPathNamesCount.html"
---

# GetModelPathNamesCount Method (IBomTableAnnotation)

Gets the number of model pathnames in the specified row of this BOM table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetModelPathNamesCount( _
   ByVal RowIndex As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableAnnotation
Dim RowIndex As System.Integer
Dim value As System.Integer

value = instance.GetModelPathNamesCount(RowIndex)
```

### C#

```csharp
System.int GetModelPathNamesCount(
   System.int RowIndex
)
```

### C++/CLI

```cpp
System.int GetModelPathNamesCount(
   System.int RowIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RowIndex`: Row in the BOM table; 0-based index

### Return Value

Number of model pathnames in the specified row

## VBA Syntax

See [BomTableAnnotation::GetModelPathNamesCount](ms-its:sldworksapivb6.chm::/sldworks~BomTableAnnotation~GetModelPathNamesCount.html).

## Examples

[Get Model Pathnames in BOM Table (C#)](Get_Model_Path_Names_in_BOM_Table_Example_CSharp.htm)
[Get Model Pathnames in BOM Table (VB.NET)](Get_Model_Path_Names_in_BOM_Table_Example_VBNET.htm)
[Get Model Pathnames in BOM Table (VBA)](Get_Model_Path_Names_in_BOM_Table_Example_VB.htm)

## Remarks

Call this method before calling [IBomTableAnnotation::IGetModelPathNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation~IGetModelPathNames.html) to determine the size of the array for that method.

## See Also

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html)
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html)
[IBomTableAnnotation::GetModelPathNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetModelPathNames.html)

## Availability

SOLIDWORKS 2011 SP01, Revision Number 19.1
