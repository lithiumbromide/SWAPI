---
title: "GetAllCustomProperties Method (IRevisionTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IRevisionTableAnnotation"
member: "GetAllCustomProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetAllCustomProperties.html"
---

# GetAllCustomProperties Method (IRevisionTableAnnotation)

Gets a list of available custom properties that can be used for a custom properties column in this revision table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAllCustomProperties() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionTableAnnotation
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

See [RevisionTableAnnotation::GetAllCustomProperties](ms-its:sldworksapivb6.chm::/sldworks~RevisionTableAnnotation~GetAllCustomProperties.html).

## Remarks

This method only works for SOLIDWORKS documents created or saved in SOLIDWORKS 2005 or later.

The list of available custom properties includes all of the items in the revision table, which includes items from the file summary items and file custom properties that have been set.

## See Also

[IRevisionTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.html)
[IRevisionTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation_members.html)
[IRevisionTableAnnotation::GetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetColumnCustomProperty.html)
[IRevisionTableAnnotation::IGetAllCustomProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~IGetAllCustomProperties.html)
[IRevisionTableAnnotation::SetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~SetColumnCustomProperty.html)
[IRevisionTableAnnotation::GetAllCustomPropertiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetAllCustomPropertiesCount.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
