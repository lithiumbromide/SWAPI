---
title: "GetColumnCustomProperty Method (IRevisionTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IRevisionTableAnnotation"
member: "GetColumnCustomProperty"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetColumnCustomProperty.html"
---

# GetColumnCustomProperty Method (IRevisionTableAnnotation)

Gets the custom property used for the values in a specified user-defined column.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetColumnCustomProperty( _
   ByVal Index As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionTableAnnotation
Dim Index As System.Integer
Dim value As System.String

value = instance.GetColumnCustomProperty(Index)
```

### C#

```csharp
System.string GetColumnCustomProperty(
   System.int Index
)
```

### C++/CLI

```cpp
System.String^ GetColumnCustomProperty(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Column from which to get the custom property

### Return Value

Custom property used for the values in this user-defined column

## VBA Syntax

See [RevisionTableAnnotation::GetColumnCustomProperty](ms-its:sldworksapivb6.chm::/sldworks~RevisionTableAnnotation~GetColumnCustomProperty.html).

## Remarks

This method returns a empty string if the column is not a user-defined column.

To get the list of custom properties, use [IRevisonTableAnnotation::GetAllCustomProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableAnnotation~GetAllCustomProperties.html) or [IRevisionTableAnnotation::IGetAllCustomProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableAnnotation~IGetAllCustomProperties.html). The list of available custom properties includes all of the items in the revision table, which includes items from the file summary items and file custom properties that have been set.

## See Also

[IRevisionTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.html)
[IRevisionTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation_members.html)
[IRevisionTableAnnotation::GetAllCustomPropertiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetAllCustomPropertiesCount.html)
[IRevisionTableAnnotation::SetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~SetColumnCustomProperty.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
