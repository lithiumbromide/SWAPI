---
title: "IGetAllCustomProperties Method (IRevisionTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IRevisionTableAnnotation"
member: "IGetAllCustomProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~IGetAllCustomProperties.html"
---

# IGetAllCustomProperties Method (IRevisionTableAnnotation)

Gets a list of available custom properties that can be used for a custom properties column in this revision table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAllCustomProperties( _
   ByVal Count As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionTableAnnotation
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

This method only works for SOLIDWORKS documents created or saved in SOLIDWORKS 2005 or later.

Before calling this method, call [IRevisionTableAnnotation::GetAllCustomPropertiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableAnnotation~GetAllCustomPropertiesCount.html) to get the number of available custom properties.

The list of available custom properties includes all of the items in the revision table, which includes items from the file summary items and file custom properties that have been set.

## See Also

[IRevisionTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.html)
[IRevisionTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation_members.html)
[IRevisionTableAnnotation::GetAllCustomProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetAllCustomProperties.html)
[IRevisionTableAnnotation::GetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetColumnCustomProperty.html)
[IRevisionTableAnnotation::SetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~SetColumnCustomProperty.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
