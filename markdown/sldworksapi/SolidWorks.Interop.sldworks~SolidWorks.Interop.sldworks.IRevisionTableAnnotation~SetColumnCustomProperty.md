---
title: "SetColumnCustomProperty Method (IRevisionTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IRevisionTableAnnotation"
member: "SetColumnCustomProperty"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~SetColumnCustomProperty.html"
---

# SetColumnCustomProperty Method (IRevisionTableAnnotation)

Sets the custom property used for the values in a specified user-defined column.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetColumnCustomProperty( _
   ByVal Index As System.Integer, _
   ByVal CustomProp As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionTableAnnotation
Dim Index As System.Integer
Dim CustomProp As System.String
Dim value As System.Boolean

value = instance.SetColumnCustomProperty(Index, CustomProp)
```

### C#

```csharp
System.bool SetColumnCustomProperty(
   System.int Index,
   System.string CustomProp
)
```

### C++/CLI

```cpp
System.bool SetColumnCustomProperty(
   System.int Index,
   System.String^ CustomProp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Column for which to get the custom property
- `CustomProp`: Custom property used for the values in this user-defined column

### Return Value

True if custom property is successfully set, false if not

## VBA Syntax

See [RevisionTableAnnotation::SetColumnCustomProperty](ms-its:sldworksapivb6.chm::/sldworks~RevisionTableAnnotation~SetColumnCustomProperty.html).

## Remarks

Use this method to create a user-defined column where each row in the column is automatically filled in with the custom property value. The default title for the column is the name of the custom property. If the specified custom property is not a valid custom property, then each row in the column remains empty.

To create a user-defined column that is not attached to a custom property; for example, you want to fill in each row of the column yourself, use this method with the CustomProp value specified as the title of the column.

To get the list of available custom properties, use [IRevisionTableAnnotation::GetAllCustomProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableAnnotation~GetAllCustomProperties.html) or [IRevisionTableAnnotation::IGetAllCustomProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableAnnotation~IGetAllCustomProperties.html). The list of possible custom properties includes all of the items in the revision table, which includes items from the file summary items and file custom properties that have been set.

This method returns false if the column is not a user-defined column, and no action is taken.

## See Also

[IRevisionTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.html)
[IRevisionTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation_members.html)
[IRevisionTableAnnotation::GetAllCustomPropertiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetAllCustomPropertiesCount.html)
[IRevisionTableAnnotation::GetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetColumnCustomProperty.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
