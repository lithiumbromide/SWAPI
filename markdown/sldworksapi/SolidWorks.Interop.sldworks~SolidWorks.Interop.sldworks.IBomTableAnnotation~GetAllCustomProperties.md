---
title: "GetAllCustomProperties Method (IBomTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IBomTableAnnotation"
member: "GetAllCustomProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetAllCustomProperties.html"
---

# GetAllCustomProperties Method (IBomTableAnnotation)

Gets the list of available custom properties that can be used for a custom properties column in this BOM table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAllCustomProperties() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableAnnotation
Dim value As System.Object

value = instance.GetAllCustomProperties()
```

### C#

```csharp
System.object GetAllCustomProperties()
```

### C++/CLI

```cpp
System.Object^ GetAllCustomProperties();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of strings of available custom properties

## VBA Syntax

See [BomTableAnnotation::GetAllCustomProperties](ms-its:sldworksapivb6.chm::/sldworks~BomTableAnnotation~GetAllCustomProperties.html).

## Examples

[Get Available Custom Properties for BOM Table (VBA)](Get_Available_Custom_Properties_for_BOM_Table_Example_VB.htm)

## Remarks

To get the number of custom properties, use [IBomTableAnnotation::GetAllCustomPropertiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation~GetAllCustomPropertiesCount.html).

The list of available custom properties includes all of the items in the BOM table, which includes items from the file summary items and file custom properties that have been set.

## See Also

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html)
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html)
[IBomTableAnnotation::IGetAllCustomProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~IGetAllCustomProperties.html)
[IBomTableAnnotation::GetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetColumnCustomProperty.html)

## Availability

SOLIDWORKS 2004 SP1, Revision Number 12
