---
title: "IGetAllCustomProperties Method (IBomTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IBomTableAnnotation"
member: "IGetAllCustomProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetAllCustomProperties.html"
---

# IGetAllCustomProperties Method (IBomTableAnnotation)

Gets the list of available custom properties that can be used for a custom properties column in this BOM table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAllCustomProperties( _
   ByVal Count As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableAnnotation
Dim Count As System.Integer
Dim value As System.String

value = instance.IGetAllCustomProperties(Count)
```

### C#

```csharp
System.string IGetAllCustomProperties(
   System.int Count
)
```

### C++/CLI

```cpp
System.String^ IGetAllCustomProperties(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of available custom properties

### Return Value

- in-process, unmanaged C++: Pointer to an array of strings of available custom properties

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

To get the number of custom properties, use [IBomTableAnnotation::GetAllCustomPropertiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation~GetAllCustomPropertiesCount.html).

The list of available custom properties includes all of the items in the BOM table, which includes items from the file summary items and file custom properties that have been set.

## See Also

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html)
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html)
[IBomTableAnnotation::GetAllCustomProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetAllCustomProperties.html)
[IBomTableAnnotation::GetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetColumnCustomProperty.html)

## Availability

SOLIDWORKS 2004 SP1, Revision Number 12
