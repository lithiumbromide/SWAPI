---
title: "IGetComponents Method (IBomTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IBomTableAnnotation"
member: "IGetComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetComponents.html"
---

# IGetComponents Method (IBomTableAnnotation)

Obsolete. Superseded by [IBomTableAnnotation::IGetComponents2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation~IGetComponents2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetComponents( _
   ByVal RowIndex As System.Integer, _
   ByVal Count As System.Integer _
) As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableAnnotation
Dim RowIndex As System.Integer
Dim Count As System.Integer
Dim value As Component2

value = instance.IGetComponents(RowIndex, Count)
```

### C#

```csharp
Component2 IGetComponents(
   System.int RowIndex,
   System.int Count
)
```

### C++/CLI

```cpp
Component2^ IGetComponents(
   System.int RowIndex,
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RowIndex`: Row in the BOM table where to get the components; 0-based index
- `Count`: Number of components in the specified row

### Return Value

- in-process, unmanaged C++: Pointer to an array of [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) in the specified row

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IBomTableAnnotation::GetComponentsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation~GetComponentsCount.html) to get the value of Count.

## See Also

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html)
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html)
[IBomTableAnnotation::GetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponents.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
