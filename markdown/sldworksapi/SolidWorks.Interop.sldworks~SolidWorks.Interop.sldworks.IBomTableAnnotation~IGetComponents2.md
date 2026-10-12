---
title: "IGetComponents2 Method (IBomTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IBomTableAnnotation"
member: "IGetComponents2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetComponents2.html"
---

# IGetComponents2 Method (IBomTableAnnotation)

Gets the components in the specified row for the specified configuration in this BOM table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetComponents2( _
   ByVal RowIndex As System.Integer, _
   ByVal Configuration As System.String, _
   ByVal Count As System.Integer _
) As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableAnnotation
Dim RowIndex As System.Integer
Dim Configuration As System.String
Dim Count As System.Integer
Dim value As Component2

value = instance.IGetComponents2(RowIndex, Configuration, Count)
```

### C#

```csharp
Component2 IGetComponents2(
   System.int RowIndex,
   System.string Configuration,
   System.int Count
)
```

### C++/CLI

```cpp
Component2^ IGetComponents2(
   System.int RowIndex,
   System.String^ Configuration,
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RowIndex`: Row in the BOM table where to get the components; 0-based index
- `Configuration`: Configuration for which to count components in top-level only BOMs; specify an empty string for parts only and indented BOMs
- `Count`: Number of components in the specified row

### Return Value

- in-process, unmanaged C++: Pointer to an array of [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) in the specified row for the specified configuration

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IBomTableAnnotation::GetComponentsCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation~GetComponentsCount2.html) to get the value of Count.

## See Also

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html)
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html)
[IBomTableAnnotation::GetComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetComponents2.html)

## Availability

SOLIDWORKS 2011 SP03 , Revision Number 19.3
