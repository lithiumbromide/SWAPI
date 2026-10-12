---
title: "IGetAllCustomProperties Method (IWeldmentCutListAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentCutListAnnotation"
member: "IGetAllCustomProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~IGetAllCustomProperties.html"
---

# IGetAllCustomProperties Method (IWeldmentCutListAnnotation)

Gets the list of available custom properties that could be used for a custom properties column in this weldment cut list table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAllCustomProperties( _
   ByVal Count As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentCutListAnnotation
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

Before calling this method, call [IWeldmentCutListAnnotation::GetAllCustomPropertiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentCutListAnnotation~GetAllCustomPropertiesCount.html) to get Count.

The list of available custom properties includes all of the items in the weldment cut list table, which includes items from the file summary items and file custom properties that have been set.

## See Also

[IWeldmentCutListAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation.html)
[IWeldmentCutListAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation_members.html)
[IWeldmentCutListAnnotation::GetAllCustomProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~GetAllCustomProperties.html)
[IWeldmentCutListAnnotation::GetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~GetColumnCustomProperty.html)
[IWeldmentCutListAnnotation::SetColumnCustomProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~SetColumnCustomProperty.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
