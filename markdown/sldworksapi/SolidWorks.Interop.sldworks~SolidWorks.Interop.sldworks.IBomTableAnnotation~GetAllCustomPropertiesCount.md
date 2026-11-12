---
title: "GetAllCustomPropertiesCount Method (IBomTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IBomTableAnnotation"
member: "GetAllCustomPropertiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetAllCustomPropertiesCount.html"
---

# GetAllCustomPropertiesCount Method (IBomTableAnnotation)

Gets the number of items in the list of available custom properties that can be used for a custom properties column in this BOM table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAllCustomPropertiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableAnnotation
Dim value As System.Integer

value = instance.GetAllCustomPropertiesCount()
```

### C#

```csharp
System.int GetAllCustomPropertiesCount()
```

### C++/CLI

```cpp
System.int GetAllCustomPropertiesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of available custom properties

## VBA Syntax

See [BomTableAnnotation::GetAllCustomPropertiesCount](ms-its:sldworksapivb6.chm::/sldworks~BomTableAnnotation~GetAllCustomPropertiesCount.html).

## Remarks

Call this method before calling [IBomTableAnnotation::IGetAllCustomProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation~IGetAllCustomProperties.html).

The list of possible custom properties includes all of the items in the BOM table, which includes items from the file summary items and file custom properties that have been set.

## See Also

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html)
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html)
[IBomTableAnnotation::GetAllCustomProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~GetAllCustomProperties.html)
[IBomTableAnnotation::SetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~SetColumnCustomProperty.html)

## Availability

SOLIDWORKS 2004 SP1, Revision Number 12
