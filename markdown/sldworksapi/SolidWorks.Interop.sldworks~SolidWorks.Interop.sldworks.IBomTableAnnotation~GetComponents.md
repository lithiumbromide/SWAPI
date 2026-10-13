---
title: "GetComponents Method (IBomTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IBomTableAnnotation"
member: "GetComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponents.html"
---

# GetComponents Method (IBomTableAnnotation)

Obsolete. Superseded by [IBomTableAnnotation::GetComponents2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation~GetComponents2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponents( _
   ByVal RowIndex As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableAnnotation
Dim RowIndex As System.Integer
Dim value As System.Object

value = instance.GetComponents(RowIndex)
```

### C#

```csharp
System.object GetComponents(
   System.int RowIndex
)
```

### C++/CLI

```cpp
System.Object^ GetComponents(
   System.int RowIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RowIndex`: Row in the BOM table where to get the components; 0-based index

### Return Value

Array of [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) in the specified row

## VBA Syntax

See [BomTableAnnotation::GetComponents](ms-its:sldworksapivb6.chm::/sldworks~BomTableAnnotation~GetComponents.html).

## See Also

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html)
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html)
[IBomTableAnnotation::GetComponentsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponentsCount.html)
[IBomTableAnnotation::IGetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetComponents.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
