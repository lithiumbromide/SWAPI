---
title: "GetAllCustomPropertiesCount Method (IRevisionTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IRevisionTableAnnotation"
member: "GetAllCustomPropertiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetAllCustomPropertiesCount.html"
---

# GetAllCustomPropertiesCount Method (IRevisionTableAnnotation)

Gets the number of items in the list of available custom properties that can be used for a custom properties column in this revision table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAllCustomPropertiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionTableAnnotation
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

See [RevisionTableAnnotation::GetAllCustomPropertiesCount](ms-its:sldworksapivb6.chm::/sldworks~RevisionTableAnnotation~GetAllCustomPropertiesCount.html).

## Remarks

Call this method before calling [IRevisionTableAnnotation::IGetAllCustomProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableAnnotation~IGetAllCustomProperties.html) to get the value of Count.

The list of available custom properties includes all of the items in the revision table, which includes items from the file summary items and file custom properties that have been set.

## See Also

[IRevisionTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.html)
[IRevisionTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation_members.html)
[IRevisionTableAnnotation::GetAllCustomProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetAllCustomProperties.html)
[IRevisionTableAnnotation::GetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetColumnCustomProperty.html)
[IRevisionTableAnnotation::SetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~SetColumnCustomProperty.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
