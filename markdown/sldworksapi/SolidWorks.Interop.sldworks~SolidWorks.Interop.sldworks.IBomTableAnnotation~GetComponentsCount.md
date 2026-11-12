---
title: "GetComponentsCount Method (IBomTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IBomTableAnnotation"
member: "GetComponentsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponentsCount.html"
---

# GetComponentsCount Method (IBomTableAnnotation)

Obsolete. Superseded by [IBomTableAnnotation::GetComponentsCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation~GetComponentsCount2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentsCount( _
   ByVal RowIndex As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableAnnotation
Dim RowIndex As System.Integer
Dim value As System.Integer

value = instance.GetComponentsCount(RowIndex)
```

### C#

```csharp
System.int GetComponentsCount(
   System.int RowIndex
)
```

### C++/CLI

```cpp
System.int GetComponentsCount(
   System.int RowIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RowIndex`: Row in the BOM table where to get the number of components; 0-based index

### Return Value

Number of components in the specified row

## VBA Syntax

See [BomTableAnnotation::GetComponentsCount](ms-its:sldworksapivb6.chm::/sldworks~BomTableAnnotation~GetComponentsCount.html).

## Remarks

Call this method before calling [IBomTableAnnotation::IGetComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation~IGetComponents.html) to determine the size of the array for that method.

## See Also

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html)
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html)
[IBomTableAnnotation::GetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponents.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
