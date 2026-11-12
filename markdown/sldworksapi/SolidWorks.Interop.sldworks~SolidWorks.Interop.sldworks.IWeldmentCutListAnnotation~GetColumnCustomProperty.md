---
title: "GetColumnCustomProperty Method (IWeldmentCutListAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentCutListAnnotation"
member: "GetColumnCustomProperty"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~GetColumnCustomProperty.html"
---

# GetColumnCustomProperty Method (IWeldmentCutListAnnotation)

Gets the custom property for the specified user-defined column.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetColumnCustomProperty( _
   ByVal Index As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentCutListAnnotation
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

- `Index`: Column for which to get the custom property

### Return Value

Custom property for this user-defined column

## VBA Syntax

See [WeldmentCutListAnnotation::GetColumnCustomProperty](ms-its:sldworksapivb6.chm::/sldworks~WeldmentCutListAnnotation~GetColumnCustomProperty.html).

## Remarks

This method returns an empty string if the column is not a user-defined column.

To get the list of custom properties, use [IWeldmentCutListAnnotation::GetAllCustomProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentCutListAnnotation~GetAllCustomProperties.html) or [IWeldmentCutListAnnotation::IGetAllCustomProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentCutListAnnotation~IGetAllCustomProperties.html). The list of possible custom properties includes all of the items in the weldment cut list annotation table, which includes items from the file summary items and file custom properties that have been set.

## See Also

[IWeldmentCutListAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation.html)
[IWeldmentCutListAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation_members.html)
[IWeldmentCutListAnnotation::SetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~SetColumnCustomProperty.html)
[IWeldmentCutListAnnotation::GetAllCustomPropertiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~GetAllCustomPropertiesCount.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
